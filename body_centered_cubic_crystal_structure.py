from manimlib.imports import *
import numpy as np 

class BCCIntro(Scene):
    def construct(self):
        intro = TextMobject("Body Centered Cubic Crystal Structure")
        intro.set_color_by_gradient(AZURE_LANE_C,AZURE_LANE_E)
        self.play(FadeInFrom(intro,direction=UP), run_time=3)
        self.wait(3)
        self.play(FadeOutAndShift(intro), run_time = 2)
        self.wait(2)

#       #       #       #       #       #       #       #       #       #   

class BCCOutro(Scene):
    def construct(self):
        outro = TextMobject("Thank You For Watching")
        outro.set_color_by_gradient(FLARE_A,FLARE_E)
        self.play(Write(outro), run_time = 4)
        self.wait(2)
        self.play(FadeOutAndShift(outro,direction=UP), run_time = 2)
        self.wait()

#       #       #       #       #       #       #       #       #       #   

class BCCScene1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,theta=30*DEGREES,distance=9)
        
        a = 1.155 # Side length of a unit cell
        
        # Corner Atoms
        
        corner_atoms_coords = []
        for x in [a,0,-a]:
            for y in [a,0,-a]:
                for z in [-a,0,a]:
                    corner_atoms_coords.append((x,y,z))
        '''                          0            1           2           3            4           5            6             7            8           
         corner_atoms_coord = [ ( a, a, -a), ( a, a, 0), ( a, a, a), ( a, 0, -a), ( a, 0, 0), ( a, 0, a), ( a, -a, -a), ( a, -a, 0), ( a, -a, a),
                                ( 0, a, -a), ( 0, a, 0), ( 0, a, a), ( 0, 0, -a), ( 0, 0, 0), ( 0, 0, a), ( 0, -a, -a), ( 0, -a, 0), ( 0, -a, a), 
                                (-a, a, -a), (-a, a, 0), (-a, a, a), (-a, 0, -a), (-a, 0, 0), (-a, 0, a), (-a, -a, -a), (-a, -a, 0), (-a, -a, a)]
        '''
        corner_atoms = [Sphere(radius=0.5).shift(np.array([x,y,z])) for (x,y,z) in corner_atoms_coords]
        corner_atoms_group1 = VGroup(*[corner_atoms[x] for x in [0,9,18,3,12,21,6,15,24]])
        corner_atoms_group2 = VGroup(*[corner_atoms[x] for x in [1,10,19,4,13,22,7,16,25]])
        corner_atoms_group3 = VGroup(*[corner_atoms[x] for x in [2,11,20,5,14,23,8,17,26]])

        # Center Atoms

        center_atoms_coords = []
        for x in [a/2,-a/2]:
            for y in [a/2,-a/2]:
                for z in [-a/2,a/2]:
                    center_atoms_coords.append((x,y,z))
        '''                             0                  1                  2                   3
        center_atoms_coords = [ ( a/2, a/2, -a/2), ( a/2, a/2, a/2), ( a/2, -a/2, -a/2), ( a/2, -a/2, a/2),
                                (-a/2, a/2, -a/2), (-a/2, a/2, a/2), (-a/2, -a/2, -a/2), (-a/2, -a/2, a/2)]
        '''
        center_atoms = [Sphere(radius=0.5,checkerboard_colors=[RED_D,RED_E]).shift(np.array([x,y,z])) for (x,y,z) in center_atoms_coords]
        center_atoms_group1 = VGroup(*[center_atoms[x] for x in [0,4,2,6]])
        center_atoms_group2 = VGroup(*[center_atoms[x] for x in [1,5,3,7]])

        # Information
        info1 = TextMobject("Body Centered Cubic Crystal")
        info1.set_color_by_gradient(BLUE,GREEN)

        self.add(corner_atoms_group1)
        self.wait(2)
        self.add(center_atoms_group1)
        self.wait(2)
        self.add(corner_atoms_group2)
        self.wait(2)
        self.add(center_atoms_group2)
        self.wait(2)
        self.add(corner_atoms_group3)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(info1)
        info1.to_edge(UP)
        self.play(FadeInFrom(info1,direction=UP), run_time = 2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75*DEGREES,theta=0*DEGREES,distance=9, run_time=3)
        unit_cell = VGroup( corner_atoms[1],corner_atoms[10],corner_atoms[4],corner_atoms[13],
                            corner_atoms[2],corner_atoms[11],corner_atoms[5],corner_atoms[14],
                            center_atoms[1])
        self.play(
            unit_cell.copy().shift, np.array([0,8,0]), run_time = 3
        )
        self.wait(5)

