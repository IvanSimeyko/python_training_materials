# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#create variables
x, y = [0, 0], [0, 0]

#reading data from user
name_one = raw_input('Введите название первой организации (например AA): ')
name_two = raw_input('Введите название второй организации (например AXP): ')

#reading file with data
lines = (line.strip().split(',') for line in open('dow_jones_index.data'))
for line in lines:
    if line[1] == name_one:
        x[0] += float(line[3][1:])
        x[1] += float(line[6][1:])
    if line[1] == name_two:
        y[0] += float(line[3][1:])
        y[1] += float(line[6][1:])

# creating two massive
x = np.array(x)
y = np.array(y)

# plotting massive
# plt.plot(x, 'r', label='x')
# plt.plot(y, 'g', label='y')
# plt.legend()
#plt.show()

#making a 2d matrix to compute distances between all pairs of x and y
distances = np.zeros((len(y), len(x)))

#use euclidean distance between the pairs of points.
for i in range(len(y)):
    for j in range(len(x)):
        distances[i, j] = (x[j]-y[i])**2
print distances


#function to visualize the distance matrix we just created.
def distance_cost_plot(distances):
    im = plt.imshow(distances, interpolation='nearest', cmap='Reds')
    plt.gca().invert_yaxis()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.colorbar()

plt.show(distance_cost_plot(distances))