from manimlib.imports import *
import numpy as np 

class SCStructureCN(ThreeDScene): # Coordination Number
    def construct(self):
        # Introduction 
        
        intro = TextMobject("Simple Cubic Crystal Structure")
        intro.set_color_by_gradient(GREEN,BLUE)
        self.play(Write(intro),run_time=3)
        self.wait()
        self.play(FadeOut(intro))
        self.wait(2)

        # Drawing Structure
        
        cube = Cube(fill_opacity=0.5,stroke_width=0.5)
        unit_cube = Cube(side_length=1,fill_color=ORANGE,fill_opacity=0.5) 
        unit_cube.shift(np.array([0.5,0.5,0.5]))
        plane1 = Rectangle(height=2,width=2,stroke_width=0.5)
        plane2,plane3 = plane1.copy().rotate(PI/2,axis=RIGHT),plane1.copy().rotate(PI/2,axis=UP)
        plane = VGroup(plane1,plane2,plane3)
        line1 = Line(np.array([-1,0,0]),np.array([1,0,0]))
        line1.set_stroke(WHITE,0.5)
        line2 = line1.copy().rotate(PI/2)
        line3 = line1.copy().rotate(PI/2,axis=UP)
        line = VGroup(line1,line2,line3)

        self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES)
        #axes = ThreeDAxes()
        #self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(
                    ShowCreation(cube),
                    ShowCreation(plane),
                    ShowCreation(line),run_time=2
                )
        self.wait()
        
        # for not close packed atoms
                      # 0   1   2   3   4   5   6   7   8   9  10  11   12  13  14  15  16  17  18  19
        ncp_atoms_x = [0,   0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  -1, -1, -1, -1, -1, -1, -1, -1]
        ncp_atoms_y = [1,   1, -1, -1,  0,  0,  1, -1,  1,  1, -1, -1,   0,  0,  1, -1,  1,  1, -1, -1]
        ncp_atoms_z = [1,   -1, 1, -1,  1, -1,  0,  0,  1, -1,  1, -1,   1, -1,  0,  0,  1, -1,  1, -1]
        ncp_atoms_pos = zip(ncp_atoms_x,ncp_atoms_y,ncp_atoms_z)
        ncp_atoms_array = [Sphere(radius=0.5,fill_opacity=0.5).shift(np.array([x,y,z]))     
                    for x,y,z in ncp_atoms_pos]
        ncp_atoms = VGroup(*ncp_atoms_array)
        ncp_atoms.set_color(PINK)
       
        # for close packed atoms
                    # 0     1   2   3   4   5   6
        cp_atoms_x = [0,    1,  -1, 0,  0,  0,  0]
        cp_atoms_y = [0,    0,   0, 1, -1,  0,  0]
        cp_atoms_z = [0,    0,   0, 0,  0,  1, -1]
        cp_atoms_pos = zip(cp_atoms_x,cp_atoms_y,cp_atoms_z)
        cp_atoms_array =[Sphere(radius=0.5,fill_opacity=0.5).shift(np.array([x,y,z]))     
                    for x,y,z in cp_atoms_pos]
        cp_atoms = VGroup(*cp_atoms_array)
        cp_atoms.set_color(PINK)
        self.add(cp_atoms)
        self.add(ncp_atoms)
        self.wait(3)
        
        # information regarding simple cubic crystal
       
        info1_1 = TextMobject("Simple Cubic Crystal Structure")
        info1_2 = TextMobject("consist of infinit number of")
        info1_3 = TextMobject("cube shaped unit cells in every direction")
        info1 = VGroup(info1_1,info1_2,info1_3)
        self.add_fixed_in_frame_mobjects(info1)
        info1.scale(0.6)
        info1.to_corner(UR)
        info1_2.next_to(info1_1,DOWN,buff = 0.2)
        info1_3.next_to(info1_2,DOWN,buff = 0.2)
        self.play(Write(info1),run_time = 8)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(info1))
       
        # unit cell separation
       
        self.move_camera(phi=75*DEGREES,theta=90*DEGREES,distance=10,run_time = 2)
        self.play(
            FadeIn(unit_cube), run_time = 2
        )
        unit_cell = VGroup(unit_cube, cp_atoms_array[0],cp_atoms_array[1],cp_atoms_array[5],cp_atoms_array[3],ncp_atoms_array[0],ncp_atoms_array[4],ncp_atoms_array[6],ncp_atoms_array[8])
        unit_cell_highlight = unit_cell.copy()
        self.play(
            ApplyMethod(unit_cell_highlight.shift,np.array([1.5,1.5,1.5])), run_time = 3
        )
        self.wait(3)
        self.begin_ambient_camera_rotation(rate = 0.2)
        
        # information of unit cell

        info2_1 = TextMobject("A unit cell has 8 atoms in each corner")
        self.add_fixed_in_frame_mobjects(info2_1)
        info2_1.to_corner(DOWN)
        self.play(Write(info2_1))
        self.wait(15)
        self.play(FadeOut(info2_1))
        self.play(
            FadeOut(unit_cell_highlight),
            FadeOut(unit_cube), run_time=2
        )
        self.wait(2)
        info2_2 = TextMobject("To simplify the view we consider")
        info2_3 = TextMobject("the atoms to be smaller in size")
        info2_3.next_to(info2_2,DOWN,buff= 0.2)
        info2 = VGroup(info2_2,info2_3)
        info2.scale(0.6)
        self.add_fixed_in_frame_mobjects(info2)
        info2.to_corner(UR)
        self.play(Write(info2), run_time = 3)
        self.remove(cp_atoms)
        self.remove(ncp_atoms)
        self.wait(3)
        for i in range(20):
            ncp_atoms_array[i].scale(0.25)
        for i in range(7):
            cp_atoms_array[i].scale(0.25)
        
        self.add(ncp_atoms)
        self.add(cp_atoms)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(info2))
        self.move_camera(phi=60*DEGREES,theta=-50*DEGREES,distance=5,run_time = 3)
        
        # information about coordination number
       
        info3_1 = TextMobject("Coordination Number")
        info3_1.set_color_by_gradient(RED,BLUE)
        info3_1.scale(0.7)
        info3_2 = TextMobject("The number of closest neighboring atoms")
        info3_3 = TextMobject("to which an atom is bonded")
        
        info3_2.scale(0.6)
        info3_3.scale(0.6)
        info3_2.next_to(info3_1,DOWN,buff = 0.2)
        info3_3.next_to(info3_2,DOWN,buff = 0.2)
        
        info3 = VGroup(info3_1,info3_2,info3_3)
        self.add_fixed_in_frame_mobjects(info3)
        info3.to_corner(UR)
        self.play(
            Write(info3), run_time = 4
        )
        self.wait(3)
        self.play(
            ApplyMethod(cp_atoms.set_color, BLUE),
            ApplyMethod(ncp_atoms.set_opacity,0.1),
            ApplyMethod(cp_atoms[0].set_color, RED),
        )
        self.wait(3)
        self.play(
            FadeOut(info3), run_time = 2
        )
        num = TexMobject("1","2","3","4","5","6")
        num.set_color(YELLOW)
        for i in range(6):
            num[i].move_to(cp_atoms_array[i+1])
            num[i].rotate(PI/2,axis=RIGHT)
            num[i].scale(0.5)
        self.play(
            ApplyMethod(cube.set_opacity,0.1),
            ApplyMethod(plane.set_opacity,0.1),
            ApplyMethod(line.set_opacity,0.1), run_time = 2
        )

        # Count Coordination Number

        for i in range(6):
            self.play(Write(num[i]))
            self.wait()
        cn_num = TextMobject("Coordination Number for SC structure is $6$")
        cn_num.scale(0.8)
        cn_num.set_color(GREEN)
        self.add_fixed_in_frame_mobjects(cn_num)
        cn_num.to_corner(UP)
        self.play(Write(cn_num), run_time = 2)
        self.wait(5)
        self.play(
            FadeOut(cn_num),
            FadeOut(cube),
            FadeOut(plane),
            FadeOut(line),
            FadeOut(cp_atoms),
            FadeOut(ncp_atoms),
            FadeOut(num), run_time = 4
            )
        self.wait(4)

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