#       #       #       #       #       #       #       #       #       #   

class BCCScene2(ThreeDScene):
    def construct(self):
        a = 1.155 # side length
        self.set_camera_orientation(phi=75*DEGREES, theta= 0*DEGREES, distance=9)
        corner_atoms_coords = []
        # Unit Cell
        center_atom = Sphere(radius=0.5,checkerboard_colors=[RED_D,RED_E])
        for x in [a/2,-a/2]:
            for y in [a/2,-a/2]:
                for z in [-a/2,a/2]:
                    corner_atoms_coords.append((x,y,z))
        
        '''                             0                  1                  2                   3
        corner_atoms_coords = [ ( a/2, a/2, -a/2), ( a/2, a/2, a/2), ( a/2, -a/2, -a/2), ( a/2, -a/2, a/2),
                                (-a/2, a/2, -a/2), (-a/2, a/2, a/2), (-a/2, -a/2, -a/2), (-a/2, -a/2, a/2)]
        '''
        unit_cell = VGroup(*[Sphere(radius=0.5).shift(np.array([x,y,z])) for (x,y,z) in corner_atoms_coords],center_atom)
        unit_cell.shift(np.array([0,-8,0]))
        self.add(unit_cell)
        self.play(
            unit_cell.shift, np.array([0,8,0]), run_time = 3
        )
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2)

        # Information
        info1 = TextMobject("BCC Unit Cell")
        info1.set_color_by_gradient(GREEN, BLUE)
        info2 = TextMobject("A single atom is directly connected")
        info3 = TextMobject("8 neighbouring atoms")
        info4 = TextMobject("Coordination Number for BCC is 8")
        info4.set_color(GREEN)
        
        self.add_fixed_in_frame_mobjects(info1)
        info1.to_edge(UP)
        self.play(FadeInFrom(info1, direction=LEFT))
        self.add_fixed_in_frame_mobjects(info2,info3)
        info2.scale(0.7)
        info3.scale(0.7)
        info2.to_corner(UR)
        info2.shift(np.array([0,-1,0]))
        info3.next_to(info2,DOWN,buff = 0.2)
        self.play(
            FadeInFrom(info2,direction=UP),
            FadeInFrom(info3,direction=UP), run_time = 2
        )
        self.wait(4)
        self.add_fixed_in_frame_mobjects(info4)
        info4.to_edge(DOWN)
        self.play(Write(info4), run_time = 3)
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.play(
            FadeOut(info1),
            FadeOut(info2),
            FadeOut(info3),
            FadeOut(info4),
            FadeOut(unit_cell), run_time = 3
        )
        self.wait(5)

#       #       #       #       #       #       #       #       #       #   

