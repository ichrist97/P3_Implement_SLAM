from helpers import display_world, make_data
from robot_class import robot
import numpy as np
import matplotlib.pyplot as plt
import random

world_size         = 100.0    # size of world (square)
measurement_range  = 50.0     # range at which we can sense landmarks
motion_noise       = 2.0      # noise in robot motion
measurement_noise  = 2.0      # noise in the measurements
num_landmarks = 5
N = 20  # time steps
distance = 20.0 # distance robot moves each step

data = make_data(
    N,
    num_landmarks,
    world_size,
    measurement_range,
    motion_noise,
    measurement_noise,
    distance
    )

for index in enumerate(data):
    print(data[step][0])
    print(data[step][1])

# instantiate a robot, r
r = robot(world_size, measurement_range, motion_noise, measurement_noise)

# print out the location of r
print(r)

# define figure size
plt.rcParams["figure.figsize"] = (5,5)

# create any number of landmarks
r.make_landmarks(num_landmarks)
print('Landmark locations [x,y]: ', r.landmarks)

measurements = r.sense()
print(measurements)

# display the world including these landmarks
#display_world(int(world_size), [r.x, r.y], r.landmarks)

# move robo
r.move(1, 2)
print(r)
measurements = r.sense()
print(measurements)
#data.append([measurements, [dx, dy]])
print(data)
#display_world(int(world_size), [r.x, r.y], r.landmarks)

def slam():

    mu = matrix([
        [Px0],
        [Py0],
        [Px1],
        [Py1],
        [Lx0],
        [Ly0],
        [Lx1],
        [Ly1]
    ])
    return mu
