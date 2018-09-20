# Path relative to main directory
import sys
sys.path.append('../')
# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Linear2dNull\'')
f.close()
# Import
import matplotlib.pyplot as plt
import fieldlines as fl
import numpy as np
import math
# Remove the f
import os
os.remove('tmp_config.py')
from magnetic_field import Linear2dNull as magnetic_field

# Some seping stuff 
delta = 1e-3
x0 = delta * 2.0**0.5
y0 = x0
z0 = 0.
sep = fl.FieldLine(x0,y0,z0)
ns = 100 
s_end = 2.0**0.5
sep.solve(s_end,ns)
plt.plot(sep.x,sep.y,'b')

x0 = -x0
y0 = -y0 
sep = fl.FieldLine(x0,y0,z0)
sep.solve(s_end,ns)
plt.plot(sep.x,sep.y,'b')

y0 = -y0 
sep = fl.FieldLine(x0,y0,z0)
s_end = - s_end
sep.solve(s_end,ns)
plt.plot(sep.x,sep.y,'b')

x0 = -x0
y0 = -y0
sep = fl.FieldLine(x0,y0,z0)
sep.solve(s_end,ns)
plt.plot(sep.x,sep.y,'b')

x0 = -0.75
y0 = 1.0
s_end = 2.0
test = fl.FieldLine(x0,y0,z0)
test.solve(s_end,ns)
plt.plot(test.x,test.y,'k--') 

plt.xlabel('x')
plt.ylabel('y')
plt.axis([-1,1,-1,1])
#plt.savefig('sep.png')
plt.show()

