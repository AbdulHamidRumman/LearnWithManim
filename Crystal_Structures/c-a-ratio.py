from manimlib.imports import *
import numpy as np

def hp(side_length,height,get_vert_coords=None,conn_line=None):
    a = side_length
    h = height/2
    b = np.sqrt(3)
                    #       0           1               2           3           4                   5
    hex_vert_coords =[  
                        [(a,0,h), (a/2,a*b/2,h), (-a/2,a*b/2,h), (-a,0,h), (-a/2,-a*b/2,h), (a/2,-a*b/2,h)],
                        [(a,0,-h), (a/2,a*b/2,-h), (-a/2,a*b/2,-h), (-a,0,-h), (-a/2,-a*b/2,-h), (a/2,-a*b/2,-h)]
                     ] 
    hexagons = [ Polygon(*hex, fill_color=BLUE, fill_opacity=0.1) for hex in hex_vert_coords ]
    # Connector Lines
    line1 = Line(np.array([a,0,h]),np.array([-a,0,h]),fill_opacity=0.3)
    line2 = Line(np.array([a/2,a*b/2,h]),np.array([-a/2,-a*b/2,h]),fill_opacity=0.3)
    line3 = Line(np.array([-a/2,a*b/2,h]),np.array([a/2,-a*b/2,h]),fill_opacity=0.3)
    ln_gp1 = VGroup(line1,line2,line3)
    ln_gp2 = ln_gp1.copy().shift([0,0,-2*h])
    ln_gp = VGroup(ln_gp1,ln_gp2)
    ln_gp.set_color(BLUE)
    
    side_vert_coords = []
    for i in range(6):
        side = [ hex_vert_coords[0][i],hex_vert_coords[1][i],hex_vert_coords[1][(i+1)%6],hex_vert_coords[0][(i+1)%6] ]
        side_vert_coords.append(side)
    side_rect = [ Polygon(*s, fill_opacity=0.1) for s in side_vert_coords ]
    sides = VGroup(*side_rect)
    if (conn_line):
        hexagonal_prism = VGroup(*hexagons,sides,ln_gp)
    else:
        hexagonal_prism = VGroup(*hexagons,sides)
    
    if(get_vert_coords):
        return (hexagonal_prism,hex_vert_coords)
    else:
        return hexagonal_prism

def mlc(hex_v_c):
    mid_layer_coords = []
    for i in [0,2,4]:
        (x,y,z),(p,q,r) = hex_v_c[i],hex_v_c[i+1]
        mid_layer_coords.append(((x+p)/3,(y+q)/3,0))
    return mid_layer_coords   