class BCCScene3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,theta=30*DEGREES,distance=7)
        a = 1.175 # side length/2
        # Cube
        cube = Cube(side_length=2*a, fill_opacity=0.1,stroke_width=0.5)
        # Center Atom
        center_atom = Sphere(checkerboard_colors=[RED_D,RED_E])
        # Corner Atom Portions
                    #      0      1       2       3       4      5       6         7             
        atom_u_min = [     0,     0,      0,      0,   PI/2,  PI/2,   PI/2,     PI/2]
        atom_u_max = [  PI/2,  PI/2,   PI/2,   PI/2,     PI,    PI,     PI,       PI]
        atom_v_min = [     0,  PI/2,     PI, 3*PI/2,      0,  PI/2,     PI,   3*PI/2]
        atom_v_max = [  PI/2,    PI, 3*PI/2,   2*PI,   PI/2,    PI, 3*PI/2,     2*PI]
        atom_tuple = zip(atom_u_min,atom_u_max,atom_v_min,atom_v_max)
        atom_part = [ParametricSurface(
            lambda u,v: np.array(
                            [ np.sin(u)*np.cos(v),
                              np.sin(u)*np.sin(v),
                              np.cos(u)]), u_min = p_min, u_max = p_max, v_min = q_min, v_max = q_max)
                    for p_min,p_max,q_min,q_max in atom_tuple]
        single_atom = VGroup(*atom_part)

        angle0 = [0,PI/2,PI,3*PI/2,0,PI/2,PI,3*PI/2]
        sector_xy_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
        sector_yz_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
        sector_zx_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
        sector_xy = VGroup(*sector_xy_array)
        sector_yz = VGroup(*sector_yz_array).rotate(PI/2,axis=UP)
        sector_zx = VGroup(*sector_zx_array).rotate(PI/2,axis=RIGHT)

        atom_portion = [
                            VGroup(single_atom[0],sector_xy_array[0],sector_yz_array[1],sector_zx_array[0]), # 0
                            VGroup(single_atom[1],sector_xy_array[1],sector_yz_array[5],sector_zx_array[1]), # 1
                            VGroup(single_atom[2],sector_xy_array[2],sector_yz_array[2],sector_zx_array[5]), # 2
                            VGroup(single_atom[3],sector_xy_array[3],sector_yz_array[6],sector_zx_array[4]), # 3
                            VGroup(single_atom[4],sector_xy_array[4],sector_yz_array[0],sector_zx_array[3]), # 4
                            VGroup(single_atom[5],sector_xy_array[5],sector_yz_array[4],sector_zx_array[2]), # 5
                            VGroup(single_atom[6],sector_xy_array[6],sector_yz_array[3],sector_zx_array[6]), # 6
                            VGroup(single_atom[7],sector_xy_array[7],sector_yz_array[7],sector_zx_array[7])  # 7
                        ]
        
        unit_cell = VGroup(*atom_portion,center_atom)
                              #         0                   1                       2                   3   
        atom_portion_pos = [np.array([-a,-a,-a]),  np.array([a,-a,-a]),  np.array([a,a,-a]),  np.array([-a, a,-a]),
                              np.array([-a,-a,a]),   np.array([a,-a,a]),   np.array([a,a,a]),   np.array([-a,a,a])]
                              #         4                   5                       6                   7
        for i in range(8):
            atom_portion[i].shift(atom_portion_pos[i])
        
        #Information

        info1 = TextMobject("BCC Unit Cell")
        info1.set_color_by_gradient(GREEN, BLUE)
        info2 = TexMobject("1\\times1(\\text{center}) = ","1")
        info3 = TexMobject("\\frac{1}{8}\\times8(\\text{corner}) = ","1")
        info4 = TexMobject("\\text{Atoms Per Unit Cell}","=","1","+","1","=","2")
        info4.set_color(YELLOW)
        info2.scale(0.6)
        info3.scale(0.6)
        self.add_fixed_in_frame_mobjects(info1)
        info1.to_edge(UP)
        self.add(info1)
        self.add(cube)
        self.add(unit_cell)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=70*DEGREES,theta=0*DEGREES,distance=7, run_time = 3)
        self.wait(2)
        self.play(
            unit_cell.shift, np.array([0,-2,0]),
            cube.shift, np.array([0,-2,0]), run_time = 3
        )
        self.wait(2)
        self.play(FadeOut(cube))
        atom_portion_pos_new = [np.array([a,a+4,a]),  np.array([-a,a+4,a]),  np.array([-a,-a+4,a]),  np.array([a, -a+4,a]),
                              np.array([a,a+4,-a]),   np.array([-a,a+4,-a]),   np.array([-a,-a+4,-a]),   np.array([a,-a+4,-a])]
        for i in range(8):
            self.play(atom_portion[i].shift, atom_portion_pos_new[i])
        self.add_fixed_in_frame_mobjects(info2)
        info2.shift(np.array([-2,2,0]))
        self.play(Write(info2), run_time = 3)
        self.add_fixed_in_frame_mobjects(info3)
        info3.next_to(info2, RIGHT, buff = 2.5)
        self.play(Write(info3), run_time = 3)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(info4)
        info4.to_edge(DOWN)
        self.play(FadeInFrom(info4,direction=UP), run_time = 3)
        self.wait(5)

        self.play(
            FadeOut(unit_cell),
            FadeOut(info1),
            FadeOut(info2),
            FadeOut(info3),
            FadeOut(info4), run_time = 4
        )
        self.wait(2)

