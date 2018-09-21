# A helper class so that df_ds can be switched to a 
# different field without modifying the code eleswhere


# Linear 2D magnetic null point B=[y,x,0]
class Linear2dNull:

    def __init__(self, x, y, z):
        self.x = y  
        self.y = x   
        self.z = 0.0
        self.x_dx = 0.0
        self.x_dy = 1.0
        self.x_dz = 0.0
        self.y_dx = 1.0
        self.y_dy = 0.0
        self.y_dz = 0.0
        self.z_dx = 0.0
        self.z_dy = 0.0
        self.z_dz = 0.0
        self.az = 0.5 * (y**2 - x**2)
        self.abs = (self.x**2 + self.y**2 + self.z**2)**(0.5)

# The field described in McLaughlin, Thurgood, Botha & Wiggs 
# (2018, in prep)
class Dipole3dCase1:

    def __init__(self, x, y, z):
        a = 1. 
        b = 1.
        d = -0.2
        self.a  = a
        self.b = b 
        self.d = d
        z = z -d # translation if you want to 'bury' at this stage. 
        # can arbitaril;y do it later
        denom = ( x**2 + y**2 + z**2 )**(5./2.)
        self.x = - a * (3.0 * x * z)  / denom
        self.y = - a * (3.0 * y * z)  / denom
        self.z = a * ( x**2 + y**2 - 2.0 * z**2 ) / denom + b
        self.abs = (self.x**2 + self.y**2 + self.z**2)**(0.5)
        denom = ( x**2 + y**2 + z**2 )**(7./2.)
        self.x_dx = 3.*a*z * (5.*x**2 - (x**2 + y**2 + z**2)) / denom
        self.x_dy = 15.*a*x*y*z / denom
        self.x_dz = 3.*a*x * (5.*z**2 - (x**2 + y**2 + z**2)) / denom
        self.y_dx = self.x_dy
        self.y_dy = 3.*a*z * (5.*y**2 - (x**2 + y**2 + z**2)) / denom
        # self.y_dz = self.x_dz / x * y # easily gives /0
        self.y_dz = 3.*a*y * (5.*z**2 - (x**2 + y**2 + z**2)) / denom
        self.z_dx = 3.*a*x * (4.*z**2 - x**2 - y**2) / denom
        # self.z_dy = self.z_dx / x * y
        self.z_dy = 3.*a*y * (4.*z**2 - x**2 - y**2) / denom
        self.z_dz = 3.*a*z * (2.*z**2 -3.*x**2 - 3.*y**2) / denom
        #flux function
        denom = ( x**2 + y**2 + z**2 )**(3./2.)
        #self.ax = a * y / denom - b * y/2.
        self.ax = a * y / denom - b * y/2.
        self.ay = - a * x / denom + b * x / 2.  
        self.az = 0.0


# 2 potential nulls linked with a separtor 
class Double2dNullSeparator:

    def __init__(self, x, y, z):
        B0 = 1.0
        a  = 1.0
        self.x = B0 / a**2 * (x**2 - y**2 - a**2)  
        self.y = B0 / a**2 * (-2.0 * x * y)
        self.z = 0.0
        self.x_dx = 2.0 * B0 / a**2 * x
        self.x_dy = -2.0 * B0 / a**2 * y
        self.x_dz = 0.0
        self.y_dx = B0 / a**2 * (-2.0 * y )
        self.y_dy = B0 / a**2 * (-2.0 * x )
        self.y_dz = 0.0
        self.z_dx = 0.0
        self.z_dy = 0.0
        self.z_dz = 0.0
        self.az = B0 / a**2 * ( x**2*y -y**3/3. -a**2 * y )
