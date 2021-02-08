import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure(figsize = (10,10))
ax1 = Axes3D(fig)
ax1.plot3D([0,4],[0,4],[0,4],'red')
x_track = np.zeros((1,3))
x_track_s = np.array([.0,.0,.0])
theta = 0
def gen_path():
    global x_track_s,x_track,theta
    theta += 14*np.pi/160
    x = 4*np.sin(theta)
    y = 4*np.cos(theta)
    x_track_s +=[x,y,0.1]
    x_track = np.append(x_track,[x_track_s],axis=0)
    return x_track

def update(i):
    label = 'timestep {0}'.format(i)
    print(label)
    x_track = gen_path()
    ax1.set_xlabel(label)

    ax.plot3D(x_track[:,0], x_track[:,1], x_track[:,2], 'blue')
    return ax1

if __name__ == '__main__':

    anim = FuncAnimation(fig, update, frames=np.arange(0,10), interval=200)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('line.gif',dpi = 80, writer='imagemagick')
    else:
        plt.show()

