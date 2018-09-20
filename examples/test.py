# Path relative to main directory
import sys
sys.path.append('../')
# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Dipole3dCase1\'')
f.close()
# Import
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import fieldlines as fl
import numpy as np
import math
# Remove the f
import os
os.remove('tmp_config.py')
from magnetic_field import Dipole3dCase1 as magnetic_field



# The spine 
delta = 2.0
x0 = 0.0
y0 = 0.0
z0 = 1.05992 + delta
spine = fl.FieldLine(x0,y0,z0)
ns = 100 
s_end = -3
spine.solve(s_end,ns)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(spine.x,spine.y,spine.z,'red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(0,3)

z0 = 0.
spine = fl.FieldLine(x0,y0,z0)
ns = 100 
s_end = -1
spine.solve(s_end,ns)
ax.plot(spine.x,spine.y,spine.z,'red')

#
plt.show()