#       #       #       #       #       #       #       #
class Scene1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,theta=25*DEGREES,distance=15)
        h_p, h_v_c = hp(side_length=2,height=3,get_vert_coords=True,conn_line=True)
        
        # Text in Fixed frame
        info1 = TextMobject("HCP Unit Cell")
        self.add_fixed_in_frame_mobjects(info1)
        info1.to_edge(UP)
        self.play(Write(info1))
        
        # Top Layer
        tpl = [Sphere(radius=0.25).shift(np.array([x,y,z])) for (x,y,z) in h_v_c[0]]
        tpl.append(Sphere(radius=0.25).shift(np.array([0,0,1.5])))
        tpl_atoms = VGroup(*tpl)
        # Middle Layer
        mdl_co = mlc(h_v_c[0])
        mdl = [Sphere(radius=0.25,checkerboard_colors=[RED_E,RED_A]).shift(np.array([x,y,z])) for (x,y,z) in mdl_co]
        
        # Bottom Layer
        btml_atoms = tpl_atoms.copy().shift(np.array([0,0,-3]))

        # Connection line in middle layer atoms
        line = [DashedLine(mdl_co[i],mdl_co[(i+1)%3]) for i in [0,1,2]]
        l = VGroup(*line)
        l.set_color(BLUE)
        mdl_atoms = VGroup(*mdl,l)

        hcp_unit_cell = VGroup(h_p,tpl_atoms,mdl_atoms,btml_atoms)

        # Tetrahedron
        a,b,c,d = h_v_c[1][0],h_v_c[1][1],np.array([0,0,-1.5]),mdl_co[0]
        tr1 = Polygon(a,b,c,fill_color=WHITE,fill_opacity=0.1)
        tr2 = Polygon(a,b,d,fill_color=WHITE,fill_opacity=0.1)
        tr3 = Polygon(a,c,d,fill_color=WHITE,fill_opacity=0.1)
        tr4 = Polygon(b,c,d,fill_color=WHITE,fill_opacity=0.1)
        tetrahedron = VGroup(tr1,tr2,tr3,tr4)

        # Label
        line1 = Line(a,b)
        brace1 = Brace(line1,np.array([0.1,0.1,0]),buff=0.1)\
                .rotate(-15*DEGREES)\
                .shift(np.array([-0.1,-0.1,0]))
        label1 = brace1.get_text("$a$")\
                .rotate(PI/2,axis=UP)\
                .rotate(PI/2,axis=RIGHT)\
                .rotate(15*DEGREES)\
                .scale(0.8)
        
        brace2 = Brace(h_p, LEFT,buff=0.1)\
                 .rotate(PI/2, axis=RIGHT)\
                 .shift(np.array([1,2,0]))\
                 .rotate(-25*DEGREES)\
                 .scale(0.9)
                 
        label2 = brace2.get_text("$c$")\
                 .rotate(PI/2,axis=UP)\
                 .rotate(PI/2,axis=RIGHT)
                 
        # Centroid of the triangle
        temp = list(mdl_co[0])
        temp[2] = -1.5
        e = tuple(temp)
        h = DashedLine(d,e)
        dot = Dot().shift(e)
        # Height of the tetrahedron
        f = np.array([1,1.8,0])
        ext_line = DashedLine(d,f)
        brace3 = Brace(tetrahedron, LEFT, buff=0.2)\
                 .shift(np.array([1,1,-0.1]))\
                 .rotate(PI/2, axis=RIGHT)\
                 .rotate(-25*DEGREES)\
                 .scale(0.9)
                 
        label3 = brace3.get_text("$\\frac{c}{2}$")\
                 .rotate(PI/2, axis=UP)\
                 .rotate(PI/2, axis=RIGHT)\
                 .shift(np.array([0.2,0.2,-0.1]))
                 
        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait()
        self.play(
            FadeInFrom(hcp_unit_cell, OUT), run_time=2
        )
        self.wait()
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75*DEGREES,theta=25*DEGREES,distance=15)

        self.play(
            GrowFromCenter(brace1),
            Write(label1),
            GrowFromCenter(brace2),
            Write(label2), run_time=3
        )
        self.wait(3)
        
        self.play(
            ApplyMethod(tpl_atoms.set_opacity, 0.05),
            ApplyMethod(h_p.set_opacity, 0.1),
            *[ApplyMethod(mdl_atoms[x].set_opacity, 0.05) for x in [1,2]],
            *[ApplyMethod(btml_atoms[x].set_opacity, 0.05) for x in range(2,6)],
            run_time= 3
        )
        self.wait(2)
        self.play(ShowCreation(tetrahedron), run_time=4)
        self.play(
            ShowCreation(ext_line),
            ShowCreation(h),
            ShowCreation(dot),
            ReplacementTransform(brace2,brace3),
            ReplacementTransform(label2,label3), run_time = 4
        )
        self.wait(3)
        new_tetrahedron = VGroup(ext_line, h, tetrahedron,brace1,brace2,brace3,label1,label2,label3,dot)
        self.play(new_tetrahedron.copy().shift, np.array([0,0,-5]), run_time=3)
        self.wait(3)

