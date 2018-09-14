# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Linear2dNull\'')
f.close()
# Import
import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import math
# Remove the f
import os
os.remove('tmp_config.py')


# Some testing stuff 

test = wkb.Ray(0.0, 1.0, 0.0, 1.0, 0.0, 0.0)
ns = 1000
s_end = 3.*math.pi/2.  
test.solve(s_end,ns)

plt.plot(test.x,test.y)
plt.show()
#plt.show()
#
#3D 
#fig = plt.figure()
#ax= fig.gca(projection='3d')
#ax = plt.plot(test.x,test.y,test.z)
#plt.show()

