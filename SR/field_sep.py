# Path relative to main directory
import sys
sys.path.append('../')
# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Double2dNullSeparator\'')
f.close()
# Import
import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import numpy as np
import math
# Remove the f
import os
os.remove('tmp_config.py')
from magnetic_field import Double2dNullSeparator as magnetic_field

# Plot fieldlines as contours of the flux functon
x0 = -2.01
x1 = 2.01
y0 = x0 
y1 = x1
nx = 200
ny = nx
gx = np.linspace(x0,x1,nx)
gy = np.linspace(y0,y1,ny)

az = np.zeros([nx,ny])

for iy in range(0,ny-1):
    for ix in range(0,nx-1):
        b = magnetic_field(gx[ix],gy[iy], 0.0)
        az[iy,ix] = b.az 

plt.rcParams['contour.negative_linestyle'] = 'solid'
plt.contour(gx,gy,az,25,colors='black')
plt.contour(gx,gy,az,levels=[0],colors='red')


plt.xlabel('x')
plt.ylabel('y')
plt.axis([-2,2, -2,2])
plt.show()
#plt.savefig('fig1.png',dpi=300)

