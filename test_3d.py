print('''Testing for wkb_fast_zerobeta solutions at a 3dnull.
      This test script intends that you enter:

          Dipole3dCase1

      when prompted. Entering other valid classes will give 
      nonsense results in this context''')

import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import math
from magnetic_field import Dipole3dCase1 as magnetic_field

## Initialise and plot an individual ray 
#
#x0 = 0.0
#y0 = -0.05 
#z0 = 0.0
#b0 = magnetic_field(x0,y0,z0)
#r0 = 2.0 * math.pi / b0.abs
#test = wkb.Ray(x0,y0,z0,0.0, 0.0, r0)
#ns = 200000 # this is a sampling number rather than number of steps in int
#         # itcan give the illusion of h0 being huge, but this is just
#         # because the poitns for plotting are not closely spaced near t0
#s_end = 2.0
#test.solve(s_end,ns)
#
#plt.plot(test.y,test.z)
#plt.xlabel('y')
#plt.ylabel('z')
#plt.axis([-2,2,0,3])
#plt.draw()
#
#plt.savefig("test3d_fig1.png")
#plt.clf()


# This example reproduces Fig 4 from McLaughlin,Thurgood, Botha + Wiggs
# 2018. It shows how to manipulate groups of rays en masse as "Swarms"
# and individual rays also.

ns = 10000 # sampling number for solution (does not effect dh directly)

x0 = 0
x1 = 0
y0 = -2 
y1 = -0.3
z0=z1=0

nrays = 18
p = 0
q = 0
b0 = magnetic_field(x0,y0,z0)
r = 2.0 * math.pi / b0.abs

swarm1 = wkb.Swarm.init_line_linspace(x0,x1,y0,y1,z0,z1,p,q,r,nrays)

s_end = 1
swarm1.solve(s_end,ns)

for myray in swarm1.rays:
    plt.plot(myray.y,myray.z,'k')


y0 = -0.3+0.01
y1 = -0.1
nrays = 20

swarm2 = wkb.Swarm.init_line_linspace(x0,x1,y0,y1,z0,z1,p,q,r,nrays)
swarm2.solve(s_end,ns)

for myray in swarm2.rays:
    plt.plot(myray.y,myray.z,'k')


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
redray.solve(s_end,ns)

plt.plot(redray.y,redray.z,color='red')

y0 = -0.05
greenray = wkb.Ray(x0,y0,z0,0.0, 0.0, r)
greenray.solve(s_end,ns)

plt.plot(greenray.y,greenray.z,color='green')
plt.xlabel('y')
plt.ylabel('z')
plt.axis([-2,2,0,3])
plt.show()

