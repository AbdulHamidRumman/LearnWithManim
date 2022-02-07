from manimlib.imports import *
import numpy as np 

def hexagonalprism(side_length,height,get_vert_coords=None,conn_line=None):
    a = side_length
    h = height/2
    b = np.sqrt(3)
                    #       0           1               2           3           4                   5
    hex_vert_coords =[  
                        [(a,0,h), (a/2,a*b/2,h), (-a/2,a*b/2,h), (-a,0,h), (-a/2,-a*b/2,h), (a/2,-a*b/2,h)],
                        [(a,0,-h), (a/2,a*b/2,-h), (-a/2,a*b/2,-h), (-a,0,-h), (-a/2,-a*b/2,-h), (a/2,-a*b/2,-h)]
                     ] 
    hexagons = [ Polygon(*hex, fill_color=BLUE, fill_opacity=0.2) for hex in hex_vert_coords ]
    # Connector Lines
    line1 = Line(np.array([a,0,h]),np.array([-a,0,h]))
    line2 = Line(np.array([a/2,a*b/2,h]),np.array([-a/2,-a*b/2,h]))
    line3 = Line(np.array([-a/2,a*b/2,h]),np.array([a/2,-a*b/2,h]))
    ln_gp1 = VGroup(line1,line2,line3)
    ln_gp2 = ln_gp1.copy().shift([0,0,-2*h])
    ln_gp = VGroup(ln_gp1,ln_gp2)
    ln_gp.set_color(BLUE)
    
    side_vert_coords = []
    for i in range(6):
        side = [ hex_vert_coords[0][i],hex_vert_coords[1][i],hex_vert_coords[1][(i+1)%6],hex_vert_coords[0][(i+1)%6] ]
        side_vert_coords.append(side)
    side_rect = [ Polygon(*s, fill_color=BLUE, fill_opacity=0.2) for s in side_vert_coords ]
    sides = VGroup(*side_rect)
    if (conn_line):
        hexagonal_prism = VGroup(*hexagons,sides,ln_gp)
    else:
        hexagonal_prism = VGroup(*hexagons,sides)
    
    if(get_vert_coords):
        return (hexagonal_prism,hex_vert_coords[0])
    else:
        return hexagonal_prism

def get_mid_layer_coord(hex_v_c):
    mid_layer_coords = []
    for i in [0,2,4]:
        (x,y,z),(p,q,r) = hex_v_c[i],hex_v_c[i+1]
        mid_layer_coords.append(((x+p)/3,(y+q)/3,0))
    return mid_layer_coords

class Intro(Scene):
    def construct(self):
        intro1 = TextMobject("HCP Crystal Structure")
        intro1.set_color_by_gradient(JSHINE_C,JSHINE_E)
        intro2 = TextMobject("Hexagonal Close Packed Crystal Structure")
        intro2.set_color_by_gradient(FLARE_A,FLARE_E)
        self.play(
            Write(intro1), run_time = 3
        )
        self.play(
            ReplacementTransform(intro1,intro2), run_time = 3
        )
        self.wait(2)
        self.play(
            FadeOutAndShift(intro2, direction=DOWN), run_time = 2
        )
        self.wait()

class Outro(Scene):
    def construct(self):
        outro = TextMobject("Thank You For Watching")
        outro.scale(1.5)
        outro.set_color_by_gradient(RED_E,BLUE_E)
        self.play(
            DrawBorderThenFill(outro), run_time = 6
        )
        self.wait()
        self.play(
            FadeOut(outro), run_time = 4
        ) 
   