#       #       #       #       #       #       #       #       #       #

class BCCScene4(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES, distance = 8)

        # Title
        title = TextMobject("Relation Between Edge Length ","$a$"," and Radius of an Atom ","$R$")
        title[1].set_color(RED)
        title[3].set_color(BLUE)
        # Close-Packed Direction
        cpd = TextMobject("$\\bullet$ Close Packed Direction is along ","Cube Diagonal")
        
        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)
        title.scale(0.8)
        self.play(FadeInFrom(title, direction=UP), run_time = 3)
        self.add_fixed_in_frame_mobjects(cpd)
        cpd.scale(0.7)
        cpd.to_edge(DOWN)
        self.play(FadeInFrom(cpd, direction=DOWN), run_time = 2)
        self.wait(2)

        # Drawing
        a = 2*1.175 # side_length
        cube = Cube(side_length=a,fill_opacity=0.1,stroke_width=0.6)
        brace1_line = Line(np.array([a/2,-a/2,-a/2]), np.array([a/2,a/2,-a/2]))
        brace2_line = Line(np.array([-a/2,-a/2,-a/2]), np.array([a/2,-a/2,-a/2]))
        brace3_line = Line(np.array([-a/2,-a/2,-a/2]), np.array([-a/2,a*0.9,-a/2]))
        face_diagonal = Line(np.array([-a/2,-a/2,-a/2]), np.array([a/2,a/2,-a/2]))
        cube_diagonal = DashedLine(np.array([-a/2,-a/2,-a/2]), np.array([a/2,a/2,a/2]),dash_length=0.1)
        cube_diagonal.set_color(YELLOW)
        
        self.play(ShowCreation(cube), run_time = 3)
        self.wait()
        
        brace1 = Brace(brace1_line, RIGHT, buff = SMALL_BUFF)
        brace2 = Brace(brace2_line, DOWN, buff = SMALL_BUFF)
        brace3 = Brace(brace3_line, RIGHT, buff = SMALL_BUFF)
        brace3.rotate(PI/2,axis=RIGHT)
        brace3.shift(np.array([0.5*a,1.6*a,0]))
        brace1_text = brace1.get_text("$a$")
        brace2_text = brace2.get_text("$a$")
        brace3_text = brace3.get_text("$a$")
        brace1_text.set_color(RED)
        brace2_text.set_color(RED)
        brace3_text.set_color(RED)
        brace1_text.rotate(PI/2)
        brace2_text.rotate(PI/2)
        brace3_text.rotate(PI/2,axis=RIGHT)
        face_diagonal_text = TexMobject("\\sqrt{","a","^2","+","a","^2","}","=","\\sqrt{2}","a",".")
        face_diagonal_text.rotate(PI/4)
        face_diagonal_text.scale(0.6)
        face_diagonal_text.shift(np.array([0.3,-0.3,-a/2]))
        face_diagonal_text[2].set_color(RED)
        face_diagonal_text[5].set_color(RED)
        face_diagonal_text[10].set_color(RED)
        cube_diagonal_text = TexMobject("\\sqrt{(","\\sqrt{2}","a",")","^2","+","a","^2","}","=","\\sqrt{3}","a")
        cube_diagonal_text.scale(0.6)
        cube_diagonal_text[2].set_color(RED)
        cube_diagonal_text[6].set_color(RED)
        cube_diagonal_text[11].set_color(RED)
        cube_diagonal_text.rotate(35*DEGREES)
        cube_diagonal_text.rotate(PI/2, axis=RIGHT)
        cube_diagonal_text.rotate(45*DEGREES)
        cube_diagonal_text.shift([-0.2,0.2,0.2])

        self.play(
            GrowFromCenter(brace1),
            GrowFromCenter(brace2),
            FadeInFrom(brace1_text, direction = UP),
            FadeInFrom(brace2_text, direction = UP), run_time = 2
        )
        self.wait(2)
        self.play(ShowCreation(face_diagonal), run_time = 2)
        self.play(
            Write(face_diagonal_text[0:7]),
            Write(face_diagonal_text[7:11]), run_time = 2
        )
        self.move_camera(phi=70*DEGREES, theta=-55*DEGREES,distance=8,run_time=2)
        self.play(
            GrowFromCenter(brace3),
            FadeInFrom(brace3_text, direction = UP), run_time = 2
        )
        self.play(
            ShowCreation(cube_diagonal), run_time = 3
        )
        self.play(
            Write(cube_diagonal_text[0:9]),
            Write(cube_diagonal_text[9:]), run_time = 2
        )

        #Information
        info1 = TexMobject("\\text{Cube Diagonal Length}","=","\\sqrt{3}","a")
        info1.scale(0.6)
        info1[3].set_color(RED)
        info2 = TextMobject("(in terms of edge length)")
        info2.scale(0.5)

        self.add_fixed_in_frame_mobjects(info1,info2)
        info1.to_edge(LEFT)
        info1.shift(np.array([0,1,0]))
        info2.next_to(info1, DOWN, buff = 0.2)
        info2.align_to(info1, LEFT)
        self.play(
            FadeInFrom(info1, direction = UP),
            FadeInFrom(info2, direction = UP), run_time = 2
        )
        self.wait(4)
        self.play(
            FadeOut(cube),
            FadeOut(cube_diagonal),
            FadeOut(cube_diagonal_text),
            FadeOut(face_diagonal),
            FadeOut(face_diagonal_text),
            FadeOut(brace1),
            FadeOut(brace1_text),
            FadeOut(brace2),
            FadeOut(brace2_text),
            FadeOut(brace3),
            FadeOut(brace3_text), run_time = 2
        )
        self.wait()

        # Unit Cell Drawing

        a = 1.175 # side length/2
        cube_new = Cube(side_length=2*a, fill_opacity=0.1,stroke_width=0.5)
        # Center Atom
        center_atom = Sphere(checkerboard_colors=[RED_D,RED_E])
        # Corner Atom Portions
                    #      0      1       2       3       4      5       6         7             
        atom_u_min = [     0,     0,      0,      0,   PI/2,  PI/2,   PI/2,     PI/2]
        atom_u_max = [  PI/2,  PI/2,   PI/2,   PI/2,     PI,    PI,     PI,       PI]
        atom_v_min = [     0,  PI/2,     PI, 3*PI/2,      0,  PI/2,     PI,   3*PI/2]
        atom_v_max = [  PI/2,    PI, 3*PI/2,   2*PI,   PI/2,    PI, 3*PI/2,     2*PI]
        atom_tuple = zip(atom_u_min,atom_u_max,atom_v_min,atom_v_max)
        atom_part = [ParametricSurface(
            lambda u,v: np.array(
                            [ np.sin(u)*np.cos(v),
                              np.sin(u)*np.sin(v),
                              np.cos(u)]), u_min = p_min, u_max = p_max, v_min = q_min, v_max = q_max)
                    for p_min,p_max,q_min,q_max in atom_tuple]
        single_atom = VGroup(*atom_part)

        angle0 = [0,PI/2,PI,3*PI/2,0,PI/2,PI,3*PI/2]
        sector_xy_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
        sector_yz_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
        sector_zx_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.3, start_angle=x) for x in angle0]
        sector_xy = VGroup(*sector_xy_array)
        sector_yz = VGroup(*sector_yz_array).rotate(PI/2,axis=UP)
        sector_zx = VGroup(*sector_zx_array).rotate(PI/2,axis=RIGHT)

        atom_portion = [
                            VGroup(single_atom[0],sector_xy_array[0],sector_yz_array[1],sector_zx_array[0]), # 0
                            VGroup(single_atom[1],sector_xy_array[1],sector_yz_array[5],sector_zx_array[1]), # 1
                            VGroup(single_atom[2],sector_xy_array[2],sector_yz_array[2],sector_zx_array[5]), # 2
                            VGroup(single_atom[3],sector_xy_array[3],sector_yz_array[6],sector_zx_array[4]), # 3
                            VGroup(single_atom[4],sector_xy_array[4],sector_yz_array[0],sector_zx_array[3]), # 4
                            VGroup(single_atom[5],sector_xy_array[5],sector_yz_array[4],sector_zx_array[2]), # 5
                            VGroup(single_atom[6],sector_xy_array[6],sector_yz_array[3],sector_zx_array[6]), # 6
                            VGroup(single_atom[7],sector_xy_array[7],sector_yz_array[7],sector_zx_array[7])  # 7
                        ]
        
        unit_cell = VGroup(*atom_portion,center_atom)
                               #         0                   1                       2                   3 
        atom_portion_pos = [np.array([-a,-a,-a]),  np.array([a,-a,-a]),  np.array([a,a,-a]),  np.array([-a, a,-a]),
                              np.array([-a,-a,a]),   np.array([a,-a,a]),   np.array([a,a,a]),   np.array([-a,a,a])]
                              #         4                   5                       6                   7
        for i in range(8):
            atom_portion[i].shift(atom_portion_pos[i])

        self.add(cube_new)
        self.add(unit_cell)
        self.wait(2)
        
        self.play(*[FadeOut(atom_portion[i]) for i in [1,2,3,4,5,7]])
        self.play(
            ApplyMethod(center_atom.set_opacity, 0.5), run_time =2
        )
        a = 1.175 # side length/2
        cube_diagonal_new = DashedLine(np.array([-a,-a,-a]), np.array([a,a,a]), dash_length=0.1)
        cube_diagonal_new.set_color(YELLOW)
        
        self.play(
            ShowCreation(cube_diagonal_new), run_time = 2
        )
        
        brace_new = Brace(cube_diagonal_new, DR, buff = 0.5)
        brace_new.rotate(7*DEGREES)
        brace_new.rotate(52.5*DEGREES, axis=RIGHT)
        brace_new.scale(1.15)
        brace_new_text = brace_new.get_text("$4$","$R$")
        brace_new_text.shift(np.array([0.5,-0.5,0.5]))
        brace_new_text[1].set_color(BLUE)
        brace_new_text.rotate(PI/2, axis = RIGHT)
        brace_new_text.rotate(31*DEGREES)
        
        self.play(
            GrowFromCenter(brace_new),
            FadeInFrom(brace_new_text, direction = UP), run_time = 2
        )

        # Information
        info3 = TexMobject("\\text{Cube Diagonal Length}","=","4","R")
        info3.scale(0.6)
        info3[3].set_color(BLUE)
        info4 = TextMobject("(in terms of radius of an atom)")
        info4.scale(0.5)
        self.add_fixed_in_frame_mobjects(info3,info4)
        info3.next_to(info1, DOWN, buff = 1)
        info3.align_to(info1, LEFT)
        info4.next_to(info3, DOWN, buff = 0.2)
        info4.align_to(info1, LEFT)
        
        self.play(
            FadeInFrom(info3, direction = DOWN),
            FadeInFrom(info4, direction = DOWN), run_time = 2
        )
        self.wait(2)
        self.play(
            FadeOut(center_atom),
            FadeOut(atom_portion[0]),
            FadeOut(atom_portion[6]),
            FadeOut(cube_new),
            FadeOut(cube_diagonal_new),
            FadeOut(brace_new),
            FadeOut(brace_new_text), run_time = 3
        )

        info13 = VGroup(info1,info3)
        self.add_fixed_in_frame_mobjects(info13)
        brace = Brace(info13,RIGHT, buff = SMALL_BUFF)
        relation1 = TexMobject("\\sqrt{3}","a","=","4","R","\\Rightarrow")
        relation2 = TexMobject("a","=","\\frac{4}{","\\sqrt{3}}","R")
        relation1[1].set_color(RED)
        relation1[4].set_color(BLUE)
        relation2[0].set_color(RED)
        relation2[4].set_color(BLUE)
        self.add_fixed_in_frame_mobjects(brace)
        self.play(
            GrowFromCenter(brace), run_time = 2
        )
        self.add_fixed_in_frame_mobjects(relation1)
        relation1.next_to(brace, RIGHT, buff = 0.3)
        self.play(
            FadeInFrom(relation1, direction=LEFT), run_time = 2
        )
        self.add_fixed_in_frame_mobjects(relation2)
        relation2.next_to(relation1, RIGHT, buff=SMALL_BUFF)
        relation2.shift(np.array([0,-0.1,0]))
        self.play(
            FadeInFrom(relation2, direction=UP), run_time = 2
        )
        box = SurroundingRectangle(relation2, buff = SMALL_BUFF)
        box.set_color(WHITE)
        self.add_fixed_in_frame_mobjects(box)
        self.play(
            ShowCreation(box), run_time = 2
        )
        self.wait(3)
        relation = VGroup(relation2,box)
        self.add_fixed_in_frame_mobjects(relation)
        self.play(
            relation.to_edge, RIGHT, run_time = 3
        )
        self.play(
            FadeOut(info1),
            FadeOut(info2),
            FadeOut(info3),
            FadeOut(info4),
            FadeOut(brace),
            FadeOut(relation1),
            FadeOut(title),
            FadeOut(cpd), run_time = 2
        )
        
        self.wait(5)