#       #       #       #       #       #       #       #
class Scene2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=20*DEGREES,distance=15)
        h_p, h_v_c = hp(side_length=2,height=3,get_vert_coords=True,conn_line=True)
        mdl_co = mlc(h_v_c[0])
        #axes = ThreeDAxes()
        
        # Tetrahedron
        a,b,c,d = h_v_c[1][0],h_v_c[1][1],np.array([0,0,-1.5]),mdl_co[0]
        tr1 = Polygon(a,b,c,fill_color=WHITE,fill_opacity=0.1)
        tr2 = Polygon(a,b,d,fill_color=WHITE,fill_opacity=0.1)
        tr3 = Polygon(a,c,d,fill_color=WHITE,fill_opacity=0.1)
        tr4 = Polygon(b,c,d,fill_color=WHITE,fill_opacity=0.1)
        tetrahedron = VGroup(tr1,tr2,tr3,tr4)

        # Label
        line1 = Line(a,b)
        brace1 = Brace(line1,np.array([0.1,0.1,0]),buff=0.1)\
                .rotate(-15*DEGREES)\
                .shift(np.array([-0.1,-0.1,0]))
        label1 = brace1.get_text("$a$")\
                .rotate(PI/2,axis=UP)\
                .rotate(PI/2,axis=RIGHT)\
                .rotate(15*DEGREES)\
                .scale(0.8)
                 
        # Centroid of the triangle
        temp = list(mdl_co[0])
        temp[2] = -1.5
        e = tuple(temp)
        h = DashedLine(d,e)
        dot = SmallDot().shift(e)
        
        # Height of the tetrahedron
        f = np.array([1,1.8,0])
        ext_line = DashedLine(d,f)
        brace2 = Brace(tetrahedron, LEFT, buff=0.2)\
                 .shift(np.array([1,1,-0.1]))\
                 .rotate(PI/2, axis=RIGHT)\
                 .rotate(-20*DEGREES)\
                 .scale(0.9)
                 
        label2 = brace2.get_text("$\\frac{c}{2}$")\
                 .rotate(PI/2, axis=UP)\
                 .rotate(PI/2, axis=RIGHT)\
                 .shift(np.array([0.2,0.2,-0.1]))
        thd_new = VGroup(ext_line, h, tetrahedron,brace1,brace2,label1,label2,dot)
        thd_new.scale(2)
        thd_new.move_to(np.array([0,0,10]))

        self.play(ApplyMethod(thd_new.move_to, ORIGIN), run_time=3)
        self.wait(3)
        # Side Notes
        txt1 = TextMobject("Let's look at the blue ","Triangle")
        txt1[1].set_color(BLUE)
        self.add_fixed_in_frame_mobjects(txt1)
        txt1.to_edge(DOWN)
        self.play(FadeInFrom(txt1, direction=DOWN), run_time=2)
        self.play(ApplyMethod(tr1.set_opacity, 0.5), run_time=2)
        self.wait()
        tr1_new = VGroup(tr1.copy(),dot.copy())
        self.play(tr1_new.shift, np.array([-3,15,0]), run_time=2)
        self.play(FadeOut(txt1))
        self.wait(4)
        # Goto Scene3
        self.wait(10)
        # Back from Scene3 
        # Lower Triangle Coords
        a,b,c = tr1.get_vertices()
        centroid = (a+b+c)/3
        
        r_line = DashedLine(a,centroid)
        r = TexMobject("r")\
            .shift((a+centroid)/2)\
            .shift(0.3*UP)\
            .shift(0.3*OUT)\
            .rotate(PI/2,axis=UP)\
            .rotate(PI/2,axis=RIGHT)\
            .rotate(15*DEGREES)
        
        self.play(
            ApplyMethod(tr1.set_opacity,0),
            ShowCreation(r_line),
            Write(r), run_time=2
        )
        # Orange Triangle
        tri_org = Polygon(centroid,a,h.get_start())\
              .set_color(ORANGE)\
              .set_opacity(0.3)
        txt2 = TextMobject("Let's look at the orange ","Triangle")
        txt2[1].set_color(ORANGE)
        self.add_fixed_in_frame_mobjects(txt2)
        txt2.to_edge(DOWN)
        self.play(FadeInFrom(txt2, direction=DOWN))
        self.play(ShowCreation(tri_org), run_time=2)
        self.wait()
        # New brace
        a_ln = Line(a,c)
        a_br = Brace(a_ln,buff=SMALL_BUFF)\
                  .rotate(60*DEGREES, axis=UP, about_point=a)\
                  .rotate(-45*DEGREES, about_point=a)\
                  .scale(0.9)\
                  .shift(0.2*DOWN)
                      
        a_lb = a_br.get_text("$a$")\
               .rotate(PI/2, axis=UP)\
               .rotate(PI/2, axis=RIGHT)\
               .rotate(15*DEGREES)\
               .scale(1.5)
        self.play(
            ReplacementTransform(brace1,a_br),
            ReplacementTransform(label1,a_lb), run_time=2
        )
        self.wait()
        tri_new = VGroup(tri_org, a_br,a_lb,brace2,label2,r)
        self.play(tri_new.copy().shift, np.array([-3,15,0]), run_time=5)
        self.play(FadeOut(txt2))
        self.wait(4)

