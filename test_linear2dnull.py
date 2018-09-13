print('''Testing for wkb_fast_zerobeta solutions at linear 2d null.
      This test script intends that you enter Linear2dNull
      when prompted. Entering other valid classes will give 
      nonsense results in this context''')

import matplotlib.pyplot as plt
import wkb_fast_zerobeta as wkb
import math
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

