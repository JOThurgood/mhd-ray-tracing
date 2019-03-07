# Path relative to main directory
import sys
sys.path.append('../')
# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Double2dNullNoSeparator\'')
f.close()
# Import
import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import numpy as np
import math
# Remove the f
import os
os.remove('tmp_config.py')
from magnetic_field import Double2dNullNoSeparator as magnetic_field

# Plot fieldlines as contours of the flux functon
x0 = -2.5 
x1 = 2.5 
y0 = x0 
y1 = x1
nx = 300
ny = nx
gx = np.linspace(x0,x1,nx)
gy = np.linspace(y0,y1,ny)

az = np.zeros([nx,ny])

for iy in range(0,ny-1):
    for ix in range(0,nx-1):
        b = magnetic_field(gx[ix],gy[iy], 0.0)
        az[iy,ix] = b.az 

plt.rcParams['contour.negative_linestyle'] = 'solid'
plt.contour(gx,gy,az,25,colors='blue')
plt.contour(gx,gy,az,levels=[0],colors='red')

# Solve the swarm
x0 = -1.
y0 = 0.
z0 = 0.
d = 0.1 # radius
nrays =40
dphi_dr = -1.0
t_end = 1.7 
s_end = t_end / 2.0 / math.pi  
ns = 1000

swarm1 = wkb.Swarm.init_circle_zplane(x0,y0,z0,d,nrays,dphi_dr)

#plot the initial points 
#for myray in swarm1.rays:
#    plt.plot(myray.x,myray.y,'ro')

#plot the rays
swarm1.solve(s_end,ns)
for myray in swarm1.rays:
   plt.plot(myray.x,myray.y,'black')



plt.xlabel('x')
plt.ylabel('y')
plt.axis([-2,2, -2,2])
plt.show()
#plt.savefig('fig1.png',dpi=300)
