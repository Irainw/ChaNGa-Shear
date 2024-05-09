import pynbody
import numpy as np


sim = pynbody.snapshot.new(dm = 1)

sim.dm['pos']  = [[0,0,0]]
sim.dm['vel'] = [[0,0,0]]

sim.dm['mass'] = 1.0

sim.write(filename='initialconditions.tipsy', fmt = pynbody.tipsy.TipsySnap)

print('Done')