#       #       #       #       #       #       #       #       #       #

class BCCScene5(Scene):
    def construct(self):
        relation1 = TexMobject("a","=","\\frac{4}{\\sqrt{3}}","R")
        relation1[0].set_color(RED)
        relation1[3].set_color(BLUE)
        box = SurroundingRectangle(relation1, buff = SMALL_BUFF)
        box.set_color(WHITE)
        relation = VGroup(box,relation1)
        relation.to_edge(RIGHT)
        self.add(relation)

        #Title
        title = TextMobject("Atomic Packing Factor")
        title.to_edge(UP)
        title.set_color_by_gradient(STRAPE_C,STRAPE_E)
        self.play(
            FadeInFrom(title, direction = DOWN), run_time = 2
        )

        # Formula and Calculation
        line1 = TexMobject("\\text{APF}","={\\text{Volume of atoms in a Unit Cell}\\over \\text{Volume of Unit Cell}}")
        line2 = TexMobject("={\\text{Number of atoms}\\times \\text{Volume of a single atom}\\over \\text{Volume of Unit Cell}}")
        line3 = TexMobject("=","{2","\\times","\\frac{4}{3}","\\pi","R","^3","\\over","\\left(","a","\\right)","^3}")
        line3_new = TexMobject("=","{2","\\times","\\frac{4}{3}","\\pi","R","^3","\\over","\\left(","\\frac{4}{\\sqrt{3}}","R","\\right)","^3}")
        line4 = TexMobject("=","\\frac{2\\sqrt{3}}{16}\\pi")
        line5 = TexMobject("\\approx","0.68")
        line3[5].set_color(BLUE)
        line3[9].set_color(RED)
        line3_new[5].set_color(BLUE)
        line3_new[10].set_color(BLUE)

        line1.next_to(title, DOWN, buff = 0.5)
        line1.shift(np.array([-4,2,0]))
        line1.shift(np.array([0,-1,0]))
        line2.next_to(line1, DOWN, buff = 0.5)
        line2.align_to(line1[1], LEFT)
        line3.next_to(line2, DOWN, buff = 0.5)
        line3.align_to(line2, LEFT)
        line3_new.next_to(line3, DOWN, buff = 0.5)
        line3_new.align_to(line3, LEFT)
        line4.next_to(line3_new, DOWN, buff = 0.5)
        line4.align_to(line3_new, LEFT)
        line5.next_to(line4, RIGHT, buff = 0.5)
        line = VGroup(line1,line2,line3,line3_new,line4,line5)
        line.scale(0.7)

        for i in [line1,line2,line3]:
            self.play(
                FadeInFrom(i, direction=DOWN), run_time = 2
            )
            self.wait()
        self.play(
            FadeInFrom(line3_new[0:8], direction=DOWN), run_time = 2
        )
        rel = VGroup(relation1[2],relation1[3])
        self.play(
            ReplacementTransform(rel.copy(),line3_new[8:]), run_time = 2
        )
        
        for i in [line4,line5]:
            self.play(
                FadeInFrom(i, direction=LEFT), run_time = 2
            )
            self.wait()
        self.wait(8)
        self.play(
            FadeOut(title),
            FadeOut(line),
            FadeOut(relation),
            FadeOut(line3[9]), run_time = 3
        )
        self.wait(3)



        


        