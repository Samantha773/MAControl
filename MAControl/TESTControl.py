import numpy as np
import math
import os
import MAControl.util as U


class TESTControl():
    def __init__(self, name, env, world, agent_index, arglist):
        print("control init")
        self.name = name
        self.env = env
        self.world = world
        self.index = agent_index
        self.arglist = arglist
        self.dt = world.dt

        self.vel = (0, 0)
        self.pos = (0, 0)
        self.pointAi = (0, 0)
        self.pointBi = (0, 0)

        self.throttle_setpoint = 0
        self.action = [0, 0, 0, 0, 0]

        self.waypoint_finished = False
        self.arrive_flag = False
        self.pointB_index = 0
        # 256×3的航点列表，第3列为航点状态 [0: 无航点] [1: 未飞] [2: pointA] [3: pointB] [4: 已到达]
        self.waypoint_list = [[0 for i in range(3)] for j in range(256)]

    def PathPlanner(self, obs):
        print("path plan")

        # TODO:根据obs进行判断是否修改航点列表
        # if True:
        #     self.WaypointUpdater(obs)

        # 初始时刻输出A、B坐标
        if self.pointB_index == 0:
            self.pointA = (obs[2], obs[3])
            self.pointB = (self.waypoint_list[self.pointB_index][0], self.waypoint_list[self.pointB_index][1])

        # 更改航点状态并输出A、B坐标
        if self.arrive_flag:
            if self.waypoint_list[self.pointB_index+1][2] != 0 and self.pointB_index < 255:
                if self.pointB_index > 0:
                    self.waypoint_list[self.pointB_index-1][2] = 4
                self.waypoint_list[self.pointB_index][2] = 2
                self.waypoint_list[self.pointB_index+1][2] = 3
                self.pointA = (self.waypoint_list[self.pointB_index][0], self.waypoint_list[self.pointB_index][1])
                self.pointB = (self.waypoint_list[self.pointB_index+1][0], self.waypoint_list[self.pointB_index+1][1])
                self.arrive_flag = False
                self.pointB_index += 1
            else:
                self.waypoint_list[self.pointB_index-1][2] = 4
                self.waypoint_list[self.pointB_index][2] = 4
                self.pointB_index = 0
                self.pointA = (self.waypoint_list[self.pointB_index][0], self.waypoint_list[self.pointB_index][1])
                self.pointB = (self.waypoint_list[self.pointB_index + 1][0], self.waypoint_list[self.pointB_index + 1][1])
                # self.waypoint_finished = True

        return self.pointA, self.pointB, self.waypoint_finished

    def MotionController(self, obs, pointAi, pointBi):
        print("motion control")
        self.vel = np.array(obs[0:2])
        self.pos = np.array(obs[2:4])
        pointAi = np.array(pointAi)
        pointBi = np.array(pointBi)

        # set L1 params
        L1_ratio = 0.1
        BP_range = 0.3
        Ex_speed = 7
        K_L1 = 0.02
        K_acct = 0.02

        # set tecs params
        TAS_setpoint = 7
        STE_rate_max = 0.05
        STE_rate_min = 0.01
        speed_error_gain = 0.02
        throttle_cruise = 0.5
        throttle_damping_gain = 0.5
        throttle_time_constant = 0.5
        throttle_setpoint_max = 1
        throttle_setpoint_min = 0
        throttle_slewrate = 0.02

        # update speed setpoint
        speed = np.sqrt(np.square(self.vel[0]) + np.square(self.vel[1]))
        tas_state = speed
        velRateMax = 0.5 * STE_rate_max / tas_state
        velRateMin = 0.5 * STE_rate_min / tas_state
        TAS_rate_setpoint = (TAS_setpoint - tas_state) * speed_error_gain
        TAS_rate_setpoint = U.constrain(TAS_rate_setpoint, velRateMin, velRateMax)

        # update energy estimates
        SKE_setpoint = 0.5 * TAS_setpoint * TAS_setpoint
        SKE_rate_setpoint = tas_state * TAS_rate_setpoint
        SKE_estimate = 0.5 * tas_state * tas_state
        SKE_rate = 0

        # update throttle setpoint
        STE_error = SKE_setpoint - SKE_estimate
        STE_rate_setpoint = U.constrain(SKE_rate_setpoint, STE_rate_min, STE_rate_max)
        STE_rate_error = STE_rate_setpoint - SKE_rate
        if STE_rate_setpoint >= 0:
            throttle_p = throttle_cruise + STE_rate_setpoint / STE_rate_max * (throttle_setpoint_max - throttle_cruise)
        else:
            throttle_p = throttle_cruise + STE_rate_setpoint / STE_rate_min * (throttle_setpoint_min - throttle_cruise)
        STE_to_throttle = 1 / throttle_time_constant / (STE_rate_max - STE_rate_min)
        throttle_setpoint = (STE_error + STE_rate_error * throttle_damping_gain) * STE_to_throttle + throttle_p
        throttle_setpoint = U.constrain(throttle_setpoint, throttle_setpoint_min, throttle_setpoint_max)
        throttle_increment_limit = self.dt * (throttle_setpoint_max - throttle_setpoint_min) * throttle_slewrate
        throttle_setpoint = U.constrain(throttle_setpoint, self.throttle_setpoint - throttle_increment_limit,
                                        self.throttle_setpoint + throttle_increment_limit)
        self.throttle_setpoint = throttle_setpoint
        throttle_setpoint = U.constrain(throttle_setpoint, throttle_setpoint_min, throttle_setpoint_max)

        # compute L1
        L1_distance = speed * L1_ratio
        print('L1_distance', L1_distance)

        # compute AB
        vector_AB = pointBi-pointAi
        dist_AB = np.sqrt(np.square(vector_AB[0]) + np.square(vector_AB[1]))
        vector_AB_unit = vector_AB/dist_AB

        # compute AP
        vector_AP = self.pos-pointAi
        dist_AP = np.sqrt(np.square(vector_AP[0]) + np.square(vector_AP[1]))
        dist_AP = max(dist_AP, 0.000000001)
        vector_AP_unit = vector_AP/dist_AP

        # compute BP
        vector_BP = self.pos - pointBi
        dist_BP = np.sqrt(np.square(vector_BP[0]) + np.square(vector_BP[1]))
        print('dist_BP', dist_BP)
        self.arrive_flag = True if dist_BP < BP_range else False
        vector_BP_unit = vector_BP/dist_BP

        # extra computation
        alongTrackDist = np.dot(vector_AP, vector_AB_unit)
        AB_to_BP_bearing = math.acos(U.constrain(np.dot(vector_AB_unit, vector_BP_unit), -1, 1))

        if dist_AP > L1_distance and alongTrackDist/dist_AP < -0.707:
            # calculate eta to fly to waypoint A
            eta = math.acos(U.constrain(np.dot(-1 * vector_AP_unit, self.vel/speed), -1, 1))
            print('scene1')

        elif abs(AB_to_BP_bearing) < math.radians(100):
            # calculate eta to fly to waypoint B
            eta = math.acos(np.dot(-1 * vector_BP_unit, self.vel/speed))
            print('scene2')

        else:
            # calculate eta to fly along the line between A and B
            eta2 = math.acos(U.constrain(np.dot(vector_AB_unit, self.vel/speed), -1, 1))
            beta = math.acos(U.constrain(np.dot(vector_AP_unit, vector_AB_unit), -1, 1))
            xtrackErr = dist_AP * math.sin(beta)
            eta1 = math.asin(U.constrain(xtrackErr / L1_distance, -0.7071, 0.7071))
            eta = eta1 + eta2
            print('scene3')

        # compute eta >>> lateral_acc_size
        eta = U.constrain(eta, -1.5708, 1.5708)
        lateral_acc_size = speed * speed / L1_distance * math.sin(eta) * K_L1
        print('lateral_acc_size', lateral_acc_size)

        # compute lateral_acc_unit >>> lateral_acc
        lateral_acc_unit = np.array([self.vel[1], -1*self.vel[0]])/speed
        if np.dot(lateral_acc_unit, vector_AB_unit) > 0 or \
                np.dot(lateral_acc_unit, vector_AB_unit) == 0 < np.dot(lateral_acc_unit, -1 * vector_AP_unit):
            lateral_acc_unit = np.array([-1*self.vel[1], self.vel[0]])/speed
        lateral_acc = lateral_acc_unit * lateral_acc_size

        # TODO: replaced by tecs
        tangent_acc_unit = self.vel/speed
        tangent_acc_size = (speed - Ex_speed) * K_acct
        print('tangent_acc_size', tangent_acc_size)
        tangent_acc = tangent_acc_unit * tangent_acc_size

        # compute acc >>> action
        acc = lateral_acc + tangent_acc
        self.action[2] = acc[0]
        self.action[4] = acc[1]
        return self.action



