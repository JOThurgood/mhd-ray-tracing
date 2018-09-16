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
p = 1.0
q = 0.1
test = wkb.Ray(0.0, 1.0, 0.0, p, q, 0.0)
ns = 1000 
t_end = 300  
s_end = t_end / 2.0 / math.pi  
test.solve(s_end,ns)

plt.plot(test.x,test.y)
plt.xlabel('y')
plt.ylabel('z')
plt.axis([-1,1,-1,1])
plt.savefig('test.png')
plt.show()

