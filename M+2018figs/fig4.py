# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Dipole3dCase1\'')
f.close()
# Path relative to main directory
import sys
sys.path.append('../')
# Import
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import wkb_fast_zerobeta as wkb
import math
from magnetic_field import Dipole3dCase1 as magnetic_field
# Remove the tmp file
import os
os.remove('tmp_config.py')

ns = 1000 # sampling number for solution (does not effect dh directly)

x0 = 0
x1 = 0
y0 = -2 
y1 = -0.3
z0=z1=0

nrays = 18
p = 0
q = 0
#b0 = magnetic_field(x0,y0,z0)
r = 2.0 * math.pi# / b0.abs

swarm1 = wkb.Swarm.init_line_linspace(x0,x1,y0,y1,z0,z1,p,q,r,nrays)

s_end = 3.0 / 2.0 / math.pi
swarm1.solve(s_end,ns)
for myray in swarm1.rays:
    plt.plot(myray.y,myray.z,'k')

y0 = -0.3+0.01
y1 = -0.1
nrays = 20

s_end = 5.0 / 2.0 / math.pi

swarm2 = wkb.Swarm.init_line_linspace(x0,x1,y0,y1,z0,z1,p,q,r,nrays)
swarm2.solve(s_end,ns)

for myray in swarm2.rays:
    plt.plot(myray.y,myray.z,'k')

s_end = 3.0 / 2.0 / math.pi
ns = ns * 10

y0 = -0.09 
yellowray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
yellowray.solve(s_end,ns)

plt.plot(yellowray.y,yellowray.z,'y')


y0 = -0.08
blueray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
blueray.solve(s_end,ns)

plt.plot(blueray.y,blueray.z,'b')

y0 = -0.07
orangeray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
orangeray.solve(s_end,ns)

plt.plot(orangeray.y,orangeray.z,color='orange')

y0 = -0.06
redray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
ns = ns * 5 
redray.solve(s_end,ns)

plt.plot(redray.y,redray.z,color='red')

ns = 1000  
s_end = 0.5 / 2.0 / math.pi
y0 = -0.05
greenray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
greenray.solve(s_end,ns)

plt.plot(greenray.y,greenray.z,color='green')
plt.xlabel('y')
plt.ylabel('z')
plt.axis([-2,2,0,3])

plt.savefig('fig4.png',dpi=300)
