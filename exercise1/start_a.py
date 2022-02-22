import gym
import exercise1.car_maze as cm
import random as rnd
import time
import maze_resolver

env = cm.CarMazeEnv("open")

#################################################
# Observation space value meanings by list index:
# 0 - up       (values: 0 - road blocked,  1 - road available)
# 1 - down
# 2 - left
# 3 - right
# 4 - ID position of car
# 5 - ID position of gold
# 6 - roads / possible moves of the maze. Tuple of two ID values (from, to)
#
###########################
# Action space values
# 0 - up
# 1 - down
# 2 - left
# 3 - right

#####################################
# You code starts here
#####################################

# print("0 - up")
# print("1 - down")
# print("2 - left")
# print("3 - right")

for i_episode in range(10):
    observation = env.reset()

    env.render()
    path = maze_resolver.maze_resolve(observation)
    #path.reverse()

    for t in range(200000):
        env.render()

        # --------------------------------------------
        # simzim code
        # --------------------------------------------

        time.sleep(0.2)
        step = path.pop()
        x_axis = observation[4].split('-')[0]
        y_axis = observation[4].split('-')[1]
        x = step.partition("-")[0]
        y = step.partition("-")[2]
        if int(x) > int(x_axis):
            action = 3
        elif int(x) < int(x_axis):
            action = 2
        elif int(y) > int(y_axis):
            action = 0
        elif int(y) < int(y_axis):
            action = 1

        # --------------------------------------------
        # end of simzim code
        # --------------------------------------------
        observation, reward, done, info = env.step(action)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print("Reward - " + reward)
            break

env.close()
