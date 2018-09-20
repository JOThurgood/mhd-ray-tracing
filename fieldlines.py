import numpy as np
import math
from scipy.integrate import odeint, solve_ivp
# This next block handles usr choice of magnetic_field clss
import importlib  
import tmp_config as config
module = importlib.import_module('magnetic_field')
className = None 
while className is None: 
    try:
        className = config.fieldclass
        magnetic_field = getattr(module, className)
    except AttributeError:
        print('''Error: tmp_config.py (passing fieldclass) missing
        (See Readme)
        ''')
        exit()
import time

def df_ds(f, s):
    x = f[0]
    y = f[1]
    z = f[2]
    b = magnetic_field(x,y,z)
    absb = (b.x**2 + b.y**2 + b.z**2)**0.5
    dx = b.x / absb
    dy = b.y / absb
    dz = b.z / absb
    df = (dx, dy, dz)
    return df 


class FieldLine:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._set_f0()

    def _set_f0(self):   
        f = (self.x, self.y, self.z)
        self.f0 = f
        return f

    def solve(self, s_end, ns):  # RK45 solve
        s = np.linspace(0, s_end, ns) 
        f = odeint(df_ds, self.f0, s)
        self.x = f[:, 0]
        self.y = f[:, 1]
        self.z = f[:, 2]
