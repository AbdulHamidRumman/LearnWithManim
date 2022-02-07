from manimlib.imports import *
import numpy as np 

def fcc_unit_cell(corner_face_cube=None):
    a = 1.41 # side length/2
    # Cube
    cube = Cube(side_length=2*a, fill_opacity=0.1,stroke_width=0.5)
    # Corner Atom Portions
             #      0      1       2       3       4      5       6         7             
    c_u_min = [     0,     0,      0,      0,   PI/2,  PI/2,   PI/2,     PI/2]
    c_u_max = [  PI/2,  PI/2,   PI/2,   PI/2,     PI,    PI,     PI,       PI]
    c_v_min = [     0,  PI/2,     PI, 3*PI/2,      0,  PI/2,     PI,   3*PI/2]
    c_v_max = [  PI/2,    PI, 3*PI/2,   2*PI,   PI/2,    PI, 3*PI/2,     2*PI]
    c_tuple = zip(c_u_min,c_u_max,c_v_min,c_v_max)
    c_part = [ParametricSurface(
      lambda u,v: np.array( 
                       [ np.sin(u)*np.cos(v),              
                         np.sin(u)*np.sin(v),
                         np.cos(u)]), u_min = p_min, u_max = p_max, v_min = q_min, v_max = q_max)
            for p_min,p_max,q_min,q_max in c_tuple]
    corner_atom = VGroup(*c_part)

    angle0 = [0,PI/2,PI,3*PI/2,0,PI/2,PI,3*PI/2]
    sector_xy_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
    sector_yz_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
    sector_zx_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
    sector_xy = VGroup(*sector_xy_array)
    sector_yz = VGroup(*sector_yz_array).rotate(PI/2,axis=UP)
    sector_zx = VGroup(*sector_zx_array).rotate(PI/2,axis=RIGHT)

    corner_atom_portion = [
                        VGroup(corner_atom[0],sector_xy_array[0],sector_yz_array[1],sector_zx_array[0]), # 0
                        VGroup(corner_atom[1],sector_xy_array[1],sector_yz_array[5],sector_zx_array[1]), # 1
                        VGroup(corner_atom[2],sector_xy_array[2],sector_yz_array[2],sector_zx_array[5]), # 2
                        VGroup(corner_atom[3],sector_xy_array[3],sector_yz_array[6],sector_zx_array[4]), # 3
                        VGroup(corner_atom[4],sector_xy_array[4],sector_yz_array[0],sector_zx_array[3]), # 4
                        VGroup(corner_atom[5],sector_xy_array[5],sector_yz_array[4],sector_zx_array[2]), # 5
                        VGroup(corner_atom[6],sector_xy_array[6],sector_yz_array[3],sector_zx_array[6]), # 6
                        VGroup(corner_atom[7],sector_xy_array[7],sector_yz_array[7],sector_zx_array[7])  # 7
                    ]
        
                              #         0                   1                       2                   3   
    corner_atom_portion_pos = [np.array([-a,-a,-a]),  np.array([a,-a,-a]),  np.array([a,a,-a]),  np.array([-a, a,-a]),
                              np.array([-a,-a,a]),   np.array([a,-a,a]),   np.array([a,a,a]),   np.array([-a,a,a])]
                              #         4                   5                       6                   7
    for i in range(8):
        corner_atom_portion[i].shift(corner_atom_portion_pos[i])

    # Face Atom Portions
                  # 0        1       2       3      4       5
    f_u_min = [     0,    PI/2,      0,      0,     0,      0]
    f_u_max = [  PI/2,      PI,     PI,     PI,    PI,     PI]
    f_v_min = [     0,       0,     PI,      0, -PI/2,   PI/2]
    f_v_max = [   TAU,     TAU,    TAU,     PI,  PI/2, 3*PI/2]
    f_tuple = zip(f_u_min,f_u_max,f_v_min,f_v_max)
    f_part = [ParametricSurface(
        lambda u,v : np.array([
            0.98*np.sin(u)*np.cos(v),
            0.98*np.sin(u)*np.sin(v),
            0.98*np.cos(u)
        ]), u_min = p_min, u_max = p_max, v_min = q_min, v_max = q_max, checkerboard_colors=[GREEN_D,GREEN_E]) 
        for p_min,p_max,q_min,q_max in f_tuple]
    face_atoms = VGroup(*f_part)
        
    circle0 = Circle(radius=0.98, fill_opacity=0.2, stroke_width=0, color=GREEN)
    circle1 = circle0.copy()
    circle2 = circle0.copy().rotate(PI/2, axis = RIGHT)
    circle3 = circle2.copy()
    circle4 = circle0.copy().rotate(PI/2, axis = UP)
    circle5 = circle4.copy()
    circles = VGroup(circle0,circle1,circle2,circle3,circle4,circle5)

    face_atoms_portions = [
                            VGroup(face_atoms[0],circle0), 
                            VGroup(face_atoms[1],circle1), 
                            VGroup(face_atoms[2],circle2), 
                            VGroup(face_atoms[3],circle3),
                            VGroup(face_atoms[4],circle4),
                            VGroup(face_atoms[5],circle5) 
                          ]
    face_atoms_portions_pos = [ np.array([0,0,-a]), np.array([0,0,a]),  np.array([0,a,0]), 
                                np.array([0,-a,0]), np.array([-a,0,0]), np.array([a,0,0]) ]
    for i in range(6):
        face_atoms_portions[i].shift(face_atoms_portions_pos[i])

    unit_cell = VGroup(cube,face_atoms,corner_atom,circles)
    if(corner_face_cube):
        return (unit_cell,corner_atom_portion,face_atoms_portions,cube)
    else:
        return unit_cell

