import gym
import exercise1.car_maze as cm
import random as rnd
import time
import maze_resolver_c

env = cm.CarMazeEnv()

#####################################
# You code starts here
#####################################

for i_episode in range(1):
    observation = env.reset()
    # --------------------------------------------
    # simzim code
    # --------------------------------------------
    maze = {}
    current = '0-0'
    gold = observation[5]
    visited = []
    path = []

    for t in range(200000):
        env.render()

        time.sleep(0.2)
        # sukuriamas taško kaimynų dict
        neighbours = maze_resolver_c.get_neighbours(observation, current, gold)
        path.append(current)
        visited.append(current)
        step = maze_resolver_c.find_next(neighbours, visited, path)
        action = maze_resolver_c.do_step(current, step)
        current = step

        # --------------------------------------------
        # end of simzim code
        # --------------------------------------------
        observation, reward, done, info = env.step(action)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print("Reward - " + reward)
            break

env.close()