class HCPScene1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,theta=-40*DEGREES,distance=15)
        hexagonal_prism,hex_v_coords = hexagonalprism(side_length=1.5,height=2,get_vert_coords=True,conn_line=True)
        # Top Layer
        top_layer = [Sphere(radius=0.75).shift(np.array([x,y,z])) for (x,y,z) in hex_v_coords]
        top_layer.append(Sphere(radius=0.75).shift(np.array([0,0,1])))
        top_layer_atoms = VGroup(*top_layer)
        # Middle Layer
        mid_layer_coords = get_mid_layer_coord(hex_v_coords)
        mid_layer = [Sphere(radius=0.75,checkerboard_colors=[RED_E,RED_A]).shift(np.array([x,y,z])) for (x,y,z) in mid_layer_coords]
        mid_layer_atoms = VGroup(*mid_layer)
        # Bottom Layer
        bott_layer_atoms = top_layer_atoms.copy().shift(np.array([0,0,-2]))
        # Title
        title = TextMobject("HCP Unit Cell")
        title.scale(0.8)
        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)
        self.play(
            FadeIn(title), run_time = 2
        )

        self.play(
            FadeInFrom(bott_layer_atoms, direction=np.array([0,0,-1])), run_time = 3
        )
        self.wait()
        self.play(
            FadeInFrom(mid_layer_atoms, direction=np.array([0,0,0.5])), run_time = 2
        )
        self.wait()
        self.play(
            FadeInFrom(top_layer_atoms, direction=np.array([0,0,1])), run_time = 3
        )
        self.wait(3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.play(
            FadeOut(bott_layer_atoms),
            FadeOut(mid_layer_atoms),
            FadeOut(top_layer_atoms), run_time = 3
        )

class HCPScene2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,theta=-40*DEGREES,distance=15)
        hexagonal_prism,hex_v_coords = hexagonalprism(side_length=2,height=3,get_vert_coords=True,conn_line=True)
        # Top Layer
        top_layer = [Sphere(radius=0.25).shift(np.array([x,y,z])) for (x,y,z) in hex_v_coords]
        top_layer.append(Sphere(radius=0.25).shift(np.array([0,0,1.5])))
        top_layer_atoms = VGroup(*top_layer)
        # Middle Layer
        mid_layer_coords = get_mid_layer_coord(hex_v_coords)
        mid_layer = [Sphere(radius=0.25,checkerboard_colors=[RED_E,RED_A]).shift(np.array([x,y,z])) for (x,y,z) in mid_layer_coords]
        # Connection line in middle layer atoms
        c = []
        for i in [0,1,2]:
            (x,y,z) = mid_layer_coords[i]
            c.append(np.array([x,y,z]))
        l1 = DashedLine(c[0],c[1])
        l2 = DashedLine(c[1],c[2])
        l3 = DashedLine(c[0],c[2])
        l = VGroup(l1,l2,l3)
        l.set_color(BLUE)
        mid_layer_atoms = VGroup(*mid_layer,l)
        # Bottom Layer
        bott_layer_atoms = top_layer_atoms.copy().shift(np.array([0,0,-3]))
        
        # Title
        title = TextMobject("HCP Unit Cell (Lattice)")
        title.scale(0.8)
        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)
        self.add(title)
        self.add(hexagonal_prism)
        self.add(top_layer_atoms)
        self.add(mid_layer_atoms)
        self.add(bott_layer_atoms)
        self.wait(3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.play(
            FadeOut(hexagonal_prism),
            FadeOut(top_layer_atoms),
            FadeOut(bott_layer_atoms),
            FadeOut(mid_layer_atoms), run_time = 3
        )

class HCPScene3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES)
        # Title
        title = TextMobject("Coordination Number")
        title.set_color_by_gradient(ORANGE,PINK)
        self.add_fixed_in_frame_mobjects(title)
        title.scale(0.8)
        title.to_edge(UP)
        self.play(
            Write(title), run_time = 2
        )
        a = 1
        b = np.sqrt(3)
        first_layer = [(a,0,0), (a/2,a*b/2,0), (-a/2,a*b/2,0), (-a,0,0), (-a/2,-a*b/2,0), (a/2,-a*b/2,0)]
        mid_layer = get_mid_layer_coord(first_layer)
        first_layer_atoms = [Sphere(radius=0.5).shift(np.array([x,y,z])) for (x,y,z) in first_layer]
        first_layer_atoms.append(Sphere(radius=0.5))
        mid_layer_atoms_1 = [Sphere(radius=0.5,checkerboard_colors=[RED_A,RED_E]).shift(np.array([x,y,z+0.5])) for (x,y,z) in mid_layer]
        mid_layer_atoms_2 = [Sphere(radius=0.5,checkerboard_colors=[RED_A,RED_E]).shift(np.array([x,y,z-1])) for (x,y,z) in mid_layer]
        f = VGroup(*first_layer_atoms)
        m1 = VGroup(*mid_layer_atoms_1)
        m2 = VGroup(*mid_layer_atoms_2)
        m1.shift(np.array([0,0,1]))
        m2.shift(np.array([0,0,-1]))
        m2.rotate(PI/3)

        # Information
        info1 = TextMobject("A ","single atom is directly connected to")
        info2 = TextMobject("(i). ","6"," corner atoms")
        info2[1].set_color(BLUE)
        info3 = TextMobject("(ii). ","3","+","3","=","6"," middle layer atoms")
        info3[1].set_color(RED)
        info3[3].set_color(RED)
        info3[5].set_color(RED)
        info4 = TextMobject("Coordination Number"," = ","6","+","6"," = ","12")
        info4[2].set_color(BLUE)
        info4[4].set_color(RED)
        info4[6].set_color_by_gradient(BLUE,RED)

        self.wait()
        self.play(
            FadeInFrom(f,direction=np.array([0,0.5,0])),
            FadeInFrom(m1,direction=np.array([0,0.5,0])),
            FadeInFrom(m2,direction=np.array([0,0.5,0])), run_time = 3
        )
        self.wait(3)
        self.add_fixed_in_frame_mobjects(info1)
        info1.scale(0.6)
        info1.to_corner(UR)
        info1.shift(DOWN)
        self.play(FadeIn(info1))
        self.add_fixed_in_frame_mobjects(info2)
        info2.scale(0.6)
        info2.next_to(info1, DOWN, buff = SMALL_BUFF)
        self.play(
            FadeIn(info2),
            first_layer_atoms[6].set_color, GREEN,
            first_layer_atoms[6].set_opacity, 0.5,
            first_layer_atoms[0].shift, np.array([0.5,0,0]),
            first_layer_atoms[1].shift, np.array([0.5,0.5,0]),
            first_layer_atoms[2].shift, np.array([-0.5,0.5,0]),
            first_layer_atoms[3].shift, np.array([-0.5,0,0]),
            first_layer_atoms[4].shift, np.array([-0.5,-0.5,0]),
            first_layer_atoms[5].shift, np.array([0.5,-0.5,0]), run_time = 3  
        )
        self.wait()
        self.play(
            first_layer_atoms[0].shift, np.array([-0.5,0,0]),
            first_layer_atoms[1].shift, np.array([-0.5,-0.5,0]),
            first_layer_atoms[2].shift, np.array([0.5,-0.5,0]),
            first_layer_atoms[3].shift, np.array([0.5,0,0]),
            first_layer_atoms[4].shift, np.array([0.5,0.5,0]),
            first_layer_atoms[5].shift, np.array([-0.5,0.5,0]), run_time = 3  
        )
        self.wait()
        self.add_fixed_in_frame_mobjects(info3)
        info3.scale(0.6)
        info3.next_to(info2, DOWN, buff = SMALL_BUFF)
        info3.align_to(info2, LEFT)
        self.play(
            FadeIn(info3),
            mid_layer_atoms_1[0].shift,np.array([b/4,0.25,0]),
            mid_layer_atoms_1[1].shift,np.array([-b/4,0.25,0]),
            mid_layer_atoms_1[2].shift,np.array([0,-0.5,0]),
            mid_layer_atoms_2[0].shift,np.array([0,0.5,0]),
            mid_layer_atoms_2[1].shift,np.array([-b/4,-0.25,0]),
            mid_layer_atoms_2[2].shift,np.array([b/4,-0.25,0]), run_time = 3  
        )
        self.play(
            mid_layer_atoms_1[0].shift,np.array([-b/4,-0.25,0]),
            mid_layer_atoms_1[1].shift,np.array([b/4,-0.25,0]),
            mid_layer_atoms_1[2].shift,np.array([0,0.5,0]),
            mid_layer_atoms_2[0].shift,np.array([0,-0.5,0]),
            mid_layer_atoms_2[1].shift,np.array([b/4,0.25,0]),
            mid_layer_atoms_2[2].shift,np.array([-b/4,0.25,0]), run_time = 3  
        )
        self.add_fixed_in_frame_mobjects(info4)
        info4.to_edge(DOWN)
        self.play(
            FadeIn(info4), run_time = 2
        )
        self.wait(5)
        self.play(
            FadeOut(title),
            FadeOut(f),
            FadeOut(m1),
            FadeOut(m2),
            FadeOut(info1),
            FadeOut(info2),
            FadeOut(info3),
            FadeOut(info4), run_time = 3
        )
        self.wait(3)