#       #       #       #       #       #       #       #       #       #       #       #

def unit_cell_surface():
    a = 1.41 # side_length/2
    sq = Square(side_length=2*a,stroke_width=1,fill_opacity=0)
    center_circle = Circle(radius=1,stroke_width=0,fill_opacity=0.5,color=GREEN)
    sectors = [AnnularSector(inner_radius=0,outer_radius=1,start_angle=x,fill_opacity=1,color=BLUE) for x in [0,PI/2,PI,3*PI/2]]
    sectors_pos = [np.array([-a,-a,0]), np.array([a,-a,0]), np.array([a,a,0]), np.array([-a,a,0])]
    for i in range(4):
        sectors[i].shift(sectors_pos[i])
    surface = VGroup(sq,center_circle,*sectors)
    return surface

#       #       #       #       #       #       #       #       #       #       #       #

class FCCIntro(Scene):
    def construct(self):
        intro  = TextMobject("Face Centered Cubic Crystal Structure")
        intro.set_color_by_gradient(BLUE)
        self.play(
            Write(intro), run_time = 6
        )
        self.wait()
        self.play(
            FadeOutAndShift(intro), run_time = 2
        )

#       #       #       #       #       #       #       #       #       #       #       #

class FCCScene1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES,theta=-30*DEGREES, distance=5)
        
        a = np.sqrt(2)/2 # side_length/2 where radius of an atom will be 0.5 
        # Title
        title = TextMobject("FCC Unit Cell")
        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)
        self.play(
            FadeInFrom(title, direction=UP), run_time = 2
        )

        # Corner Atoms
        corner_atoms_coords = [(x,y,z) for x in [a,-a] for y in [a,-a] for z in [a,-a]]
        '''
         corner_atoms_coords = [     (a, a, a),    (a, a, -a),   (a, -a, a),  (a, -a, -a),
                                    (-a, a, a),   (-a, a, -a),  (-a, -a, a),  (-a, -a, -a)]
        '''
        corner_atoms = VGroup(*[Sphere(radius=0.5).shift(np.array([x,y,z])) for (x,y,z) in corner_atoms_coords])

        # Face Atoms
        face_atoms_coords = [(a,0,0),   (-a,0,0),    (0,a,0),    (0,-a,0),  (0,0,a),    (0,0,-a)]
        face_atoms = VGroup(*[Sphere(radius=0.5,checkerboard_colors=[GREEN_D,GREEN_E]).shift(np.array([x,y,z])) for (x,y,z) in face_atoms_coords])
        self.wait(2)
        self.add(corner_atoms)
        self.wait(3)
        self.add(face_atoms)
        self.wait(3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(10)
        self.stop_ambient_camera_rotation()

#       #       #       #       #       #       #       #       #       #       #       #

class FCCScene2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES,theta=-30*DEGREES)
        
        a = np.sqrt(2) # side_length where radius of an atom will be 0.5 
        # Title
        title = TextMobject("FCC Unit Cell","(Lattice View)")
        title[1].scale(0.6)
        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)
        self.play(
            FadeInFrom(title, direction=UP), run_time = 2
        )
        # Unit Cell Cube
        cube = Cube(side_length=(2*a), fill_opacity=0.1, stroke_width=1.5)
        # Corner Atoms
        corner_atoms_coords = [(x,y,z) for x in [a,-a] for y in [a,-a] for z in [a,-a]]
        '''
         corner_atoms_coords = [     (a, a, a),    (a, a, -a),   (a, -a, a),  (a, -a, -a),
                                    (-a, a, a),   (-a, a, -a),  (-a, -a, a),  (-a, -a, -a)]
        '''
        corner_atoms = VGroup(*[Sphere(radius=0.25).shift(np.array([x,y,z])) for (x,y,z) in corner_atoms_coords])

        # Face Atoms
        face_atoms_coords = [(a,0,0),   (-a,0,0),    (0,a,0),    (0,-a,0),  (0,0,a),    (0,0,-a)]
        face_atoms = VGroup(*[Sphere(radius=0.25,checkerboard_colors=[GREEN_D,GREEN_E]).shift(np.array([x,y,z])) for (x,y,z) in face_atoms_coords])

        unit_cell = VGroup(cube,corner_atoms,face_atoms)
        self.add(unit_cell)
        self.wait(3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(10)
        
        # Information
        info1 = TextMobject("There are 8 atoms in the corner and")
        info2 = TextMobject("6 atoms in 6 faces of the cube")
        info1.scale(0.6)
        info2.scale(0.6)
        info1.set_color(BLUE)
        info2.set_color(BLUE)
        self.add_fixed_in_frame_mobjects(info1)
        info1.to_edge(DOWN)
        info1.shift(np.array([0,0.5,0]))
        self.play(
            FadeIn(info1), run_time = 2
        )
        self.add_fixed_in_frame_mobjects(info2)
        info2.next_to(info1, DOWN, buff = 0.2)
        self.play(
            FadeIn(info2), run_time = 2
        )
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(
            FadeOut(title),
            FadeOut(info1),
            FadeOut(info2), run_time = 1
        )
        self.move_camera(phi=75*DEGREES,theta=-70*DEGREES, run_time=3)
        self.wait(5)

#       #       #       #       #       #       #       #       #       #       #       #

class FCCScene3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,theta=-70*DEGREES)

        a = np.sqrt(2) # side_length where radius of an atom will be 0.5
        # Unit Cell 1
        cube1 = Cube(side_length=(2*a), fill_opacity=0.1, stroke_width=1.5)
        # Corner Atoms
        corner_atoms_coords1 = [(x,y,z) for x in [a,-a] for y in [a,-a] for z in [a,-a]]
        '''
         corner_atoms_coords1 = [     (a, a, a),    (a, a, -a),   (a, -a, a),  (a, -a, -a),
                                    (-a, a, a),   (-a, a, -a),  (-a, -a, a),  (-a, -a, -a)]
        '''
        corner_atoms1 = VGroup(*[Sphere(radius=0.25).shift(np.array([x,y,z])) for (x,y,z) in corner_atoms_coords1])

        # Face Atoms
        face_atoms_coords1 = [(a,0,0),   (-a,0,0),    (0,a,0),    (0,-a,0),  (0,0,a),    (0,0,-a)]
        face_atoms1 = VGroup(*[Sphere(radius=0.25,checkerboard_colors=[GREEN_D,GREEN_E]).shift(np.array([x,y,z])) for (x,y,z) in face_atoms_coords1])

        unit_cell1 = VGroup(cube1,corner_atoms1,face_atoms1)

        self.add(unit_cell1)

        # Unit Cell 2
        cube2 = cube1.copy()
        corner_atoms_coords2 = corner_atoms_coords1.copy()
        for x in range(4):
            corner_atoms_coords2.pop()
        '''
         corner_atoms_coords2 = [(a, a, a),    (a, a, -a),   (a, -a, a),  (a, -a, -a)]
        '''
        corner_atoms2 = VGroup(*[Sphere(radius=0.25).shift(np.array([x,y,z])) for (x,y,z) in corner_atoms_coords2])
        face_atoms_coords2 = face_atoms_coords1.copy()
        face_atoms_coords2.pop(1)
        ''' 
        face_atoms_coords2 = [(a,0,0), (0,a,0),  (0,-a,0),  (0,0,a),    (0,0,-a)]
        '''
        face_atoms2 = VGroup(*[Sphere(radius=0.25,checkerboard_colors=[GREEN_D,GREEN_E]).shift(np.array([x,y,z])) for (x,y,z) in face_atoms_coords2])
        unit_cell2 = VGroup(cube2,corner_atoms2,face_atoms2)
        
        self.add(unit_cell2)
        
        # Title
        title = TextMobject("Coordination Number")
        title.set_color(GREEN_D)
        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)
        self.play(
            FadeIn(title), run_time = 1
        )

        self.play(
            unit_cell1.shift, np.array(np.array([-a,0,0])),
            unit_cell2.shift, np.array(np.array([a,0,0])), run_time  = 2
        )
        #self.move_camera()

        # Information
        info1 = TextMobject("One atom is directly connected to")
        info2 = TextMobject("4 corner atoms,")
        info3 = TextMobject("4 face atoms on each side")
        info2.set_color(BLUE)
        info3.set_color(GREEN)
        info1.scale(0.8)
        info2.scale(0.8)
        info3.scale(0.8)
        self.add_fixed_in_frame_mobjects(info1)
        info1.to_corner(DL)
        info1.shift(np.array([0,0.5,0]))
        self.play(
            FadeIn(info1),
            face_atoms1[0].set_color, YELLOW, run_time = 2
        )
        # Connection
        corner_conn = VGroup(*[DashedLine(np.array([0,0,0]), np.array(np.array([x-a,y,z]))) for (x,y,z) in corner_atoms_coords1[:4]])
        corner_conn.set_color(YELLOW)
        face_conn1 = VGroup(*[DashedLine(np.array([0,0,0]), np.array([x-a,y,z])) for (x,y,z) in face_atoms_coords1[2:]])
        face_conn2 = VGroup(*[DashedLine(np.array([0,0,0]), np.array([x+a,y,z])) for (x,y,z) in face_atoms_coords2[1:]])
        face_conn1.set_color(YELLOW)
        face_conn2.set_color(YELLOW)
        
        self.add_fixed_in_frame_mobjects(info2)
        info2.next_to(info1, RIGHT, buff = 0.2)
        self.play(FadeIn(info2))
        self.play(
            ShowCreation(corner_conn), run_time = 4
        )
        self.wait(2)
        self.add_fixed_in_frame_mobjects(info3)
        info3.next_to(info2, RIGHT, buff = 0.2)
        self.play(FadeIn(info3))
        self.play(
            ShowCreation(face_conn2), run_time  = 4
        )
        self.move_camera(phi=75*DEGREES, theta=-110*DEGREES, run_time = 3)
        self.play(
            ShowCreation(face_conn1), run_time = 4
        )
        self.wait(2)
        cn = TexMobject("\\text{Coordination Number for FCC}","=","4\\text{(corner)}+2\\times4\\text{(face)}","=","12")
        self.add_fixed_in_frame_mobjects(cn)
        cn.to_edge(DOWN)
        self.play(
            FadeOut(info1),
            FadeOut(info2),
            FadeOut(info3),
            FadeInFrom(cn, direction = DOWN), run_time = 3
        )
        self.wait(5)
        self.play(
            FadeOut(cn),
            FadeOut(corner_conn),
            FadeOut(face_conn1),
            FadeOut(face_conn2),
            FadeOutAndShift(title, direction = UP), run_time = 2
        )
        self.remove(unit_cell1)
        self.remove(unit_cell2)
        self.wait(5)