#       #       #       #       #       #       #       #
class Scene3(Scene):
    def construct(self):
        tr = Triangle()\
             .scale(2)\
             .shift(UP*0.2)
        a,b,c = tr.get_vertices()
        dot = Dot()
        # Braces
        br1 = Brace(tr, DOWN, buff=0.2)
        temp_line = Line(b,(b+c)/2)
        br2 = Brace(temp_line, DOWN, buff=0.2)
        lb1 = br1.get_text("$a$")
        lb2 = br2.get_text("$\\frac{a}{2}$")

        triangle = VGroup(tr,dot,br1,lb1)

        # Angle
        arc1 = Arc(arc_center=b, angle=PI/3,radius=0.5)
        arc2 = Arc(arc_center=c, start_angle=2*PI/3,angle=PI/3,radius=0.5)
        arc3 = Arc(arc_center=a, start_angle=4*PI/3,angle=PI/3,radius=0.5)
        arc = Arc(arc_center=b, angle=PI/6,radius=0.5)
        
        ang1 = TexMobject("60^\\circ")\
              .scale(0.7)\
              .next_to(arc1, 0.1*UR, buff=0.1)

        ang2 = TexMobject("30^\\circ")\
              .scale(0.5)\
              .move_to(b)\
              .shift(0.8*RIGHT+0.2*UP)

        #Dashed Lines 
        centroid = dot.get_center()
        ln1 = DashedLine(centroid, (b+c)/2)
        ln2 = DashedLine(centroid, b)
        r = TexMobject("r")\
            .move_to((centroid+b)/2)\
            .shift(0.3*UP+0.05*LEFT)\
            .rotate(PI/6)

        self.play(FadeInFrom(triangle, LEFT), run_time=2)
        self.wait()
        self.play(
            ShowCreation(arc1),
            ShowCreation(arc2),
            ShowCreation(arc3),
            Write(ang1), run_time=2
        )
        self.wait(3)
        self.play(
            ShowCreation(ln1),
            ShowCreation(ln2),
            FadeOut(arc2),
            FadeOut(arc3),
            Write(r),
            *[ReplacementTransform(i,j) for (i,j) in [(arc1,arc),(ang1,ang2),(br1,br2),(lb1,lb2)]],
            run_time=3
        )
        self.wait(2)
        n_tr = VGroup(triangle,ln1,ln2,br2,lb2,ang2,arc,r)
        self.play(n_tr.to_corner, UL, run_time=3)
        self.wait(2)
        # Calculation
        text1 = TexMobject("\\cos{","30^\\circ}","=","{\\frac{a}{2}","\\over r}")\
                .shift(0.5*UP)
        text2 = TexMobject("r","=","{\\frac{a}{2}","\\over \\cos{30^\\circ}}")\
                .next_to(text1, DOWN, buff=0.5)
        text3 = TexMobject("r","=","{\\frac{a}{2}","\\over \\frac{\\sqrt{3}}{2}}}")\
                .next_to(text1, DOWN, buff=0.5)
        text4 = TexMobject("r","=","\\frac{a}{\\sqrt{3}}")\
                .next_to(text1, DOWN, buff=0.5)
        self.play(Write(text1[0]),run_time=2)
        self.wait()
        self.play(
            ReplacementTransform(ang2.copy(), text1[1]),
            Write(text1[2]), run_time=2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(lb2.copy(), text1[3]),
            ReplacementTransform(r.copy(), text1[4]), run_time=2
        )
        self.wait(2)
        self.play(ReplacementTransform(text1.copy(), text2), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(text2, text3), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(text3,text4), run_time=2)
        self.wait()
        # Box
        box = SurroundingRectangle(text4, buff=0.2)
        self.play(ShowCreation(box), run_time=2)
        r_box = VGroup(box, text4)
        self.play(
            ApplyMethod(r_box.next_to, n_tr, DOWN),
            FadeOut(text1), run_time=3
        )
        self.wait(5)
        
#       #       #       #       #       #       #       #

