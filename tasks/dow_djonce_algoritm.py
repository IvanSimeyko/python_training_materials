import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#%matplotlib inline

# creating two massive
x = np.array([15.82, 16.72, 15.78, 16.42])
y = np.array([16.71, 16.71, 15.64, 15.97])
print x, y

# plotting massive
# plt.plot(x, 'r', label='x')
# plt.plot(y, 'g', label='y')
# plt.legend()
#plt.show()

#making a 2d matrix to compute distances between all pairs of x and y
distances = np.zeros((len(y), len(x)))
print distances

#use euclidean distance between the pairs of points.
for i in range(len(y)):
    for j in range(len(x)):
        distances[i, j] = (x[j]-y[i])**2

print distances


#write a small function to visualize the distance matrix we just created.
def distance_cost_plot(distances):
    im = plt.imshow(distances, interpolation='nearest', cmap='Reds')
    plt.gca().invert_yaxis()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.colorbar()

plt.show(distance_cost_plot(distances))