class HCPScene4(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES,theta=45*DEGREES)
        # Title
        title = TextMobject("Corner Atom Division in HCP")
        # Info
        info1 = TexMobject("\\frac{1}{2}","\\text{ of an atom}")
        info2 = TexMobject("\\frac{1}{2}","\\times","\\frac{1}{3}","\\text{ of an atom}")
        info3 = TexMobject("\\frac{1}{6}","\\text{ of an atom}")
        info1.scale(0.7)
        info2.scale(0.7)
        info3.scale(0.7)
        info1.rotate(PI/2,axis=RIGHT)
        info1.flip(LEFT)
        info1.flip(UP)
        info1.rotate(-45*DEGREES)
        info2.rotate(PI/2,axis=RIGHT)
        info2.flip(LEFT)
        info2.flip(UP)
        info2.rotate(-45*DEGREES)
        info3.rotate(PI/2,axis=RIGHT)
        info3.flip(LEFT)
        info3.flip(UP)
        info3.rotate(-45*DEGREES)
        info1.set_color(BLUE)
        info2.set_color(BLUE)
        info3.set_color(BLUE)
        info1.shift(np.array([0,0,2]))
        info2.shift(np.array([0,0,2]))
        info3.shift(np.array([0,0,2]))

        # Corner Atom
            #         0       1       2       3       4       5
        x_min = [     0,      0,      0,   PI/2,   PI/2,   PI/2]
        x_max = [  PI/2,   PI/2,   PI/2,     PI,     PI,     PI]
        y_min = [ -PI/3,   PI/3,     PI,  -PI/3,   PI/3,     PI]
        y_max = [  PI/3,     PI,   2*PI,   PI/3,     PI,   2*PI]
        x_y_tuple = zip(x_min,x_max,y_min,y_max)
        corner_atom_parts = [ParametricSurface(
            lambda u,v: np.array([
                np.sin(u)*np.cos(v),
                np.sin(u)*np.sin(v),
                np.cos(u)
            ]), u_max=p,u_min=q,v_max=r,v_min=s, checkerboard_colors=[GREEN_D,GREEN_E]) for (p,q,r,s) in x_y_tuple]
        corner_atom = VGroup(*corner_atom_parts)
        corner_atom.set_opacity(0.5)
        # Hexagon
        b = np.sqrt(3)
        hex1 = hexagonalprism(side_length=2,height=3)
        hex2,hex3 = hex1.copy().shift(np.array([-3,b,0])), hex1.copy().shift(np.array([-3,-b,0]))
        for h in [hex1,hex2,hex3]:
            h.shift(np.array([2,0,0]))
        
        # Arc
        arc1 = AnnularSector(inner_radius=0,outer_radius=1,start_angle=PI/3,angle=2*PI/3,fill_opacity=0.5,color=GREEN)

        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)
        self.play(
            FadeIn(title),
            ShowCreation(hex1),
            ShowCreation(hex2),
            ShowCreation(hex3), run_time = 3
        )
        self.wait()
        self.play(
            hex1.set_opacity, 0.1,
            hex2.set_opacity, 0.1,
            hex3.set_opacity, 0.1, run_time = 2
        )
        self.play(
            *[ApplyMethod(h.shift,np.array([0,0,-1.5])) for h in [hex1,hex2,hex3]], run_time = 4
        )
        self.play(
            FadeInFrom(corner_atom,direction=UP), run_time = 3
        )
        self.wait()
        self.play(
            FadeIn(info1),
            *[FadeOutAndShift(corner_atom_parts[x],direction=np.array([0,0,1])) for x in [0,1,2]], run_time = 2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(info1,info2),
            FadeOutAndShift(hex1),
            FadeOutAndShift(hex3),
            FadeIn(arc1),
            *[FadeOutAndShift(corner_atom_parts[x]) for x in [3,5]], run_time = 3
        )
        self.wait(2)
        self.play(
            ReplacementTransform(info2,info3)
        )
        self.wait(4)
        self.play(
            FadeOutAndShift(title),
            FadeOutAndShift(info3),
            FadeOutAndShift(arc1),
            FadeOutAndShift(corner_atom_parts[4]),
            FadeOutAndShift(hex2), run_time = 3
        )
        self.wait(5)

