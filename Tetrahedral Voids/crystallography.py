from manimlib import * 

class CubicLattice(VGroup):
    """ Creates a Cubic Lattice object using side_length value """
    def __init__(self,side_length=2.0,**kwargs):
        super().__init__(**kwargs)
        a = side_length/2
        rg = [a,-a]
        self.corners = np.array([[x,y,z] for x in rg for y in rg for z in rg])
        """
        For rg = [1,-1]
        self.corners = array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], 
                             [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]])
        """
        self.body_center = ORIGIN
        self.face_centers = np.concatenate((a*np.identity(3),a*-1*np.identity(3)))
        face = Square(side_length)
        self.add(*self.square_to_cube_faces(face))
    
    @staticmethod
    def square_to_cube_faces(square):
        """ Generate Faces of the cube """
        radius = square.get_height() / 2
        square.move_to(radius * OUT)
        result = [square]
        result.extend([
            square.copy().rotate(PI / 2, axis=vect, about_point=ORIGIN)
            for vect in compass_directions(4)
        ])
        result.append(square.copy().rotate(PI, RIGHT, about_point=ORIGIN))
        return result

class Tetrahedron(VGroup):
    """ Creates a Tetrahedron object using 4 vertices """
    def __init__(self,*vertices,**kwargs):
        super().__init__(**kwargs)
        self.vertices = vertices
        v = np.array(vertices)
        zenith = v[3]
        bplc = sum(v[:3])/3 # Base Plane Centroid
        self.void = ((3*bplc+zenith)/4).tolist()
        plane1 = Polygon(vertices[0],vertices[1],vertices[2])
        plane2 = Polygon(vertices[0],vertices[1],vertices[3])
        plane3 = Polygon(vertices[1],vertices[2],vertices[3])
        plane4 = Polygon(vertices[2],vertices[0],vertices[3])
        self.add(plane1,plane2,plane3,plane4)