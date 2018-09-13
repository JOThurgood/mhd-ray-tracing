# A helper class so that df_ds can be switched to a 
# different field without modifying the code eleswhere


class Linear2dNull:

    def __init__(self, x, y, z):

        # 2D linear null point
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