class HCPScene5(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES,theta=-30*DEGREES,distance=15)
        hexagonal_prism,hex_v_coords = hexagonalprism(side_length=2,height=3,get_vert_coords=True,conn_line=False)
        hexagonal_prism.set_opacity(0.1)
        
        # Top Layer
        top_layer = [Sphere(radius=0.3).shift(np.array([x,y,z])) for (x,y,z) in hex_v_coords]
        top_layer.append(Sphere(radius=0.3).shift(np.array([0,0,1.5])))
        top_layer_atoms = VGroup(*top_layer)
        # Middle Layer
        mid_layer_coords = get_mid_layer_coord(hex_v_coords)
        mid_layer = [Sphere(radius=0.3,checkerboard_colors=[RED_E,RED_A],fill_opacity=0.5).shift(np.array([x,y,z])) for (x,y,z) in mid_layer_coords]
        mid_layer_atoms = VGroup(*mid_layer)
        # Bottom Layer
        bott_layer = [Sphere(radius=0.3).shift(np.array([x,y,z-3])) for (x,y,z) in hex_v_coords]
        bott_layer.append(Sphere(radius=0.3).shift(np.array([0,0,-1.5])))
        bott_layer_atoms = VGroup(*bott_layer)

        hexagonal_prism.shift(np.array([-2,-1,0]))
        top_layer_atoms.shift(np.array([-2,-1,0]))
        mid_layer_atoms.shift(np.array([-2,-1,0]))
        bott_layer_atoms.shift(np.array([-2,-1,0]))

        # Title
        title = TextMobject("Number of atoms in a Unit Cell")
        title.set_color_by_gradient(BLUE,GREEN)
        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)

        # Information
        info1 = TexMobject("12","\\text{ Corner Atoms }","=","12","\\times","\\frac{1}{6}","=","2")
        info2 = TexMobject("3","\\text{ Midplane Atoms }","=","3","\\times","1","=","3")
        info3 = TexMobject("2","\\text{ Face Center Atoms }","=","2","\\times","\\frac{1}{2}","=","1")
        info4 = TextMobject("\\text{ Total Atoms }","= ","6")
        info1.set_color(BLUE)
        info2.set_color(RED)
        info3.set_color(BLUE)
        info4.set_color_by_gradient(RED,BLUE)
        info2.next_to(info1, DOWN, buff=0.3)
        info2.align_to(info1, np.array([0,0,0]))
        info3.next_to(info2, DOWN, buff=0.3)
        info3.align_to(info2, np.array([0,0,0]))
        info4.next_to(info3, DOWN, buff=0.3)
        info4.align_to(info3, np.array([0,0,0]))
        info = VGroup(info1,info2,info3,info4)
        info.rotate(80*DEGREES, axis=RIGHT)
        info.rotate(60*DEGREES)
        info.shift(np.array([-7,12,-3]))
        info4.shift(np.array([3,-3,1]))
        info4.scale(1.5)

        self.play(
            Write(title), run_time = 2
        )
        self.wait()
        self.play(
            ShowCreation(hexagonal_prism), run_time = 3
        )
        self.play(
            Write(info1),
            *[FadeIn(top_layer[x]) for x in range(6)],
            *[FadeIn(bott_layer[x]) for x in range(6)], run_time = 4
        )
        self.wait(2)
        self.play(
            Write(info2),
            FadeIn(mid_layer_atoms), run_time = 4
        )
        self.wait(2)
        self.play(
            Write(info3),
            FadeIn(top_layer[6]),
            FadeIn(bott_layer[6]), run_time = 4
        )
        self.wait(2)
        self.play(
            FadeIn(info4[:2]), run_time = 2
        )
        total = VGroup(info1[-1],info2[-1],info3[-1])
        self.play(
            ReplacementTransform(total.copy(),info4[2]), run_time = 2
        )
        self.wait(4)
        self.play(
            FadeOut(info),
            FadeOut(title),
            FadeOut(top_layer_atoms),
            FadeOut(mid_layer_atoms),
            FadeOut(bott_layer_atoms),
            FadeOut(hexagonal_prism), run_time = 3
        )
        self.wait(3)

