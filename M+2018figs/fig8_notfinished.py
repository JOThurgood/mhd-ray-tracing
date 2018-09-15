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
from mpl_toolkits.mplot3d import Axes3D
# Remove the f
import os
os.remove('tmp_config.py')


s_end = 0.5/2.0/math.pi
ns = 2 # sampling number for solution (does not effect dh directly)

x0 = -3
x1 = 3
y0 = -3 
y1 = 3
z = 0  

nx = 100 
ny = 100  
p = 0
q = 0
#b0 = magnetic_field(x0,y0,z0)
r = - 2.0 * math.pi #/ b0.abs

swarm1 = wkb.Swarm.init_zplane(x0,x1,y0,y1,z,nx,ny,p,q,r)

swarm1.solve(s_end,ns)


# # Trisurf
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#X=[]
#Y=[]
#Z=[]
#for myray in swarm1.rays:
#    i = len(myray.t)-1    
#    X.append(myray.x[i])
#    Y.append(myray.y[i])
#    Z.append(myray.z[i])
#
#ax.plot_trisurf(X, Y, Z, linewidth=0.2, antialiased=True)
#plt.show()

# scatter - doesnt look great with many points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for myray in swarm1.rays:
    i = len(myray.t)-1    
    x = myray.x[i]
    y = myray.y[i]
    z = myray.z[i]
    ax.scatter(x , y , z , c='black',s=1)               

ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2,2)
ax.set_zlim3d(0,1)

plt.show()

#
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#
#
#
#for myray in swarm1.rays:
#    i = len(myray.t)-1    
#    #print(myray.t[i])
#    #plt.plot(myray.y[i],myray.z[i],'k+')
#    x = myray.x#[i]
#    y = myray.y#[i]
#    z = myray.z#[i]
#    ax.plot(x, y, z,'k')
#help(ax)
#ax.axis([-2,2,-2,2,0,3])
#ax.legend
#
#plt.show()
#plt.xlabel('y')
#plt.ylabel('z')
#plt.axis([-3,3,0,3])
#plt.savefig('fig6.png',dpi=300)
#
