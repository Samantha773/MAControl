# coding=utf-8

import argparse
import time
import MAControl.PTMA_CBAA.InnerController_PID as IC_P
import MAControl.PTMA_CBAA.MotionController_L1_TECS as MC_L
import MAControl.PTMA_CBAA.PathPlanner_Shared as PP_S
import MAControl.PTMA_CBAA.PolicyMaker_Probability as PM_A
import logging
import os

# 运行 execute_Probability.py 需要补足参数，如 execute_all_P1/P2/P3/P4_unit/Q.py 中所示
logging.basicConfig(filename='\\Users\\xj\\PycharmProjects\\Result-A\\P1234_unit.log', level=logging.INFO)
logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
logging.info(time.strftime('%Y-%m-%d, %H:%M:%S'))
logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 需要自行指定为本地存在的绝对路径，指定名称的文件如果不存在，会自动创建
# 如果存在，不会覆盖内容，会从结尾处向后添加新内容


def parse_args():
    parser = argparse.ArgumentParser("Control Experiments for Multi-Agent Environments")
    parser.add_argument("--scenario", type=str, default="scenario_paper", help="name of the scenario script")
    parser.add_argument("--step-max", type=int, default=3000, help="maximum steps")
    parser.add_argument("--episode-max", type=int, default=30, help="maximum episodes")
    parser.add_argument("--p1", action='append', type=float, dest='p1', default=[], help="P: Line one")
    parser.add_argument("--p2", action='append', type=float, dest='p2', default=[], help="P: Line Two")
    parser.add_argument("--p3", action='append', type=float, dest='p3', default=[], help="P: Line Three")
    parser.add_argument("--q1", action='append', type=float, dest='q1', default=[], help="Q: Line One")
    parser.add_argument("--q2", action='append', type=float, dest='q2', default=[], help="Q: Line Two")
    parser.add_argument("--q3", action='append', type=float, dest='q3', default=[], help="Q: Line Three")
    parser.add_argument("--numU", type=int, default=5, help="how many UAVs")
    parser.add_argument("--typeT", action='append', type=int, dest='typeT', default=[], help="target types")

    return parser.parse_args()


def make_env(arglist):
    from MAEnv.environment import MultiAgentEnv
    import MAEnv.scenarios as scenarios

    # load scenario from script
    scenario = scenarios.load(arglist.scenario + ".py").Scenario()

    # create world and env
    world = scenario.make_s_world(arglist.numU, arglist.typeT)
    env = MultiAgentEnv(world, scenario.reset_world, scenario.reward, scenario.observation)
    return env, world


def get_controller(env, world, arglist):
    ControllerSet = []

    for i in range(env.n):
        control = []
        control.append(PM_A.PolicyMaker_Probability("agent_%d" % i, env, world, i, arglist))
        control.append(PP_S.PathPlanner_Shared("agent_%d" % i, env, world, i, arglist))
        control.append(MC_L.MotionController_L1_TECS("agent_%d" % i, env, world, i, arglist))
        control.append(IC_P.InnerController_PID("agent_%d" % i, env, world, i, arglist))
        control.append(False)  # Arriveflag
        control.append(False)  # Isattacking
        control.append(-1)  # which target is it attacking
        ControllerSet.append(control)

    return ControllerSet


def update_action(env, world, obs_n, step, NewController):

    WorldTarget = []
    for i, landmark in enumerate(world.targets):
        WorldTarget.append([landmark.state.p_pos[0], landmark.state.p_pos[1], landmark.value,
                            landmark.a_defence, landmark.b_defence, landmark.type, i])
    # print(step)
    action_n = []
    for i in range(env.n):

        list_i = NewController[i][0]. \
            make_policy(WorldTarget, obs_n, step)

        NewController[i][6] = list_i[1][2]

        pointAi, pointBi, finishedi, NewController[i][5] = NewController[i][1].\
            planpath(list_i, obs_n[i], NewController[i][4], step)

        acctEi, acclEi, NewController[i][4] = NewController[i][2]. \
            get_expected_action(obs_n[i], pointAi, pointBi, step, finishedi)

        actioni = NewController[i][3]. \
            get_action(obs_n[i], acctEi, acclEi, step, finishedi)

        action_n.append(actioni)

    return action_n


def augment_view(env, world, NewController):
    for i in range(env.n):
        world.agents[i].attacking_to = NewController[i][6]
        if NewController[i][5]:
            world.agents[i].attacking = True


if __name__ == '__main__':
    arglist = parse_args()
    logging.info(arglist)
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    # Create environment
    env, world = make_env(arglist)

    episode = 0
    t_start = time.time()

    while episode < arglist.episode_max:

        # Create Controller (重置实例变量)
        NewController = get_controller(env, world, arglist)

        # Rest Controller (重置类变量)
        PM_A.PolicyMaker_Probability.SEEN_TARGETS = []
        PM_A.PolicyMaker_Probability.KNOWN_TARGETS = []
        PM_A.PolicyMaker_Probability.RESULT = []
        PM_A.PolicyMaker_Probability.Prices = []
        PM_A.PolicyMaker_Probability.Occupied_U = []
        PM_A.PolicyMaker_Probability.Attacked_T = []

        obs_n = env.reset()
        episode += 1
        step = 0

        while step <= arglist.step_max:

            # get action
            # print('>>> step ', step)
            action_n = update_action(env, world, obs_n, step, NewController)

            # environment step
            new_obs_n, rew_n, done_n, info_n = env.step(action_n)
            step += 1
            obs_n = new_obs_n

            # for displaying
            augment_view(env, world, NewController)
            # env.render()  # could be commented out

            # for recording
            if step == arglist.step_max:
                print('>>>>>>>>>>> Episode', episode)
                pairing = []
                for i in range(env.n):
                    pairing.append(world.agents[i].attacking_to)
                print('pairing: ', pairing)
                print('reward:', rew_n[0][0])
                timing = round(time.time() - t_start, 3)
                t_start = time.time()
                print('timing: ', timing)
                if episode == 1:
                    logging.info('EPISODE | PAIRING                                               REWARD          TIME')
                logging.info([episode]+pairing+[rew_n[0][0]]+[timing])
                print('\n')
                if episode == arglist.episode_max:
                    logging.info('\n')