class Scene4(Scene):
    def construct(self):
        txt0 = TexMobject("r","=","\\frac{a}{\\sqrt{3}}")
        box = SurroundingRectangle(txt0, buff=0.2)
        r_box = VGroup(box, txt0)\
                .to_corner(UL)
        self.add(r_box)
        tri = Polygon(ORIGIN, 3*RIGHT, 3*RIGHT+4*UP, fill_opacity=0.1)\
              .set_color(ORANGE)\
              .next_to(r_box, DOWN+0.2*RIGHT)
        x,y,z = tri.get_vertices()
        # Braces
        br1 = Brace(tri, DOWN, buff=SMALL_BUFF)
        br2 = Brace(tri, RIGHT, buff=SMALL_BUFF)
        t_ln = Line(x,x+5*RIGHT)
        br3 = Brace(t_ln, UP, buff=SMALL_BUFF)\
              .rotate(53.13*DEGREES, about_point=x)
        
        # Labels
        lb1 = br1.get_text("$r$")
        lb2 = br2.get_text("$\\frac{c}{2}$")
        lb3 = br3.get_text("$a$")
        triangle = VGroup(tri,br1,br2,br3,lb1,lb2,lb3)
        
        self.play(FadeInFrom(triangle, LEFT))
        self.wait(3)
        # Calculations
        txt1 = TexMobject("a^2","=","r^2","+","\\left(\\frac{c}{2}\\right)^2")\
                .scale(0.8)\
                .to_edge(UP)\
                .shift(2*RIGHT)
        txt2 = TexMobject("a^2","=","\\left(\\frac{a}{\\sqrt{3}}\\right)^2","+","\\left(\\frac{c}{2}\\right)^2")\
                .scale(0.8)\
                .next_to(txt1, DOWN, buff=0.3)
        txt3 = TexMobject("a^2","=","\\frac{a^2}{3}","+","\\frac{c^2}{4}")\
                .scale(0.8)\
                .next_to(txt1, DOWN, buff=0.3)
        txt4 = TexMobject("a^2","-","\\frac{a^2}{3}","=","\\frac{c^2}{4}")\
                .scale(0.8)\
                .next_to(txt1, DOWN, buff=0.3)
        txt5 = TexMobject("\\frac{2}{3}","a^2","=","\\frac{c^2}{4}")\
                .scale(0.8)\
                .next_to(txt4, DOWN, buff=0.3)
        txt6 = TexMobject("\\frac{c^2}{a^2}","=","\\frac{8}{3}")\
                .scale(0.8)\
                .next_to(txt5, DOWN, buff=0.3)
        txt7 = TexMobject("\\frac{c}{a}","=","\\sqrt{\\frac{8}{3}}")\
                .scale(0.8)\
                .next_to(txt5, DOWN, buff=0.3)
        txt8 = TexMobject("\\frac{c}{a}","=","\\frac{2\\sqrt{2}}{\\sqrt{3}}","\\approx","1.63")\
                .scale(0.8)\
                .next_to(txt7, DOWN, buff=0.5)
        
        self.play(
            ReplacementTransform(lb3.copy(), txt1[0]),
            Write(txt1[1])
        )
        self.wait(1.5)
        self.play(
            ReplacementTransform(lb1.copy(), txt1[2]),
            Write(txt1[3])
        )
        self.wait(1.5)
        self.play(ReplacementTransform(lb2.copy(), txt1[4]))
        self.wait(1.5)
        self.play(FadeInFrom(txt2[:2]))
        self.wait(1.5)
        self.play(
            ReplacementTransform(txt0[2].copy(),txt2[2]),
            Write(txt2[3:])
        )
        self.wait(1.5)
        self.play(ReplacementTransform(txt2,txt3))
        self.wait(1.5)
        self.play(ReplacementTransform(txt3[0], txt4[0]))
        self.wait(1.5)
        self.play(
            ReplacementTransform(txt3[1],txt4[3]),
            ReplacementTransform(txt3[2],txt4[1:3]),
            FadeOut(txt3[3])
        )
        self.wait(1.5)
        self.play(ReplacementTransform(txt3[4],txt4[4]))
        self.wait(1.5)
        self.play(FadeInFrom(txt5, direction=UP))
        self.wait(1.5)
        self.play(FadeInFrom(txt6, direction=UP))
        self.wait(1.5)
        self.play(ReplacementTransform(txt6,txt7))
        self.wait(1.5)
        self.play(ReplacementTransform(txt7.copy(), txt8))
        self.wait(1.5)
        
        box2 = SurroundingRectangle(txt8, buff=0.1)\
                .set_color(BLUE)
        
        self.play(ShowCreation(box2), run_time=3)
        self.wait(3)
        self.play(
            FadeOut(triangle),
            FadeOut(r_box),
            FadeOut(box2),
            *[FadeOut(obj) for obj in [txt1,txt4,txt5,txt7,txt8]], run_time=4
        )
        self.wait(3)

