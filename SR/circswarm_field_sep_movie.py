# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Double2dNullSeparator\'')
f.close()
# Path relative to main directory
import sys
sys.path.append('../')
# Import
import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import math
from magnetic_field import Double2dNullSeparator as magnetic_field
import numpy as np
# Remove the f
import os
os.remove('tmp_config.py')


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

#plt.rcParams['contour.negative_linestyle'] = 'solid'
#plt.contour(gx,gy,az,25,colors='blue')
#plt.contour(gx,gy,az,levels=[0],colors='red')

# solve the rays iteratively
x0 = -1.
y0 = 0.
z0 = 0.
d = 0.1 # radius
nrays =40
dphi_dr = -1.0
t_end = 23.0
s_end = t_end / 2.0 / math.pi  
ns = 100

swarm1 = wkb.Swarm.init_circle_zplane(x0,y0,z0,d,nrays,dphi_dr)
swarm1.solve(s_end,ns)

#for myray in swarm1.rays:
#    plt.plot(myray.x,myray.y,'black')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.axis([-2,2, -2,2])
#plt.show()



print('ODE solve for swarm done. Now making the figures at the sampling times')

outdir = 'frames/'
if not os.path.exists(outdir):
    os.mkdir(outdir)

for i in range(0,ns-1):
    plt.contour(gx,gy,az,levels=[0],colors='red')
    for myray in swarm1.rays:
        plt.plot(myray.x[i],myray.y[i],'k+') # ko is ok too
        if i > 4:
            plt.plot(myray.x[i-3:i],myray.y[i-3:i],'k')
    title = '{:0.2f}'.format(swarm1.rays[1].t[i])
    title = 't = '+title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.axis([-2,2,-2,2])
    filename = '{:04d}'.format(i)
    filename = outdir+'/'+filename+'.png'
    plt.savefig(filename,dpi=300)
    msg = 'saved image '+filename    
    print(msg)
    plt.clf()
