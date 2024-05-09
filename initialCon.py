import os
import pynbody
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from astropy import units as u
from astropy import constants as const
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

path = './glass16.std'
s = pynbody.load(path)

positions = s['pos']
velocity = s['vel']
	
fig = plt.figure(figsize = (12, 12))
ax1 = fig.add_subplot(121, projection = '3d')
ax2 = fig.add_subplot(122)
print(positions)
ax1.scatter(positions[:,0], positions[:,1], positions[:,2], c='b', marker = 'o')
ax1.set_title('Positions')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.view_init(elev=90, azim = 0)

ax2.gca()
ax2.plot(positions[:,0], velocity[:,1], 'g.')
ax2.set_title('X position vs Y Velocity')
ax2.set_xlabel('X Position')
ax2.set_ylabel('Y Velocity')
ax2.set_ylim([-0.001,0.001])

path2 = './pargravs/pargrav.000100'
f = pynbody.load(path2)
print(f.properties['time'])

#plt.show()

#animation.save('initialCondition.gif', writer = mywriter)