class SCStructureAPUC(ThreeDScene):  # Atoms Per Unit Cell
    def construct(self):
        self.set_camera_orientation(phi = 75*DEGREES,theta = 30*DEGREES, distance=10)
        self.begin_ambient_camera_rotation(rate=0.2)
        
        # Unit Cell Drawing

        cube = Cube(fill_opacity=0.5,stroke_width=1.5)
        cube.set_color(WHITE)
                #   0    1   2   3    4   5   6   7
        atoms_x = [ 1,   1,  1,  1,  -1, -1, -1, -1]
        atoms_y = [ 1,   1, -1, -1,   1,  1, -1, -1]
        atoms_z = [ 1,  -1,  1, -1,   1, -1,  1, -1]
        atoms_pos = zip(atoms_x,atoms_y,atoms_z)
        atoms_array = [Sphere().shift(np.array([x,y,z]))       # Use Dot for faster rendering
                        for x,y,z in atoms_pos]
        atoms = VGroup(*atoms_array)
        self.play(
            ShowCreation(cube),
            ShowCreation(atoms), run_time = 5
            )
        self.wait(5)

        # Unit Cell Definition & Lattice Definition 
        
        unit_cell_def_1 = TextMobject("Unit Cell :", " The smallest representative structural unit of lattice")
        unit_cell_def_2 = TextMobject("that can describe the crystal structure")
        unit_cell_def_1.scale(0.6)
        unit_cell_def_2.scale(0.6)
        unit_cell_def = VGroup(unit_cell_def_1,unit_cell_def_2)
        unit_cell_def_1[0].set_color(QUEPAL_E)
        unit_cell_def_2.next_to(unit_cell_def[1], DOWN, buff=0.2)
        unit_cell_def_2.align_to(unit_cell_def[1],LEFT)
        lattice_def = TextMobject("Lattice : ","An array of atoms arranged in 3D grid like pattern")
        lattice_def.scale(0.6)
        lattice_def[0].set_color(QUEPAL_E)

        self.add_fixed_in_frame_mobjects(unit_cell_def)
        unit_cell_def.to_corner(UL)
        self.play(Write(unit_cell_def), run_time = 3)
        self.wait(3)
        self.add_fixed_in_frame_mobjects(lattice_def)
        lattice_def.to_corner(DL)
        self.play(FadeIn(lattice_def))
        self.wait(10)
        self.play(
            FadeOut(unit_cell_def),
            FadeOut(lattice_def), run_time = 2
            ) 
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=65*DEGREES,theta=30*DEGREES,distance=7, run_time = 4)
        
        # Single Atom Portions
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
        sector_xy_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.2, start_angle=x) for x in angle0]
        sector_yz_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.2, start_angle=x) for x in angle0]
        sector_zx_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.2, start_angle=x) for x in angle0]
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
        
        full_atom = VGroup(*atom_portion)
        
        # Cutting Plane

        plane1 = Prism(dimensions=[2.2,2.2,0],fill_color=WHITE,fill_opacity=0.1,stroke_width=0)
        plane2,plane3 = plane1.copy().rotate(PI/2,axis=RIGHT), plane1.copy().rotate(PI/2,axis=UP)
        plane = VGroup(plane1,plane2,plane3)
        self.play(
            FadeOut(atoms),
            FadeOut(cube), run_time = 4
        )
        self.wait(2)
        self.play(FadeIn(full_atom), run_time = 2)
        self.play(ShowCreation(plane),run_time = 3)
        self.wait(2)
    
        # Informations 

        info1 = TextMobject("Corner atoms are divided into 8 equal portions using three plane")
        info1_1 = TextMobject("So each portion is $\\frac{1}{8}$ of an atom")
        info1.scale(0.7)
        info1_1.scale(0.7)
        info2 = TextMobject("Number of atoms per unit cell $=\\frac{1}{8}\\times8$(corner) $=1$")

        self.add_fixed_in_frame_mobjects(info1)
        info1.to_corner(UL)
        self.play(Write(info1), run_time = 5)
        self.play(
            ApplyMethod(atom_portion[0].shift, np.array([1,1,1])), run_time = 4
        )
        self.add_fixed_in_frame_mobjects(info1_1)
        info1_1.to_corner(DL)
        self.play(Write(info1_1), run_time = 5)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(20)
        self.play(
            ApplyMethod(atom_portion[0].shift, np.array([-1,-1,-1])), run_time = 4
        )
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75*DEGREES,theta=30*DEGREES,distance=10, run_time = 4)
        self.play(
            FadeOut(full_atom), 
            FadeOut(plane),
            FadeOut(info1),
            FadeOut(info1_1), run_time = 3
            )
        cube.set_opacity(0)
        cube.set_stroke(WHITE,1.5)
        self.wait(3)
        # Positioning atom portions
                         #      0                           1                       2                   3   
        atom_portion_pos = [np.array([-1,-1,-1]),  np.array([1,-1,-1]),  np.array([1,1,-1]),  np.array([-1, 1,-1]),
                              np.array([-1,-1,1]),   np.array([1,-1,1]),   np.array([1,1,1]),   np.array([-1,1,1])]
                              #         4                   5                       6                   7
        for i in range(8):
            atom_portion[i].shift(atom_portion_pos[i])
        
        self.play(FadeIn(full_atom),run_time = 5) 
        self.wait(3)
        self.add_fixed_in_frame_mobjects(info2)
        info2.to_corner(DL)
        self.begin_ambient_camera_rotation(rate = 0.2)

        self.play(Write(info2), run_time = 8)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.play(
            FadeOut(info2),
            FadeOut(full_atom),
            FadeOut(cube), run_time = 3
        )
        self.wait(5)

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

