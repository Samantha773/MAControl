# 环境长度 1 = 实际长度 1000 米 = 1 千米
# 初步应用了 entity = agent + landmark 和 agent = uav + target 的区分，删去了许多参数，仍需进一步修改
# (landmark = grid + obstacle + ...  , target = fixed_target + movable_target)
# 用来算的大小 vs 拿来看的大小 # 这个关系要理顺 视觉效果应该ok
# Require >=8 entities in the scenario for the codes to properly work -?

import numpy as np
import os
import math
from MAEnv.core import World, Agent, Landmark
from MAEnv.scenario import BaseScenario
import MAEnv.scenarios.TargetProfile as T


class Scenario(BaseScenario):
    def make_World(self, _uav_num):
        world = World()
        # set any world properties first
        world.damping = 0     # 取消第一种阻尼计算方式
        world.damping2 = 10   # 调整第二种阻尼计算方式的参数
        world.edge = T.edge   # 确定边界
        # set nums
        num_uav = _uav_num
        num_targets = T.num_targets
        num_grids = T.num_grids
        num_square = T.num_square  # zero for now

        # add agents (uavs)
        world.U_agents = [Agent() for i in range(num_uav)]
        for i, uav in enumerate(world.U_agents):
            uav.name = 'uav %d' % i
            uav.state.size = T.UAV_size * 0.01  # 10米
            uav.movable = True
            uav.UAV = True
            uav.H = T.UAV_H
            uav.Dam = T.UAV_Dam
            uav.w = T.UAV_w
            uav.rule = 'default'

        # add agents (targets)
        world.T_agents = [Agent() for i in range(num_targets)]
        for i, target in enumerate(world.T_agents):
            target.name = 'target %d' % i
            target.state.size = T.target_size[i] * 0.01
            if not T.target_movable[i]:
                target.movable = False
            target.Target = True
            target.H = T.target_H[i]
            target.Dam = T.target_Dam[i]
            target.w = T.target_w[i]

        # agents summary
        world.agents = world.U_agents + world.T_agents

        # add grids
        world.grids = [Landmark() for i in range(num_grids)]
        for i, grid in enumerate(world.grids):
            grid.name = 'grid %d' % i
            grid.state.size = T.grid_size
            grid.Landmark = True
            grid.obstacle = False

        # add squares
        world.squares = [Landmark() for i in range(num_square)]
        for i, square in enumerate(world.squares):
            square.name = 'square %d' % i
            square.state.size = T.square_size
            square.Landmark = True
            square.obstacle = True

        # landmarks summary
        world.landmarks = world.grids + world.squares

        # write-o
        curdir_ = os.path.dirname(__file__)  # current directory
        pardir_ = os.path.dirname(os.path.dirname(curdir_))  # parent parent directory
        para = np.loadtxt(pardir_ + '/track/para.txt')  # currently [10,3000]
        # self.collect = int(para[2])  # so ... wtf?

        # make initial conditions
        self.reset_world(world)
        return world

    def reset_world(self, world):

        uav_count = 0
        for i, agent in enumerate(world.agents):
            if agent.UAV:
                # agent.state.p_pos = np.array([-1.2, -0.4+i*0.2])
                # agent.state.p_pos = np.array([-1.3, 0.])
                agent.state.p_pos = np.random.uniform(-1.0, 1.0, world.dim_p)

                # agent.state.p_vel = np.array([0.01, 0.00])  # 10 米/秒
                agent.state.p_vel = np.random.uniform(-0.01, 0.01, world.dim_p)

                # agent.state.p_pos, agent.state.p_vel = T.init_state.get_state(self.collect, uav_count)

                agent.state.p_acc = np.array([0, 0])
                agent.color = T.UAV_color
                uav_count += 1
            else:
                agent.state.p_pos = np.array(T.target_pos[i-uav_count])
                agent.state.p_vel = np.array([0.01, 0.00])  # 10 米/秒
                agent.state.p_acc = np.array([0, 0])
                if agent.movable:
                    agent.color = T.movable_target_color
                else:
                    agent.color = T.fixed_target_color

        for i, landmark in enumerate(world.landmarks):
            landmark.state.p_vel = np.zeros(world.dim_p)
            if 'grid' in landmark.name:
                landmark.color = T.grid_color
                landmark.state.p_pos = T.grid_pos[i]
            elif 'square' in landmark.name:
                landmark.color = T.square_color
                landmark.state.p_pos = T.square_pos[i-T.num_grids]
            else:
                pass

    def benchmark_data(self, agent, world):
        # returns data for benchmarking purposes
        rew = agent.color[0] + world.edge
        return rew

    def reward(self, agent, world):
        rew = agent.color[0] + world.edge
        return rew

    def retina(self, agent, world):
        # 描述自己
        selfpos = agent.state.p_pos
        selfvel = agent.state.p_vel
        self_ornt = math.atan2(selfvel[1], selfvel[0])  # orientation = ORNT

        # 视场参数
        gamma = T.blind_angle[0]  # 整个盲区角
        G1 = math.fmod(self_ornt + math.pi - gamma/2, math.pi)  # so that -math.pi <= G1 <= math.pi
        G2 = math.fmod(G1 + gamma, math.pi)

        # 根据个体的方位 + 距离 + 大小 得到个体的投影角(1,2) + 距离
        # ## # entity size, bearing, distance -> entity projected-angles, distance
        retina = []  # each item = 3-tuple element
        for i, other in enumerate(world.agents):
            if other is not agent:
                relative_pos = other.state.p_pos - selfpos
                relative_dis = np.linalg.norm(relative_pos)
                relative_bearing = math.atan2(relative_pos[1], relative_pos[0])
                half_ang = math.atan2(other.state.size/2, relative_dis)
                r1 = math.fmod(relative_bearing - half_ang, math.pi)
                r2 = math.fmod(relative_bearing + half_ang, math.pi)
                r3 = relative_dis
                # ## # ↓↓ credit: KSB ↓↓ # ## #
                if abs(math.fmod(r1-G1, math.pi)) + abs(math.fmod(r1-G2, math.pi)) != gamma \
                        and abs(math.fmod(r2-G1, math.pi)) + abs(math.fmod(r2-G2, math.pi)) != gamma:
                    retina.append([r1, r2, r3])
                elif abs(math.fmod(r1-G1, math.pi)) + abs(math.fmod(r1-G2, math.pi)) == gamma \
                        and abs(math.fmod(r2-G1, math.pi)) + abs(math.fmod(r2-G2, math.pi)) == gamma:
                    retina.append([G1, G2, float('inf')])
                elif abs(math.fmod(r1-G1, math.pi)) + abs(math.fmod(r1-G2, math.pi)) == gamma:
                    retina.append([G2, r2, r3])
                else:
                    retina.append([r1, G1, r3])

        # output
        return retina

    def neighbouring_view(self, agent, world):
        _retina = self.retina(agent, world)
        _distance = [item[2] for item in _retina]

        neighborhood = []
        return neighborhood

    def projected_view(self, agent, world):

        projection = []
        return projection

    def observation(self, agent, world):
        a1 = agent.state.p_acc[0]
        a2 = agent.state.p_acc[1]
        vel_size = np.sqrt(np.square(agent.state.p_vel[0]) + np.square(agent.state.p_vel[1]))
        vel_front_unit = agent.state.p_vel / vel_size
        vel_right_unit = np.array([agent.state.p_vel[1], -1 * agent.state.p_vel[0]]) / vel_size
        a_front = np.dot([a1, 0], vel_front_unit) + np.dot([0, a2], vel_front_unit)
        a_right = np.dot([a1, 0], vel_right_unit) + np.dot([0, a2], vel_right_unit)
        n_view = self.neighbouring_view(agent, world)
        p_view = self.projected_view(agent, world)
        return np.concatenate([agent.state.p_vel] + [agent.state.p_pos] + [[a_front]] + [[a_right]] + [n_view]+[p_view])
