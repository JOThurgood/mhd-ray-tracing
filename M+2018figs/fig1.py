# Path relative to main directory
import sys
sys.path.append('../')
# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Dipole3dCase1\'')
f.close()
# Import
import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import numpy as np
import math
# Remove the f
import os
os.remove('tmp_config.py')
from magnetic_field import Dipole3dCase1 as magnetic_field

# Plot fieldlines as contours of the flux functon
y0 = -2.01
y1 = 2.01
z0 = 0.
z1 = 3.01
ny = 4*100
nz = ny
gy = np.linspace(y0,y1,ny)
gz = np.linspace(z0,z1,nz)

ax = np.zeros([ny,nz])

for iz in range(0,nz-1):
    for iy in range(0,ny-1):
        b = magnetic_field(0.0,gy[iy], gz[iz])
        ax[iz,iy] = b.ax 

plt.rcParams['contour.negative_linestyle'] = 'solid'
plt.contour(gy,gz,ax,100,colors='black')
plt.contour(gy,gz,ax,levels=[0],colors='red')


plt.xlabel('y')
plt.ylabel('z')
plt.axis([-2,2, 0,3])
plt.arrow(-0.30,1.02,1e-1,0.2*1e-1,width=3e-2, color='red',
          edgecolor=None,zorder=1e6)
plt.arrow(0.30,1.02,-1e-1,0.2*1e-1,width=3e-2, color='red',
          edgecolor=None,zorder=1e6)
plt.arrow(0.0,1.1,0.,1e-1,width=3e-2, color='red',
          edgecolor=None,zorder=1e6)
plt.arrow(0.0,1.0  ,0.,-1e-1,width=3e-2, color='red',
          edgecolor=None,zorder=1e6)
plt.savefig('fig1.png',dpi=300)
#plt.show()

