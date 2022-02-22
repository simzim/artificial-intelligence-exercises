import gym
import exercise1.car_maze as cm
import random as rnd
import time
import maze_resolver_b

env = cm.CarMazeEnv()



for i_episode in range(1):
    observation = env.reset()

    # --------------------------------------------
    # simzim code
    # --------------------------------------------

    maze = {}           # nebutina, bet vis tiek smagu :)
    current = '0-0'
    visited = []
    path = []

    for t in range(200000):
        env.render()
        time.sleep(0.2)

        # sukuriamas taško kaimynų sąrašas
        neighbours = maze_resolver_b.get_neighbours(observation, current)

        maze[current] = neighbours              # isidedam i maze dicionary for fun :)
        path.append(current)                    # isidedam i nueita kelia esama taska
        visited.append(current)                 # visi aplankyti taskai

        # renkames sekanti zingsni
        step = maze_resolver_b.find_next(neighbours, visited, path)
        # zingsniuojam
        action = maze_resolver_b.do_step(current, step)
        current = step

        observation, reward, done, info = env.step(action)

        if done:
            print('SVEIKINAM LAIMĖJOTE :)')
            print("Episode finished after {} timesteps".format(t+1))
            print("Reward - " + reward)
            break
        # --------------------------------------------
        # end of simzim code
        # --------------------------------------------
env.close()
