# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Dipole3dCase1\'')
f.close()
# Path relative to main directory
import sys
sys.path.append('../')
# Import
import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import math
from magnetic_field import Dipole3dCase1 as magnetic_field
import numpy as np
# Remove the f
import os
os.remove('tmp_config.py')

# Calclate the contours of the flux functon
y0 = -2.10
y1 = 2.10
z0 = 0.
z1 = 3.10
ny = 4*25
nz = ny
gy = np.linspace(y0,y1,ny)
gz = np.linspace(z0,z1,nz)

ax = np.zeros([ny,nz])
speed = np.zeros([ny,nz])
for iz in range(0,nz-1):
    for iy in range(0,ny-1):
        b = magnetic_field(0.0,gy[iy], gz[iz])
        ax[iz,iy] = b.ax 
        speed[iz,iy] = b.abs

# solve the rays iteratively

t_end = 4.00 
s_end = t_end / 2.0 / math.pi
ns = 40 + 1
ns = 4000 + 1# sampling number for solution (does not effect dh directly)

x0 = 0
x1 = 0
y0 = -3 
y1 = 0#-0.025  
z0=z1=0

nrays = 300  
p = 0
q = 0
r = -2.0 * math.pi

swarm1 = wkb.Swarm.init_line_linspace(x0,x1,y0,y1,z0,z1,p,q,r,nrays)


swarm1.solve(s_end,ns)
print('ODE solve for swarm done. Now making the figures at the sampling times')

outdir = 'frames_fig6'
if not os.path.exists(outdir):
    os.mkdir(outdir)

for i in range(0,ns-1):
    plt.contour(gy,gz,ax,levels=[0],colors='red')
    for myray in swarm1.rays:
        plt.plot(myray.y[i],myray.z[i],'k+')
#    title = '{:0.2f}'.format(swarm1.rays[1].t[i])
    title = '{:0.3f}'.format(swarm1.rays[1].t[i])
    title = 't = '+title
    plt.xlabel('y')
    plt.ylabel('z')
    plt.title(title)
    plt.axis([-3,3,0,3])
    filename = '{:04d}'.format(i)
    filename = outdir+'/'+filename+'.png'
    plt.savefig(filename,dpi=300)
    msg = 'saved image '+filename    
    print(msg)
    plt.clf()
