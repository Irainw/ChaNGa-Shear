import os
import pynbody
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from astropy import units as u
from astropy import constants as const
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

#matplotlib.use('Agg')

#path = ('./pargrav.000100')
#s = pynbody.load(path)

def loadFiles(path):
	positions = []
	velocities = []
	numFiles = len(os.listdir(path))
	
	filesLoaded = 0
	for i in range(1, numFiles + 1):
		name = 'pargrav.{:06d}'.format(i)
		filePath = os.path.join(path, name)
		#print(f'Latest file is {filePath}')
		filesLoaded += 1
		#print(f'Loading file: {filePath}')
		s = pynbody.load(filePath)
		position = s['pos']
		velocity = s['vel']
		positions.append(position)
		velocities.append(velocity)
#		if os.path.isfile(path):
			#print(f'Loading file: {filePath}')
			#s = pynbody.load(filePath)
			#position = s['pos']
			#data.append(position)
	print(f'Total files loaded {filesLoaded}')
	print(f'Array lengths: {len(positions)}, {len(velocities)}')
	return np.array(positions), np.array(velocities)
	
pargravFolder = './pargravs'
positions, velocity = loadFiles(pargravFolder)

def updateFrame(frame):
	ax1.cla()
	ax2.cla()
	
	
	ax1.scatter(positions[frame][:,0], positions[frame][:,1],positions[frame][:,2], c='b', marker = 'o')
	ax1.set_title('Frame {}'.format(frame))
	ax1.set_xlabel('X')
	ax1.set_ylabel('Y')
	ax1.set_zlabel('Z')
	ax1.view_init(elev=90, azim = 0)
	
	ax2.plot(positions[frame][:,0], velocity[frame][:,1], 'g.')
	ax2.set_title('X position vs Y Velocity')
	ax2.set_xlabel('X Position')
	ax2.set_ylabel('Y Velocity')
	
fig = plt.figure(figsize = (12, 12))
ax1 = fig.add_subplot(121, projection = '3d')
ax2 = fig.add_subplot(122)


animation = FuncAnimation(fig, updateFrame, frames = range(100), interval = 250)

mywriter = matplotlib.animation.PillowWriter(fps=24,metadata=dict(artist='Ian RW'), bitrate = 1800)
animation.save('100step2Plot.gif', writer = mywriter)

#Next Make a plot of the y velocity vs the x coordinates

plt.show()
