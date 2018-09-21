# Path relative to main directory
import sys
sys.path.append('../')
# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Linear2dNull\'')
f.close()
# Import
import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import numpy as np
import math
# Remove the f
import os
os.remove('tmp_config.py')
from magnetic_field import Linear2dNull as magnetic_field

# Plot fieldlines as contours of the flux functon
nx = 512
ny = 512
gx = np.linspace(-1.0,1.0,nx)
gy = np.linspace(-1.0,1.0,ny)

az = np.zeros([nx,ny])

for iy in range(0,ny-1):
    for ix in range(0,nx-1):
        b = magnetic_field(gx[ix],gy[iy],0.0)
        az[ix,iy] = b.az

plt.contour(gx,gy,az,4,colors='black')

# Some testing stuff 
x0 = 0.
y0 = 0.
z0 = 0.
d = 0.5 # radius
nrays =40
dphi_dr = 1.0
t_end = 2. 
s_end = t_end / 2.0 / math.pi  
ns = 100

swarm1 = wkb.Swarm.init_circle_zplane(x0,y0,z0,d,nrays,dphi_dr)
swarm2 = wkb.Swarm.init_circle_zplane(x0,y0,z0,d,nrays,dphi_dr)

for myray in swarm1.rays:
    plt.plot(myray.x,myray.y,'ro')

swarm1.solve(s_end,ns)
for myray in swarm1.rays:
    plt.plot(myray.x,myray.y,'g')

swarm2 = wkb.Swarm.init_circle_zplane(x0,y0,z0,d,nrays,-dphi_dr)
swarm2.solve(s_end,ns)
for myray in swarm2.rays:
    plt.plot(myray.x,myray.y,'b')


plt.xlabel('x')
plt.ylabel('y')
plt.axis([-1,1,-1,1])
#plt.savefig('test.png')
plt.show()

