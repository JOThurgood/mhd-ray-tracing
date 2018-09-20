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


x0 = 0
x1 = 0
y0 = -2 
y1 = -0.3
z0=z1=0
p = 0
q = 0
r = - 2.0 * math.pi
ns = 1e5  
 
s_end = 3.0 / 2.0 / math.pi


y0 = -0.060 
redray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
redray.solve(s_end,ns)
plt.plot(redray.y,redray.z,'red',label='$y_0$=-0.06')

y0 = -0.062
blueray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
blueray.solve(s_end,ns)
plt.plot(blueray.y,blueray.z,'blue',label='$y_0$=-0.062')

ns = ns * 1e2
delta=-1e-5
#delta=-5e-6
y0 = -0.061-delta
blackray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
blackray.solve(s_end,ns)
plt.plot(blackray.y,blackray.z,'black',label='$y_0$=-0.061')

#plot the null as a cross
plt.plot(0.0,1.05992,'kx')

plt.legend()
plt.xlabel('y')
plt.ylabel('z')
plt.title('(a)')
plt.axis([-2,2,0,3])
#plt.show()
plt.savefig('fig5_a.png',dpi=300)