class HCPScene6(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES)
        a = 2
        h = 1.5
        b = np.sqrt(3)
        # Title
        title = TextMobject("Volume of a Unit Cell")
        # Unit Cell
        hexagonal_prism = hexagonalprism(side_length=a,height=2*h)
        hexagonal_prism.set_opacity(0.1)
        hex_vert_coords = [(a,0,h), (a/2,a*b/2,h), (-a/2,a*b/2,h), (-a,0,h), (-a/2,-a*b/2,h), (a/2,-a*b/2,h)]
        hexagon = Polygon(*hex_vert_coords, fill_color=BLUE, fill_opacity=0.5)
        sp1 = Sphere().shift(np.array([a,0,h]))
        sp2 = Sphere().shift(np.array([(a/2),-a*b/2,h]))
        # Side Length, Height, Arrow, Braces, Labels
        l1 = DoubleArrow(np.array([-a/2,-a*b/2,h]),np.array([a/2,-a*b/2,h]),max_tip_length_to_length_ratio=0.1)
        l1.scale(1.4)
        l1.rotate(PI/2,axis=RIGHT)
        l1.set_color(HARVEY)
        lb1 = TexMobject("a","=","2","R")
        lb1.scale(0.7)
        lb1.next_to(l1, np.array([0,0,-2]), buff = 2*SMALL_BUFF)
        lb1.rotate(PI/2, axis = RIGHT)
        lb1.rotate(30*DEGREES)
        lb1[0].set_color(HARVEY)
        lb1[3].set_color(BLUE)
        brace1 = Brace(hexagonal_prism, RIGHT, buff= SMALL_BUFF)
        brace1.rotate(PI/2, axis= RIGHT)
        brace1.shift(np.array([-1,1.8,0]))
        brace1.scale(0.9)
        brace1.set_color(ORANGE)
        lb2 = brace1.get_text("$c$")
        lb2.rotate(PI/2, axis = RIGHT)
        lb2.rotate(45*DEGREES)
        lb2.set_color(ORANGE)
        
        group = VGroup(hexagonal_prism,hexagon,sp1,sp2,l1,lb1,brace1,lb2)
        group.shift(np.array([-2,0,0]))

        # Information
        info1 = TexMobject("\\text{Area of Hexagon}","\\times","\\text{Height}")
        info2 = TexMobject("=","6\\times","\\frac{\\sqrt{3}}{4}","a^2","\\times","c")
        info2[3].set_color(HARVEY)
        info2[5].set_color(ORANGE)
        info2.next_to(info1, DOWN, buff = 0.2)
        info2.align_to(info1, LEFT)
        info3 = TexMobject("=","\\frac{3\\sqrt{3}}{2}","a^2","\\times","c")
        info3[2].set_color(HARVEY)
        info3[4].set_color(ORANGE)
        info3.next_to(info2, DOWN, buff = 0.2)
        info3.align_to(info2, LEFT)
        info4 = TexMobject("=","\\frac{3\\sqrt{3}}{2}","a^3","\\times","\\left(","{c","\\over","a}","\\right)")
        info4[2].set_color(HARVEY)
        info4[5].set_color(ORANGE)
        info4[7].set_color(HARVEY)
        info4.next_to(info2, DOWN, buff = 0.2)
        info4.align_to(info2, LEFT)
        
        info5 = TexMobject("\\text{For ideal case }","c","\\text{ to }","a","\\text{ ratio}","=","\\frac{2\\sqrt{2}}{\\sqrt{3}}")
        info5[1].set_color(ORANGE)
        info5[3].set_color(HARVEY)
        info5.scale(0.7)
        
        info6 = TexMobject("=","\\frac{3\\sqrt{3}}{2}","a^3","\\times","\\frac{2\\sqrt{2}}{\\sqrt{3}}")
        info6[2].set_color(HARVEY)
        info6.next_to(info4, DOWN, buff = 0.2)
        info6.align_to(info4, LEFT)
        info7 = TexMobject("=","3\\sqrt{2}","a^3")
        info7[2].set_color(HARVEY)
        info7.next_to(info4, DOWN, buff = 0.2)
        info7.align_to(info4, LEFT)
        info8 = TexMobject("=","3\\sqrt{2}","\\left(2","R","\\right)^3")
        info8[3].set_color(BLUE)
        info8.next_to(info7, DOWN, buff = 0.2)
        info8.align_to(info7, LEFT)
        info9 = TexMobject("=","24\\sqrt{2}","R^3")
        info9[2].set_color(BLUE)
        info9.next_to(info8, DOWN, buff = 0.2)
        info9.align_to(info8, LEFT)

        info = VGroup(info1,info2,info3,info4,info6,info7,info8,info9)
        info.scale(0.6)
        info.shift(np.array([4,4,1]))
        info.rotate(80*DEGREES, axis = RIGHT)
        info.rotate(45*DEGREES)

        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)
        self.play(
            Write(title), run_time = 2
        )
        self.wait(2)
        self.play(
            ShowCreation(hexagonal_prism), run_time = 3
        )
        self.wait(2)
        self.play(
            FadeIn(hexagon),
            GrowFromCenter(l1),
            GrowFromCenter(brace1),
            FadeInFrom(lb1, direction = np.array([0,0,-1])),
            FadeInFrom(lb2, direction = LEFT), run_time = 2
        )
        self.wait(2)
        self.play(
            Write(info1)
        )
        self.wait(2)
        self.play(
            FadeIn(info2)
        )
        self.wait(2)
        self.play(
            FadeIn(info3)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(info3,info4), run_time = 2
        )
        self.wait(2)
        self.add_fixed_in_frame_mobjects(info5)
        info5.to_edge(DOWN)
        self.play(
            FadeInFrom(info5, direction = DOWN), run_time = 2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(info4.copy(),info6), run_time = 2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(info6,info7), run_time = 2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(info7.copy(),info8), run_time = 2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(info8.copy(),info9), run_time = 2
        )
        self.wait(5)
        self.play(
            *[FadeOut(i) for i in [hexagonal_prism,hexagon,l1,lb1,brace1,lb2,title,info1,info2,info4,info5,info7,info8,info9]], run_time = 3
        )
        self.wait(5)

