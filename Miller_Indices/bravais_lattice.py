from manim import *

class GenLattice(Polyhedron):
    def __init__(self,a: float,b: float,c: float,alpha: float,beta: float,gamma: float,**kwargs):
        self.a, self.b, self.c = a, b, c
        self.cos_a, self.cos_b, self.cos_g = np.cos(alpha), np.cos(beta), np.cos(gamma)
        self.sin_a, self.sin_b, self.sin_g = np.sin(alpha), np.sin(beta), np.sin(gamma) 
        self.i,self.j,self.k = self.get_unit_vectors()
        vertices_coords = [np.array([0.0,0.0,0.0]), self.i, self.j, self.k, 
                           self.i+self.j, self.j+self.k, self.k+self.i, 
                           self.i+self.j+self.k]
        face_list = [[0,1,6,3], [0,1,4,2], [0,2,5,3], [2,4,7,5], [3,6,7,5], [1,4,7,6]]
        Polyhedron.__init__(self, vertices_coords, face_list, **kwargs)
    
    def get_unit_vectors(self):
        t = 1+(2*self.cos_a*self.cos_b*self.cos_g)-(self.cos_a*self.cos_a)-(self.cos_b*self.cos_b)-(self.cos_g*self.cos_g)
        sigma_xy = np.sqrt(t) 
        x = self.a*np.array([1.0,0.0,0.0])
        y = self.b*np.array([self.cos_g,self.sin_g,0.0])
        y[np.isclose(y,0.0)] = 0.0
        z = self.c*np.array([self.cos_b,(self.cos_a-(self.cos_b*self.cos_g))/self.sin_g,sigma_xy/self.sin_g])
        z[np.isclose(z,0.0)] = 0.0
        return x,y,z
    
    def new_axes(self):
        org = Dot3D(color=RED)
        end_x = 1.35*self.i
        end_y = 1.35*self.j
        end_z = 1.35*self.k
        x = Arrow3D(start=self.i,end=end_x,base_radius=0.1)
        y = Arrow3D(start=self.j,end=end_y,base_radius=0.1)
        z = Arrow3D(start=self.k,end=end_z,base_radius=0.1)
        x_label = MathTex("x")
        y_label = MathTex("y")
        z_label = MathTex("z")
        x_label.rotate(PI)
        x_label.move_to(0.3*OUT+end_x)
        x_label.rotate(PI/2, axis=X_AXIS)
        y_label.rotate(PI/2)
        y_label.move_to(0.3*OUT+end_y)
        y_label.rotate(PI/2, axis=Y_AXIS)
        z_label.rotate(PI/2, axis=X_AXIS)
        z_label.rotate(125*DEGREES)
        z_label.move_to(0.4*RIGHT+end_z+0.4*IN)
        new_axes = VGroup(x,y,z,x_label,y_label,z_label,org)
        return new_axes

    def draw_dir(self, u:float, v:float, w:float):
        mx = max(abs(u),abs(v),abs(w))
        u,v,w = u/mx, v/mx, w/mx
        ui,vj,wk = u*self.i, v*self.j, w*self.k
        start_point = ORIGIN
        if u < 0.0:
            start_point = start_point + self.i
        if v < 0.0:
            start_point = start_point + self.j
        if w < 0.0:
            start_point = start_point + self.k
        end_point = start_point + (ui+vj+wk)    
        vect = Arrow3D(start=start_point,end=end_point, base_radius=0.1)
        return vect
    
    def get_proj(self, u:float, v:float, w:float):
        mx = max(abs(u),abs(v),abs(w))
        u,v,w = u/mx, v/mx, w/mx
        ui,vj,wk = u*self.i, v*self.j, w*self.k
        start_point = ORIGIN
        if u < 0.0:
            start_point = start_point + self.i
        if v < 0.0:
            start_point = start_point + self.j
        if w < 0.0:
            start_point = start_point + self.k
        end_point = start_point + (ui+vj+wk)
        x_start = start_point*RIGHT
        x_end = end_point*RIGHT
        y_start = start_point*UP
        y_end = end_point*UP
        z_start = start_point*OUT
        z_end = end_point*OUT
        xy_start = start_point*(RIGHT+UP)
        xy_end = end_point*(RIGHT+UP)
        proj_x = Arrow3D(start=x_start, end=x_end, base_radius=0.1)
        proj_y = Arrow3D(start=y_start, end=y_end, base_radius=0.1)
        proj_z = Arrow3D(start=z_start, end=z_end, base_radius=0.1)
        proj_xy_plane = Arrow3D(start=xy_start, end=xy_end, base_radius=0.1)
    
        return proj_x,proj_y,proj_z,proj_xy_plane 
        
    def draw_plane(self, h:float, k:float, l:float):
        pass