#       #       #       #       #       #       #       #

class SideNotes1(Scene):
    def construct(self):
        text1 = TextMobject("In our HCP Crystal Video")\
                .shift(1.5*UP)
        text2 = TextMobject("we used the ","$c$"," to ","$a$"," ratio ","where")\
                .next_to(text1, DOWN, buff=0.4)
        text2[1].set_color(ORANGE)
        text2[3].set_color(BLUE)     
        text3 = TextMobject("$c$ = Height of the Unit Cell")\
                .next_to(text2, DOWN, buff=0.4)\
                .set_color(ORANGE)    
        text4 = TextMobject("$a$ = ","Distance between two")\
                .next_to(text3, DOWN, buff=0.4)\
                .set_color(BLUE)               
        text5 = TextMobject("adjacent atom centers")\
                .next_to(text4[1], DOWN, buff=0.4)\
                .set_color(BLUE)            
        self.play(FadeInFrom(text1,direction=UP))
        self.wait()
        self.play(FadeIn(text2))
        self.wait()
        self.play(FadeIn(text3))
        self.wait()
        self.play(
            FadeIn(text4),
            FadeIn(text5)
        )
        self.wait(3)
        txts = VGroup(text1,text2,text3,text4,text5)
        text6 = TextMobject("In this video we will calculate")\
                .set_color(GREEN)
        text7 = TextMobject("this ratio geometrically")\
                .set_color(GREEN)\
                .next_to(text6,DOWN, buff=0.5)\
                .align_to(text6, LEFT)
        txt = VGroup(text6,text7)
        self.play(ReplacementTransform(txts,txt))
        self.wait(4)

#       #       #       #       #       #       #       #
class SideNotes2(Scene):
    def construct(self):
        text1 = TextMobject("We can create a ","Tetrahedron"," using")\
                .shift(1.5*UP)
        text2 = TextMobject("1 atom from the ","middle plane"," and")\
                .next_to(text1, DOWN, buff=0.5)\
                .align_to(text1, LEFT)
        text3 = TextMobject("3 atoms from the ","top"," or ","bottom plane")\
                .next_to(text2, DOWN, buff=0.5)\
                .align_to(text2, LEFT)
        text4 = TextMobject("Which has the height of ","$\\frac{c}{2}$")
        text4[1].scale(1.2)
        text1[1].set_color(GREEN)
        text2[1].set_color(RED)
        text3[1].set_color(BLUE)
        text3[3].set_color(BLUE)
        txts = VGroup(text1,text2,text3)
        self.play(FadeInFrom(txts, direction=UP))
        self.wait(5)
        self.play(ReplacementTransform(txts, text4))
        self.wait(4)
        self.play(
            FadeOut(txts),
            FadeOut(text4) 
        )

class Outro(Scene):
    def construct(self):
        text0 = TextMobject("Special Thanks to")\
                .shift(1.5*UP)
        text1 = TextMobject("\\textsc{Parisa Najafi}")\
                .next_to(text0, DOWN, buff=0.5)\
                .set_color(RED)
        text2 = TextMobject("from the channel")\
                .next_to(text1, DOWN, buff=0.5)\
                .scale(0.7)
        text3 = TextMobject("Scott Ramsay")\
                .next_to(text2, DOWN, buff=0.5)\
                .set_color(BLUE)
        text4 = TextMobject("(link in the description)")\
                .scale(0.6)\
                .next_to(text3, DOWN, buff=0.3)
        text = VGroup(text0,text1,text2,text3,text4)
        self.play(DrawBorderThenFill(text), run_time=5)
        self.wait(5)
        thanks = TextMobject("\\textsc{Thank You For Watching}")\
                 .set_color_by_gradient(RED,BLUE)
        self.play(ReplacementTransform(text,thanks), run_time=2)
        self.wait(4)
        self.play(FadeOut(thanks))
        self.wait()