#       #       #       #       #       #       #       #       #       #       #       #

class FCCScene4(ThreeDScene):

    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-50*DEGREES)
        # Cutting Plane
        cutting_plane = Rectangle(width=2.5,height=2.5,fill_opacity=0.2, stroke_width = 0).rotate(PI/2, axis = RIGHT)
        # Single Atom in two portion
        circle1 = Circle(radius=1,fill_opacity = 0.2,stroke_width = 0).rotate(PI/2, axis = RIGHT)
        circle1.set_color(GREEN)
        circle2 = circle1.copy()
        
        atom_u_min = [0,0]
        atom_u_max = [PI,PI]
        atom_v_min = [PI,0]
        atom_v_max = [TAU,PI]
        atom_tuple = zip(atom_u_min,atom_u_max,atom_v_min,atom_v_max)
        atom_part = [ParametricSurface(
            lambda u,v : np.array([
                np.sin(u)*np.cos(v),
                np.sin(u)*np.sin(v),
                np.cos(u)
            ]), u_min = p_min, u_max = p_max, v_min = q_min, v_max = q_max, checkerboard_colors=[GREEN_D,GREEN_E]) 
            for p_min,p_max,q_min,q_max in atom_tuple]
        single_atom = VGroup(*atom_part)
        atom_portion = [    VGroup(circle1,single_atom[0]),
                            VGroup(circle2,single_atom[1])]
        full_atom = VGroup(*atom_portion)

        # Information
        info1 = TextMobject("A surface of a unit cell divides face atom into two portion")
        info2 = TextMobject("Each portions is $\\frac{1}{2}$ of an atom")
        self.play(
            FadeInFrom(full_atom, direction = UP)
        )
        self.play(
            FadeInFrom(cutting_plane, direction = np.array([0,0,2])), run_time = 2
        )
        self.add(circle1,circle2)
        self.play(
            atom_portion[0].shift, np.array([0,-1,0]),
            atom_portion[1].shift, np.array([0,1,0]), run_time = 3
        )
        self.add_fixed_in_frame_mobjects(info1)
        info1.to_edge(DL)
        self.play(
            FadeIn(info1), run_time = 2
        )
        self.wait(2)
        self.add_fixed_in_frame_mobjects(info2)
        info2.to_edge(UP)
        self.play(
            FadeIn(info2), run_time = 2
        )
        self.play(
            FadeOutAndShift(cutting_plane, direction = np.array([0,0,-2]))
        )
        self.wait(2)
        self.play(
            atom_portion[0].shift, np.array([0,1,0]),
            atom_portion[1].shift, np.array([0,-1,0]), run_time = 3
        )
        self.play(
            FadeOut(full_atom),
            FadeOut(info1),
            FadeOut(info2), run_time = 2
        )
        self.wait(5)