class HCPScene7(Scene):
    def construct(self):
        # Title
        title = TextMobject("Atomic Packing Factor")
        title.set_color_by_gradient(BLUE,ORANGE)
        title.to_edge(UP)
        # Information
        info1 = TexMobject("\\text{APF }","=","\\frac{\\text{Volume of Atoms}}{\\text{Volume of Unit Cell}}")
        info1.next_to(title, DOWN, buff = 0.5)
        info2 = TexMobject("=","{6\\times\\frac{4}{3}\\pi","R^3","\\over 24\\sqrt{2}","R^3}")
        info2[2].set_color(BLUE)
        info2[4].set_color(BLUE)
        info2.next_to(info1[1], DOWN, buff = 0.7)
        info2.align_to(info1[1], LEFT)
        info3 = TexMobject("=","\\frac{\\pi}{3\\sqrt{2}}")
        info3.next_to(info2, DOWN, buff = 0.5)
        info3.align_to(info2, LEFT)
        info4 = TexMobject("\\approx","0.74")
        info4.next_to(info3, DOWN, buff = 0.5)
        info4.align_to(info3, LEFT)
        info = VGroup(info1,info2,info3,info4)
        info.scale(0.7)

        self.play(
            FadeInFrom(title, direction = UP), run_time = 4
        )
        self.wait()
        self.play(
            Write(info1), run_time = 5
        )
        self.wait()
        self.play(
            FadeInFrom(info2, direction = UP), run_time = 2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(info2.copy(), info3), run_time = 2
        )
        self.wait(2)
        self.play(
            DrawBorderThenFill(info4), run_time = 3
        )
        self.wait(5)
        self.play(
            FadeOut(info),
            FadeOut(title), run_time = 3
        )
        self.wait(5)
        

