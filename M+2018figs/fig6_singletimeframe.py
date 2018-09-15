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
# Remove the f
import os
os.remove('tmp_config.py')

t_end = 1.00 
s_end = t_end / 2.0 / math.pi
ns = 2 # sampling number for solution (does not effect dh directly)

x0 = 0
x1 = 0
y0 = -3 
y1 = 0#-0.025  
z0=z1=0

nrays = 300  
p = 0
q = 0
#b0 = magnetic_field(x0,y0,z0)
r = - 2.0 * math.pi #/ b0.abs

swarm1 = wkb.Swarm.init_line_linspace(x0,x1,y0,y1,z0,z1,p,q,r,nrays)


swarm1.solve(s_end,ns)


for myray in swarm1.rays:
    i = len(myray.t)-1    
    #print(myray.t[i])
    plt.plot(myray.y[i],myray.z[i],'k+')

title = '{:0.2f}'.format(t_end)
title = 't = '+title
plt.xlabel('y')
plt.ylabel('z')
plt.title(title)
plt.axis([-3,3,0,3])
plt.savefig('fig6.png',dpi=300)

