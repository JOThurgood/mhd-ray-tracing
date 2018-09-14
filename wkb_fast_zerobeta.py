import numpy as np
import math
from scipy.integrate import odeint

# This next block handles usr choice of magnetic_field clss
import importlib  
module = importlib.import_module('magnetic_field')
className = None 
while className is None: 
    try:
        className = input('enter Class name for your magnetic field:')
        my_class = getattr(module, className)
    except AttributeError:
        print('''Error: 
        Enter the name of one of the magnetic field classes defined
        in magnetic_field.py. If you are running this from one of the
        pre-defined tests, it should correspond to the intended
        field

        ''')
        className = None


magnetic_field = my_class


def df_ds(f, s):
    # Helper variables
    t = f[0]
    omega = 2.0 * math.pi  # hardcoded as const
    phi = 0.0   # could generalise later... 
    x = f[1]
    y = f[2]
    z = f[3]
    p = f[4]
    q = f[5]
    r = f[6] 
    k2 = p**2 + q**2 + r**2
    b = magnetic_field(x, y, z) 
    b2 = b.x**2 + b.y**2 + b.z**2
    # Derivatives with respect to s
    dt = -omega #James' code had -2pi**2? 
    dx = p * b2
    dy = q * b2
    dz = r * b2 
    dp = -k2 * (b.x*b.x_dx + b.y*b.y_dx + b.z*b.z_dx)  
    dq = -k2 * (b.x*b.x_dy + b.y*b.y_dy + b.z*b.z_dy)  
    dr = -k2 * (b.x*b.x_dz + b.y*b.y_dz + b.z*b.z_dz)  
    # dphi = 0.0 # hardcoded as const
    # domega = 0.0  
    # Collect result as tuple in appropriate order
    df = (dt, dx, dy, dz, dp, dq, dr)
    return df 


class Ray:

    def __init__(self, x, y, z, p, q, r):
        self.t = 0.0
        self.omega = -2.0 * math.pi 
        self.phi = 0.0 
        self.x = x
        self.y = y
        self.z = z
        self.p = p
        self.q = q
        self.r = r
        self._set_f0()

    def _set_f0(self):   
        f = (self.t, self.x, self.y, self.z, self.p, self.q, self.r)
        self.f0 = f
        return f

    def solve(self, s_end, ns):  # RK45 solve
        s = np.linspace(0, s_end, ns) 
        f = odeint(df_ds, self.f0, s,h0=1e-3)
        # self.f = f  
        self.t = f[:, 0]
        self.x = f[:, 1]
        self.y = f[:, 2]
        self.z = f[:, 3]
        self.p = f[:, 4]
        self.q = f[:, 5]
        self.r = f[:, 6]

class Swarm:  # Essentially a list of Rays plus associated functions

    # Constructor takes a *list* of *tuples* for xyzpqr for each ray
    def __init__(self,coordlist):
        self.nrays = len(coordlist)
        self.rays = []
        for index in coordlist:
            x = index[0]
            y = index[1]
            z = index[2]
            p = index[3]
            q = index[4]
            r = index[5]
            self.rays.append(Ray(x,y,z,p,q,r))

    # Initialise rays at evenly spaced points along a line with same
    # p0,q0,r0 
    @classmethod
    def init_line_linspace(cls,x0,x1,y0,y1,z0,z1,p,q,r,nrays):
        #use d as 'radius' since r is grad_x k and reserved
        l = ((x1-x0)**2 + (y1-y0)**2 + (z1-z0)**2)**(0.5) # length
        d = np.linspace(0,l,nrays)
        theta = math.acos((z1-z0)/l)
        phi = math.atan2((y1-y0),(x1-x0))
        coordlist =[]
        for dp in d:
            x = x0 + dp * math.sin(theta) * math.cos(phi)
            y = y0 + dp * math.sin(theta) * math.sin(phi)
            z = z0 + dp * math.cos(theta)
            print(dp,x,y,z)
            element = (x,y,z,p,q,r)
            coordlist.append(element)
        return cls(coordlist)

    def solve(self,s_end,ns):
        for myray in self.rays:
            myray.solve(s_end,ns)
