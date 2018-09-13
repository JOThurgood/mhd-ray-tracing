print('''Testing for wkb_fast_zerobeta solutions at a 3dnukk.
      This test script intends that you enter Dipole3dCase1
      when prompted. Entering other valid classes will give 
      nonsense results in this context''')

import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import math
from magnetic_field import Dipole3dCase1 as magnetic_field

# Some testing stuff 

x0 = 0.0
y0 = -0.05 
z0 = 0.0
b0 = magnetic_field(x0,y0,z0)
r0 = 2.0 * math.pi / b0.abs
test = wkb.Ray(x0,y0,z0,0.0, 0.0, r0)
ns = 200000 # this is a sampling number rather than number of steps in int
         # itcan give the illusion of h0 being huge, but this is just
         # because the poitns for plotting are not closely spaced near t0
s_end = 2.0
test.solve(s_end,ns)

plt.plot(test.y,test.z)
plt.xlabel('y')
plt.ylabel('z')
plt.axis([-2,2,0,3])
plt.show()

print(len(test.t))

#plt.show()
#
#3D 
#fig = plt.figure()
#ax= fig.gca(projection='3d')
#ax = plt.plot(test.x,test.y,test.z)
#plt.show()