class SCStructureAPF(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75*DEGREES, theta = 60*DEGREES, distance = 8)

        cube = Cube(fill_opacity=0,stroke_width=1.5)

        # Single Atom Portions
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
        sector_xy_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.2, start_angle=x) for x in angle0]
        sector_yz_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.2, start_angle=x) for x in angle0]
        sector_zx_array = [AnnularSector(inner_radius=0, outer_radius=1, color=BLUE, fill_opacity=0.2, start_angle=x) for x in angle0]
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
        
        full_atom = VGroup(*atom_portion)
       
        atom_portion_pos = [np.array([-1,-1,-1]),  np.array([1,-1,-1]),  np.array([1,1,-1]),  np.array([-1, 1,-1]),
                              np.array([-1,-1,1]),   np.array([1,-1,1]),   np.array([1,1,1]),   np.array([-1,1,1])]
                              #         4                   5                       6                   7
        for i in range(8):
            atom_portion[i].shift(atom_portion_pos[i])
        
        self.play(
            FadeIn(cube),
            FadeIn(full_atom), run_time = 3
        )
        
        #self.add(cube)
        #self.add(full_atom)

        edge_arrow1 = DoubleArrow(np.array([1.5,1.5,-1]),np.array([-1,1.5,-1]))
        edge_arrow2 = DoubleArrow(np.array([-3.4,0.5,-1]),np.array([-3.4,-3,-1]))
        edge_arrow1.rotate(PI/2, axis = RIGHT)
        edge_arrow2.rotate(PI/2,axis = RIGHT)
        a1 = TexMobject("a")
        a2 = a1.copy()
        a1.move_to(np.array([0.5,2,-1]))
        a2.move_to(np.array([-1.7,1,0]))
        a1.rotate(PI)
        a2.rotate(PI)
        a1.rotate(-PI/2, axis=RIGHT)
        a2.rotate(-PI/2, axis=RIGHT)
        a2.rotate(-30*DEGREES)
        
        self.play(
            GrowFromCenter(edge_arrow1),
            GrowFromCenter(edge_arrow2), run_time = 3
        )
        self.play(
            FadeIn(a1), 
            FadeIn(a2), run_time = 2
        )
        radius_arrow1 = Arrow(np.array([0,0,0]),np.array([1.5,0,0]))
        radius_arrow1.set_color(YELLOW)
        radius_arrow1.shift(np.array([-1.2,1,-1]))
        radius_arrow1.rotate(-PI/2, axis = RIGHT)
        radius_arrow1.rotate(-45*DEGREES,about_point=np.array([-1,1,-1]),axis=UP)
        r = TexMobject("R")
        twice_r = TexMobject("=2","R")
        r.set_color(YELLOW)
        twice_r[1].set_color(YELLOW)
        r.scale(0.6)
        r.shift(np.array([-0.8,1,-0.5]))
        r.rotate(-PI)
        r.rotate(-PI/2, axis = RIGHT)
        twice_r.move_to(np.array([-2.6,1.3,0]))
        twice_r.rotate(PI)
        twice_r.rotate(-PI/2, axis=RIGHT)
        twice_r.rotate(-30*DEGREES)
        self.play(
            GrowArrow(radius_arrow1),
            FadeIn(r), run_time = 3
        )
        self.wait(3)
        self.play(
            ReplacementTransform(r.copy(),twice_r), run_time = 3
        )

        edge = TextMobject("$a$ = Edge length of unit cell(cube)")
        radius = TextMobject("$R$"," = Radius of an atom")
        radius[0].set_color(YELLOW)
        cpd1 = TextMobject("$\\bullet$ Close Packed Direction is along")
        cpd2 = TextMobject("  cube edge.")
        cpd1.set_color(WHITE)
        edge.scale(0.7)
        radius.scale(0.7)
        cpd1.scale(0.7)
        cpd2.scale(0.7)
        cpd = VGroup(cpd1,cpd2)
        self.add_fixed_in_frame_mobjects(edge)
        self.add_fixed_in_frame_mobjects(radius)
        self.add_fixed_in_frame_mobjects(cpd)
        edge.to_corner(UR)
        radius.next_to(edge, DOWN, buff = 0.2)
        radius.align_to(edge, LEFT)
        cpd1.next_to(radius, DOWN, buff = 0.4)
        cpd1.align_to(radius, LEFT)
        cpd2.next_to(cpd1, DOWN, buff = 0.2)
        cpd2.align_to(cpd1, LEFT)

        self.play(
            FadeIn(edge),
            FadeIn(radius),
            FadeIn(cpd), run_time = 4
        )
        self.wait(3)
        apf1 = TextMobject("Atomic Packing Factor")
        apf1.set_color_by_gradient(BLUE,GREEN)
        apf2 = TexMobject("={\\text{Volume of atoms in a Unit Cell}\\over \\text{Volume of Unit Cell}}")
        apf3 = TexMobject("={\\text{Number of atoms}\\times \\text{Volume of a single atom}\\over \\text{Volume of Unit Cell}}")
        apf4 = TexMobject("=","{1","\\times","\\frac{4}{3}","\\pi","R","^3","\\over","a^3}")
        apf4_1 = TexMobject("=","{1","\\times","\\frac{4}{3}","\\pi","R","^3","\\over","\\left(2","R","\\right)^3}")
        apf4[5].set_color(YELLOW)
        apf4_1[9].set_color(YELLOW)
        apf4_1[5].set_color(YELLOW)
        apf5 = TexMobject("=","{\\pi","\\over","6}","\\approx","0.52")
        apf = VGroup(apf1,apf2,apf3,apf4,apf4_1,apf5)
        apf.scale(0.6)
        self.add_fixed_in_frame_mobjects(apf1)
        apf1.to_corner(UL)
        apf1.scale(1.2)
        self.play(Write(apf1))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(apf2)
        apf2.next_to(apf1, DOWN, buff = 0.4)
        apf2.align_to(apf1, LEFT)
        self.play(FadeIn(apf2), run_time = 2)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(apf3)
        apf3.next_to(apf2, DOWN, buff = 0.2)
        apf3.align_to(apf2, LEFT)
        self.play(FadeIn(apf3), run_time = 2)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(apf4)
        apf4.next_to(apf3, DOWN, buff = 0.2)
        apf4.align_to(apf3, LEFT)
        self.play(FadeIn(apf4), run_time = 2)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(apf4_1)
        apf4_1.next_to(apf4, DOWN, buff = 0.2)
        apf4_1.align_to(apf4, LEFT)
        self.play(FadeIn(apf4_1), run_time = 2)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(apf5)
        apf5.next_to(apf4_1, DOWN, buff = 0.2)
        apf5.align_to(apf4, LEFT)
        self.play(FadeIn(apf5))
        self.wait(2)
    
        apf7 = TextMobject("Atomic Packing Factor indicates how densely atoms are packed")
        apf7.scale(0.8)
        self.add_fixed_in_frame_mobjects(apf7)
        apf7.to_corner(DL)
        self.play(FadeIn(apf7), run_time = 2)
        self.wait(5)
        
        scene  = VGroup(cube,full_atom,edge,radius_arrow1,radius,edge_arrow1,edge_arrow2,r,a1,a2,twice_r,cpd,apf,apf7)
        self.play(
            FadeOut(scene), run_time = 3
        )
        # Outro
        outro = TextMobject("Thank You For Watching")
        outro.set_color_by_gradient(BLUE,PINK)
        self.add_fixed_in_frame_mobjects(outro)
        self.play(Write(outro), run_time = 3)
        self.play(FadeOut(outro), run_time = 2)
        self.wait(3)