#       #       #       #       #       #       #       #       #       #       #       #

class FCCScene5(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES,theta=-30*DEGREES,distance=7) 
        a = 1.41 # side_length/2
        unit_cell, corner_atom_portion, face_atoms_portions, cube = fcc_unit_cell(corner_face_cube=True)
        self.add(unit_cell)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75*DEGREES,theta=-90*DEGREES,distance=7)
        # Information
        info1 = TexMobject("\\frac{1}{8}\\times8\\text{ (corner) }","=","1")
        info2 = TexMobject("\\frac{1}{2}\\times6\\text{ (face) }","=","3")
        info3 = TexMobject("\\text{Atoms Per Unit Cell for FCC}","=","1","+","3","=","4")
        info1.set_color(BLUE)
        info2.set_color(GREEN)
        info3[2].set_color(BLUE)
        info3[4].set_color(GREEN)
        info1.scale(0.7)
        info2.scale(0.7)
        self.play(
            FadeOut(cube)
        )
        # Atom Portions shift
        corner_atom_portion_pos_new = [ np.array([a+4,a,a]), np.array([-a+4,a,a]), np.array([-a+4,-a,a]), np.array([a+4,-a,a]),
                                        np.array([a+4,a,-a]), np.array([-a+4,a,-a]), np.array([-a+4,-a,-a]), np.array([a+4,-a,-a]) ]
        face_atoms_portions_pos_new = [ np.array([1,0,a]), np.array([1,0,-a]),  np.array([-1.5,-a,0]), 
                                        np.array([-1.5,a,0]), np.array([a-4,0,0]), np.array([-a-4,0,0]) ]
        self.play(
            *[ApplyMethod(corner_atom_portion[i].shift, corner_atom_portion_pos_new[i]) for i in range(8)], run_time = 3
        )

        self.play(
            face_atoms_portions[4].shift, face_atoms_portions_pos_new[4],
            face_atoms_portions[5].shift, face_atoms_portions_pos_new[5], run_time = 3
        )
        self.play(
            face_atoms_portions[2].shift, face_atoms_portions_pos_new[2],
            face_atoms_portions[3].shift, face_atoms_portions_pos_new[3], run_time = 3
        )
        self.play(
            face_atoms_portions[0].shift, face_atoms_portions_pos_new[0],
            face_atoms_portions[1].shift, face_atoms_portions_pos_new[1], run_time = 3
        )
        line1 = Line(np.array([-4,0,0]),np.array([1,0,0]), stroke_width=0)
        line2 = Line(np.array([5.1,0,0]),np.array([3.1,0,0]), stroke_width=0)
        brace1 = Brace(line1, UP, buff = 1.5)
        brace2 = Brace(line2, UP, buff = 1.5)
        self.add_fixed_in_frame_mobjects(line1,brace1,line2,brace2)
        self.play(
            GrowFromCenter(brace1),
            GrowFromCenter(brace2), run_time = 3
        )
        self.add_fixed_in_frame_mobjects(info1)
        info1.shift(np.array([4.1,2.3,0]))
        self.add_fixed_in_frame_mobjects(info2)
        info2.shift(np.array([-1.5,2.3,0]))
        self.play(
            FadeInFrom(info1, direction = DOWN),
            FadeInFrom(info2, direction = DOWN), run_time = 2
        )
        self.wait(3)
        self.add_fixed_in_frame_mobjects(info3)
        info3.to_edge(DOWN)
        self.play(
            FadeInFrom(info3, direction = UP), run_time = 2
        )
        self.wait(5)
        self.remove(*corner_atom_portion)
        self.remove(*face_atoms_portions)
        self.play(
            FadeOut(info1),
            FadeOut(info2),
            FadeOut(info3),
            FadeOut(brace1),
            FadeOut(brace2), run_time = 3
        )
        self.wait(3)

