# 环境长度 1 = 实际长度 1000 米 = 1 千米

import numpy as np
import random
from MAEnv.core import World, Agent, Landmark
from MAEnv.scenario import BaseScenario
import MAEnv.scenarios.TargetProfile as T
import math


class Scenario(BaseScenario):
    def make_s_world(self, agent_num, target_type):
        world = World()
        # set any world properties first
        world.damping = 0  # 取消第一种阻尼计算方式
        world.damping2 = 10  # 调整第二种阻尼计算方式的参数
        # set nums
        num_agents = agent_num
        num_targets = T.num_targets
        num_obstacles = 0
        num_grids = 5
        # add agents
        world.agents = [Agent() for i in range(num_agents)]
        for i, agent in enumerate(world.agents):
            agent.name = 'agent %d' % i
            agent.collide = False
            agent.silent = True
            agent.size = 0.01  # 10米
        # add landmarks
        world.targets = [Landmark() for i in range(num_targets)]
        VALUE = [70, 50, 90]
        A_DEFENCE = [3, 4, 2]
        B_DEFENCE = [2, 1, 3]
        for i, landmark in enumerate(world.targets):
            landmark.name = 'target %d' % i
            landmark.collide = False
            landmark.movable = False
            landmark.value = VALUE[target_type[i]-1]
            landmark.size = T.target_size[i] * 0.01
            landmark.a_defence = A_DEFENCE[target_type[i]-1]
            landmark.b_defence = B_DEFENCE[target_type[i]-1]
            landmark.attacking = False
            landmark.type = target_type[i]
        world.obstacles = [Landmark() for i in range(num_obstacles)]
        for i, landmark in enumerate(world.obstacles):
            landmark.name = 'obstacle %d' % i
            landmark.collide = False
            landmark.movable = False
            landmark.size = np.ceil(random.random()*10)*0.01
            landmark.attacking = False
        world.grids = [Landmark() for i in range(num_grids)]
        for i, landmark in enumerate(world.grids):
            landmark.name = 'grid %d' % i
            landmark.collide = False
            landmark.movable = False
            landmark.size = 0.005
            landmark.attacking = False
        world.landmarks = world.targets + world.obstacles + world.grids
        # make initial conditions
        self.reset_world(world)
        return world

    def reset_world(self, world):

        for i, agent in enumerate(world.agents):
            agent.state.p_pos = np.random.uniform(T.agent_pos_init[0], T.agent_pos_init[1], world.dim_p)
            agent.state.p_vel = np.array([0, 0.05])  # 50 米/秒
            agent.state.p_acc = np.array([0, 0])
            agent.color = T.agent_color
            agent.attacking = False
            agent.attacking_to = -1

        for i, landmark in enumerate(world.landmarks):
            landmark.state.p_vel = np.zeros(world.dim_p)
            if i < len(world.targets):
                landmark.color = np.random.uniform(0, 1, 3)
                landmark.state.p_pos = np.array(T.target_pos[i])
            else:
                landmark.color = T.grid_color
                landmark.state.p_pos = np.array(T.grid_pos[i-len(world.targets)])

    def benchmark_data(self, agent, world):
        # returns data for benchmarking purposes
        rew = 0
        occupied_landmarks = 0
        min_dists = 0
        for l in world.landmarks:
            dists = [np.sqrt(np.sum(np.square(a.state.p_pos - l.state.p_pos))) for a in world.agents]
            min_dists += min(dists)
            rew -= min(dists)
            if min(dists) < 0.1:
                occupied_landmarks += 1
        return rew, min_dists, occupied_landmarks

    def result(self, world):
        # TARGET-UAV 分配情况 TASK-TIME
        X_JA = [0 for j in range(len(world.targets))]
        X_JB = [0 for j in range(len(world.targets))]
        for a, agent in enumerate(world.agents):
            task = [agent.attacking_to, agent.attacking_type, agent.attacking_time]
            # 长度为UAV数量，每个元素是 [所攻击的目标，任务类型(A/B)，转入攻击的时刻(step) ]
            if task[1] == 'A':
                X_JA[task[0]] += 1
            elif task[1] == 'B':
                X_JB[task[0]] += 1
            else:
                pass

        E_JA = []
        E_JB = []
        W = []
        for j in range(len(world.targets)):
            E_JA.append(world.targets[j].a_defence)
            E_JB.append(world.targets[j].b_defence)
            W.append(world.targets[j].value)

        F = []
        for j in range(len(world.targets)):
            delta = 10
            ra = abs(X_JA[j] - E_JA[j])+10
            rb = abs(X_JB[j] - E_JB[j])+10
            F.append(delta*W[j]/ra/rb)
        return F

    def reward(self, agent, world):
        F_list = self.result(world)
        return sum(F_list)

    def observation(self, agent, world):
        a1 = agent.state.p_acc[0]
        a2 = agent.state.p_acc[1]
        vel_size = np.sqrt(np.square(agent.state.p_vel[0]) + np.square(agent.state.p_vel[1]))
        vel_front_unit = agent.state.p_vel / vel_size
        vel_right_unit = np.array([agent.state.p_vel[1], -1 * agent.state.p_vel[0]]) / vel_size
        a_front = np.dot(a1, vel_front_unit) + np.dot(a2, vel_front_unit)
        a_right = np.dot(a2, vel_right_unit) + np.dot(a2, vel_right_unit)
        return np.concatenate([agent.state.p_vel] + [agent.state.p_pos] + [a_front] + [a_right])
