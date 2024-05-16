import pynbody
import numpy as np
import pynbody.units as u
import matplotlib.pyplot as plt

s = pynbody.load('./glass16.std')

originalVel = s['vel'].copy()

positions = s['pos']
radii = np.sqrt(positions[:,0]**2 + positions[:,1]**2 + positions[:,2]**2)
angMomentum = np.cross(positions, s['vel'])
print(angMomentum)

h = np.linalg.norm(angMomentum)
print(h)
omega = h/(radii**2)
print(omega[0])
velocity = s['vel']
velocity[:,1] = -2 * (1 * (1/u.s)) * positions[:,0]

plt.figure(figsize = (12,6))
plt.subplot(1,2,1)
plt.scatter(positions[:,0], originalVel[:,1], s=1, alpha = 0.5)
plt.xlabel('X Position')
plt.ylabel('Y Velocities (Original)')
plt.title('Original Y Velocities')

plt.subplot(1,2,2)
plt.scatter(positions[:,0], velocity[:,1], s =1, alpha = 0.5)
plt.xlabel('X Position')
plt.ylabel('Y Velocities (Modified)')
plt.title('Modified Y Velocities')

plt.tight_layout()
plt.show()