#       #       #       #       #       #       #       #       #       #       #       #

class FCCScene6(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES,theta=-90*DEGREES,distance=7)
        a = 1.41 # side_length/2
        unit_cell = fcc_unit_cell()
        self.add(unit_cell)
        surface = unit_cell_surface()
        surface.rotate(PI/2,axis = RIGHT)
        surface.shift(np.array([0,-a,0]))
        self.play(
            FadeIn(surface), run_time = 3
        )
        self.play(
            surface.shift, np.array([10,0,0]), run_time = 5
        )
        self.wait(5)

#       #       #       #       #       #       #       #       #       #       #       #

class FCCScene7(Scene):
    def construct(self):
        a = 1.41 # side_length/2
        surface = unit_cell_surface()
        surface.shift(np.array([-10,0,0]))
        self.add(surface)
        self.play(
            surface.shift, np.array([5,0,0]), run_time = 2
        )
        self.play(
            surface.to_corner, UL, run_time = 2
        )
        corner_points = [surface.get_corner(DL), surface.get_corner(DR), surface.get_corner(UL), surface.get_corner(UR)]
        line1 = Line(corner_points[0], corner_points[1])
        line2 = Line(corner_points[1], corner_points[3])
        line3 = DashedLine(corner_points[0], corner_points[3])
        brace1 = Brace(line1, DOWN, buff = SMALL_BUFF)
        brace2 = Brace(line2, RIGHT, buff = SMALL_BUFF)
        label1 = brace1.get_text("$a$")
        label2 = brace2.get_text("$a$")
        label3 = TexMobject("4","R")
        label3.scale(0.7)
        label3[1].set_color(RED_E)
        label = VGroup(label1,label2)
        label.set_color(PURPLE_A)
        self.play(
            GrowFromCenter(brace1),
            GrowFromCenter(brace2),
            FadeInFrom(label1, direction=DOWN),
            FadeInFrom(label2, direction=RIGHT), run_time = 3
        )
        diagonal = TexMobject("\\sqrt{2}","a","=","4","R")
        diag_pos = (corner_points[0]+corner_points[3])/2
        np.add.at(diag_pos,[0],-0.2)            # np.add.at adds at a specific postion of an numpy array 
        np.add.at(diag_pos,[1], 0.2)
        diagonal.move_to(diag_pos)
        np.add.at(diag_pos,[0], 0.6)
        np.add.at(diag_pos,[1],-0.6)
        label3.move_to(diag_pos)
        diagonal.scale(0.7)
        diagonal[1].set_color(PURPLE_A) 
        diagonal[4].set_color(RED_E)
        rel = diagonal.copy()
        diagonal.rotate(PI/4)
        four_r = VGroup(*diagonal[2:])
        self.play(
            ShowCreation(line3), run_time = 2
        )
        self.play(
            FadeIn(label3), run_time = 2
        )
        self.play(
            Write(diagonal[0]),
            ReplacementTransform(label.copy(), diagonal[1]), run_time = 2
        )
        self.wait()
        self.play(
            ReplacementTransform(label3, four_r, path_arc = PI), run_time = 3
        )
        rel.next_to(label1, DOWN, buff = 0.5)
        rel_1 = TexMobject("a","=","\\frac{4}{\\sqrt{2}}","R")
        rel_2 = TexMobject("a","=","2\\sqrt{2}","R")
        rel_1[0].set_color(PURPLE_A)
        rel_2[0].set_color(PURPLE_A)
        rel_1[3].set_color(RED_E)
        rel_2[3].set_color(RED_E)
        rel_1.next_to(label1, DOWN, buff = 0.5)
        rel_2.next_to(label1, DOWN, buff = 0.5)
        rel_1.scale(0.8)
        rel_2.scale(0.8)
        rect = SurroundingRectangle(rel_2, buff = 0.1)
        rect.set_color(WHITE)
        self.play(
            ReplacementTransform(diagonal.copy(), rel, path_arc = -PI), run_time = 3
        )
        self.wait()
        self.play(
            ReplacementTransform(rel, rel_1), run_time = 2
        )
        self.wait()
        self.play(
            ReplacementTransform(rel_1,rel_2), run_time = 2
        )
        self.play( 
            ShowCreation(rect), run_time = 3
        )
        # Information
        edge = TexMobject("a","=","\\text{Edge Length}")
        radius = TexMobject("R","=","\\text{Radius of an Atom}")
        edge.scale(0.7)
        radius.scale(0.7)
        edge[0].set_color(PURPLE_A)
        radius[0].set_color(RED_E)
        radius.next_to(edge, DOWN, buff = 0.5)
        radius.align_to(edge, LEFT)
        info1 = VGroup(edge,radius)
        info1.to_corner(DL)
        self.play(
            FadeIn(info1), run_time = 2
        )
        # Information
        info2 = TextMobject("Atomic Packing Factor")
        info2.to_corner(UP)
        info2.shift(np.array([1,0,0]))
        info2.set_color_by_gradient(SUBU_C,SUBU_E)
        info3 = TexMobject("=","\\frac{\\text{Volume of Atoms}}{\\text{Volume of Unit Cell}}")
        info3.next_to(info2, DOWN, buff = 0.8)
        info3.align_to(info2, LEFT)
        info3.scale(0.7)
        info4 = TexMobject("={","4","\\times","\\frac{4}{3}","\\pi","R","^3","\\over","a","^3}")
        info4.scale(0.7)
        info4.next_to(info3, DOWN, buff = 0.3)
        info4.align_to(info3, LEFT)
        info4[1].set_color(GREEN_E)
        info4[5].set_color(RED_E)
        info4[8].set_color(PURPLE_A)
        info5 = TexMobject("={","4","\\times","\\frac{4}{3}","\\pi","R","^3","\\over","(2\\sqrt{2}","R",")^3}")
        info5.scale(0.7)
        info5.next_to(info4, DOWN, buff = 0.3)
        info5.align_to(info4, LEFT)
        info5[1].set_color(GREEN_E)
        info5[5].set_color(RED_E)
        info5[9].set_color(RED_E)
        info6 = TexMobject("\\approx","0.74")
        info6.scale(0.7)
        info6.next_to(info5, DOWN, buff = 0.3)
        info6.align_to(info5, LEFT)
        for inf in [info2,info3,info4]:
            self.play(
                FadeInFrom(inf, direction = UP), run_time =2
            )
            self.wait(2)
        self.play(
            FadeIn(info5[:8]), run_time = 2
        )
        self.play(
            ReplacementTransform(rel_2[2:].copy(),info5[8:], path_arc = PI), run_time = 2
        )
        self.wait()
        self.play(
            Write(info6), run_time = 2
        )
        self.wait(3)
        info = VGroup(info1, info2, info3, info4, info5, info6)
        braces = VGroup(brace1, brace2, line3)
        labels = VGroup(label,diagonal)
        relations = VGroup(rel_2, rect)
        self.play(
            FadeOut(surface),
            FadeOut(braces),
            FadeOut(labels),
            FadeOut(relations),
            FadeOut(info), run_time = 3
        )
        self.wait()

#       #       #       #       #       #       #       #       #       #       #       #

class FCCOutro(Scene):
    def construct(self):
        outro = TextMobject("Thank You For Watching")
        outro.set_color_by_gradient(MAROON_E,MAROON_A)
        self.play(
            Write(outro), run_time = 4
        )
        self.wait()
        self.play(
            FadeOut(outro), run_time = 2
        )