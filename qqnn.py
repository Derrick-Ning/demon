
import math
import numpy as np
import matplotlib.pyplot as plt
from itertools import count
from mpl_toolkits.mplot3d import Axes3D

x_track = np.zeros((1,3))
x_track_s = np.array([.0,.0,.0])
theta = 0
def gen_path():
    global x_track_s,x_track,theta
    theta += 2*np.pi/90
    x = 300*np.tan(theta)
    y = 0.1*np.tan(theta)
    x_track_s += [x,y,0.1]
    x_track = np.append(x_track,[x_track_s],axis=0)
    return x_track

ax = plt.axes(projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('3d_mobile_obs')

plt.grid(True)
plt.ion()

for t in count():
    if t == 2500:
        break

    ax.plot3D(x_track[:,0],x_track[:,1],x_track[:,2],'blue')
    x_track = gen_path()
    plt.pause(0.01)
