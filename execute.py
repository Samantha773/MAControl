# coding=utf-8
import argparse
import time
import MAControl.TESTControl as TESTC
import MAControl.util as U


def parse_args():
    parser = argparse.ArgumentParser("Control Experiments for Multi-Agent Environments")
    parser.add_argument("--scenario", type=str, default="scenario_DIY", help="name of the scenario script")
    parser.add_argument("--step-max", type=int, default=4000, help="maximum steps")
    return parser.parse_args()


def make_env(arglist):
    print('make_env')
    from MAEnv.environment import MultiAgentEnv
    import MAEnv.scenarios as scenarios

    # load scenario from script
    scenario = scenarios.load(arglist.scenario + ".py").Scenario()

    # create world and env
    world = scenario.make_world()
    env = MultiAgentEnv(world, scenario.reset_world, scenario.reward, scenario.observation)
    return env, world


if __name__ == '__main__':
    arglist = parse_args()

    # Create environment
    env, world = make_env(arglist)

    # Create Controllers
    Control = []
    for i in range(env.n):
        Control.append(TESTC.TESTControl("agent_%d" % i, env, world, i, arglist))
        Control[i].waypoint_list[0:len(U.init_waypoint[i])] = U.init_waypoint[i]

    obs_n = env.reset()
    step = 0
    start = time.time()

    while True:

        # get action
        action_n = []
        for i in range(env.n):
            pointAi, pointBi, finishedi = Control[i].PathPlanner(obs_n[i])
            actioni = Control[i].MotionController(obs_n[i], pointAi, pointBi)
            action_n.append(actioni)

        # environment step
        new_obs_n, rew_n, done_n, info_n = env.step(action_n)
        step += 1
        obs_n = new_obs_n

        # for displaying
        time.sleep(0.05)
        env.render()
        print('>>>> step', step)
        print('obs_n', obs_n)
        print('action_n', action_n)
