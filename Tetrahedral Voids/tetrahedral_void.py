from manimlib import *
from .crystallography import *

class CubicLattice(VGroup):
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

class Intro(Scene):
    def construct(self):
        banner = Tex("L \sum \Delta RN \quad","\sum","\hat{i}t h","\quad","\sum","\Lambda NIM").scale(1.5)
        banner.set_color(BLUE)
        banner[1].rotate(PI/2)
        banner[3].rotate(-PI/2)
        self.play(DrawBorderThenFill(banner),run_time=5)
        self.wait(3)
    
        topic = TexText(r"Tetrahedral Voids",color=GREEN)\
                       .scale(1.5)
        self.play(FadeTransform(banner,topic),run_time=5)
        self.wait(5)

class Scene_1(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera
    }
    def construct(self):
        frame = self.camera.frame
        frame.set_euler_angles(
            theta = -35*DEGREES,
            phi = 70*DEGREES
        )

        text1 = Text("A Tetrahedron is a solid having four plane triangular faces",
                      t2c={'Tetrahedron':BLUE,'four':RED,'triangular':GREEN},
                      font='Lato').scale(0.9)
        text1.fix_in_frame()\
             .to_edge(UP)
        vertices = [[1,0,-0.5],
                    [-0.5,math.sqrt(3)/2,-0.5],
                    [-0.5,-math.sqrt(3)/2,-0.5],
                    [0,0,(math.sqrt(2))-0.5]]          
        # Shifted version of points since original points creates a smaller drawing
        vertices = (1.5*np.array(vertices)).tolist()
        tetra = Tetrahedron(*vertices)
        tetra.set_fill(RED,0.1)\
             .set_stroke(WHITE,0.5,1)
        dots = SGroup(*[Sphere(radius=0.1,color=BLUE,opacity=0.8).move_to(p) 
                        for p in vertices])
        
        self.play(
            ShowCreation(tetra),
            Write(text1),
            FadeIn(dots),
            run_time=3
        )
        self.play(
            Rotate(tetra,TAU,about_point=ORIGIN),
            Rotate(dots,TAU,about_point=ORIGIN),
            run_time=3
        )
        self.wait(3)
        self.play(
            FadeOut(tetra),
            FadeOut(dots),
            run_time=3
        )

        text2 = Text("If we take three atoms of one layer",
                      t2c={"three":BLUE,"one layer":RED},
                      font='Lato').scale(0.8)
        text3 = Text("and one atom of another layer",
                      t2c={"one":BLUE,"another layer":RED},
                      font='Lato').scale(0.8)
        text2.fix_in_frame()
        text3.fix_in_frame()
        text4 = VGroup(text2,text3).arrange(RIGHT,buff=0.1)
        text4.to_edge(UP)
        text5 = Text("We can create a tetrahedron by joining the atom centers",
                      t2c={"tetrahedron":RED},
                      font='Lato').scale(0.8)
        text5.fix_in_frame()\
             .to_edge(DOWN)
        atoms = SGroup(*[Sphere(radius=1.5*0.5*math.sqrt(3),color=BLUE,opacity=0.5)\
                .move_to(p) for p in vertices])
        lines = SGroup(*[Line3D(np.array(p),np.array(tetra.void)) for p in vertices])
        
        self.play(FadeTransform(text1,text2),run_time=2)
        self.play(*[FadeInFromPoint(obj,3*IN) for obj in atoms[:3]],run_time=2)
        self.play(FadeIn(text3),run_time=2)
        self.play(FadeInFromPoint(atoms[3],2*OUT),run_time=2)
        self.play(FadeIn(text5),run_time=2)
        self.play(atoms.animate.set_opacity(0.2),run_time=2)
        self.play(ShowCreation(tetra),run_time=2)
        self.wait(3)

        text6 = Text("The void space inside this tetrahedron is called a tetrahedral void",
                      t2s={"void space":ITALIC,"tetrahedral void":ITALIC},
                      t2w={"void space":BOLD,"tetrahedral void":BOLD},
                      t2c={"void space":GREEN,"tetrahedral void":GREEN},
                      font='Lato').scale(0.8)
        void_sp = Sphere(radius=0.225*1.5*0.5*math.sqrt(3),color=GREEN,opacity=0.6)\
                  .move_to(tetra.void)
        text6.fix_in_frame()\
             .to_edge(DOWN)
        
        self.play(frame.animate.set_theta(-90*DEGREES))
        self.play(frame.animate.set_phi(75*DEGREES))
        self.wait()
        self.play(FadeTransform(text5,text6),run_time=2)
        self.play(GrowFromCenter(void_sp),run_time=3)
        self.wait(6)
        self.play(
            FadeOut(text4),
            FadeOut(text6),
            run_time=2
        )
        self.add(lines)
        self.play(frame.animate.set_theta(70*DEGREES))
        self.play(frame.animate.set_phi(70*DEGREES))
        self.play(frame.animate.set_width(8))
        self.play(
            *[atom.animate.scale(0.1) for atom in atoms],
            void_sp.animate.scale(0.5)
        )
        self.play(atoms.animate.set_opacity(1))

        bt_pl_cent = sum(np.array(v) for v in vertices[:3])/3
        ds_lns = VGroup(*[Line(np.array(v),bt_pl_cent)\
                          .set_stroke(BLUE,3) for v in vertices[:3]])
        ln1 = Line(bt_pl_cent,void_sp.get_center())\
                .set_stroke(BLUE,3)
        ln2 = Line(void_sp.get_center(),np.array(vertices[3]))\
                .set_stroke(RED,3)
        d1 = ln1.get_unit_normal()
        d2 = ln2.get_unit_normal()
        f1 = Tex(r"\frac{1}{4}")\
            .scale(0.5)\
            .move_to(midpoint(bt_pl_cent,void_sp.get_center())-1.8*d1)
        f2 = Tex(r"\frac{3}{4}")\
            .scale(0.5)\
            .move_to(midpoint(void_sp.get_center(),np.array(vertices[3]))-1.8*d1)

        for (tx,norm_dir) in zip([f1,f2],[d1,d2]):
            tx.rotate(90*DEGREES)
            tx.rotate(-90*DEGREES,axis=norm_dir)

        txt7 = VGroup(Text("The void is",t2c={"void":GREEN},font="Lato"),
                      Tex(r"1\over4"),
                      Text("units away from centroid of the bottom plane",font="Lato")).arrange(RIGHT)\
                      .scale(0.7)
        txt7.fix_in_frame()\
            .to_edge(DOWN)
        txt8 = VGroup(Text("Or it is",font="Lato"),
                      Tex(r"\frac{3}{4}"),
                      Text("units away from upper vertex",font="Lato")).arrange(RIGHT)
        txt8.scale(0.7)\
            .fix_in_frame()\
            .to_edge(DOWN)
        txt9 = VGroup(Text("So the void will divide the central axis with a ratio of",font="Lato").scale(0.7),
                      Tex(r"\frac{3}{4}:\frac{1}{4}=3:1").scale(0.7)).arrange(RIGHT)\
                      .fix_in_frame()\
                      .to_edge(DOWN)

        self.play(ShowCreation(ds_lns),run_time=3)
        self.wait()
        self.play(
            ShowCreation(ln1),
            ShowCreation(txt7),
            run_time=3
        )
        self.wait()
        self.play(ln1.copy().animate.shift(-1.5*d1),run_time=2)
        self.wait()
        self.play(FadeIn(f1,shift=-d1),run_time=2)
        self.wait()
        self.play(ReplacementTransform(txt7,txt8),run_time=2)
        self.wait()
        self.play(ln2.copy().animate.shift(-1.5*d2),run_time=2)
        self.wait()
        self.play(FadeIn(f2,shift=-d2),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(txt8,txt9),run_time=2)
        self.wait(5)
        #self.embed()
        

class Scene_2_0(Scene):
    CONFIG = {
        "camera_class":ThreeDCamera
    }
    def construct(self):
        frame = self.camera.frame
        frame.set_euler_angles(
            theta = 120*DEGREES,
            phi = 75*DEGREES
        )

        topic = Text("Tetrahedral Angle",font='Lato')\
                .set_color_by_gradient(GREEN,ORANGE)\
                .fix_in_frame()\
                .to_edge(UP)
        
        self.play(Write(topic), run_time=3)

        cube = CubicLattice(side_length=3).set_fill(BLUE,0.2)
        corners = cube.corners
        atoms = SGroup(*[Sphere(radius=0.2,color=BLUE).move_to(p) for p in corners])
        ax = ThreeDAxes(x_range=[0,3,3],y_range=[0,3,3],z_range=[0,3,3])
        ax.shift(corners[7]-ax.c2p(0,0,0))
        points = A,B,C,D = VGroup(Tex(r"A(1,0,0)").move_to(ax.c2p(3.5,0,-0.3)),
                                  Tex(r"B(0,1,0)").move_to(ax.c2p(0,3.5,-0.3)),
                                  Tex(r"C(0,0,1)").move_to(ax.c2p(0,0,3.5)),
                                  Tex(r"D(1,1,1)").move_to(ax.c2p(2.7,3.5,2.9)))
                        
        for obj in [A,B,C,D]:
            obj.scale(0.7)
            obj.rotate(135*DEGREES)
            obj.rotate(PI/2,axis=UP-RIGHT)
        D.scale(0.7)
        txt1 = Text("Let us consider a cubic lattice of unit length",font="Lato").scale(0.8)\
                .fix_in_frame()\
                .to_edge(DOWN)
        
        self.play(FadeIn(txt1),run_time=2)
        self.wait()
        self.play(
            FadeIn(cube,shift=DOWN),
            FadeIn(atoms,shift=DOWN),run_time=3)

        txt2 = VGroup(Text("Now we construct a tetrahedron using",font="Lato"),
                    Tex("A,B,C,D"),
                    Text("points",font="Lato")).arrange(RIGHT)\
                    .scale(0.8)\
                    .fix_in_frame()\
                    .to_edge(DOWN)
        
        tetra = Tetrahedron(*[corners[i] for i in [0,3,5,6]])\
                .set_fill(RED,0.2)\
                .set_stroke(WHITE,1.5)
        
        self.play(*[atoms[i].animate.set_color(ORANGE)
                    for i in [0,3,5,6]],run_time=2)
        self.wait()
        self.play(FadeIn(points,shift=OUT),run_time=2)
        self.wait(2)
        self.play(FadeTransform(txt1,txt2),run_time=2)
        self.wait()
        self.play(ShowCreation(tetra),run_time=3)

        txt3 = VGroup(Text("The centroid of",font="Lato"),
                    Tex(r"\triangle ABC"),
                    Text("is point",font="Lato"),
                    Tex(r"E")).arrange(RIGHT)\
                        .scale(0.8)\
                        .fix_in_frame()\
                        .to_edge(DOWN)
        centroid = sum([corners[i] for i in [3,5,6]])/3
        E = Tex(r"E").move_to(ax.c2p(0.6,1,1.2))\
            .rotate(135*DEGREES)\
            .rotate(PI/2,axis=UP-RIGHT)
        dash_lns = VGroup(*[DashedLine(corners[i],centroid,dash_length=0.2).set_stroke(WHITE,2)
                            for i in [3,5,6]])
        E_dot = Dot(color=WHITE).move_to(centroid)\
                .rotate(PI/2,axis=UP-RIGHT)
        
        self.play(ShowCreation(dash_lns),run_time=2)
        self.wait()
        self.play(ShowCreation(E_dot))
        self.wait()
        self.play(FadeIn(E))
        self.wait()
        self.play(FadeTransform(txt2,txt3),run_time=2)
        self.wait()

        e1 = VGroup(Text("Coordinate of point",font="Lato"),
                           Tex(r"E:")).arrange(RIGHT)
        e2 = Tex("(","A","+","B","+","C",")","/3")
        e3 = Tex("{\left[","(1,0,0)","+","(0,1,0)","+","(0,0,1)","\\right]","\\over","3}")
        e4 = Tex(r"\frac{1}{3}\times (1,1,1)")
        e5 = Tex(r"\therefore E\equiv",r"\left(\sfrac{1}{3},\sfrac{1}{3},\sfrac{1}{3}\right)")
        calc0 = VGroup(e1,e2,e3,e4,e5)\
                    .arrange_in_grid(n_rows=3,n_cols=1,v_buff=0.3,aligned_edge=LEFT)\
                    .scale(0.7)\
                    .fix_in_frame()\
                    .to_corner(UL)

        self.play(Write(e1),run_time=2)
        self.wait()
        self.play(FadeIn(e2),run_time=2)
        self.wait()
        self.play(TransformMatchingTex(e2.copy(),e3,
                  key_map={"A":"(1,0,0)",
                           "B":"(0,1,0)",
                           "C":"(0,0,1)",
                           "(":r"\left[",
                           ")":r"\right]"}),run_time=2)
        self.wait()
        self.play(FadeTransform(e3.copy(),e4),run_time=2)
        self.wait()
        self.play(FadeTransform(e4.copy(),e5),run_time=2)
        self.wait(3)
        
        E_coord = e5.copy().to_corner(UR)\
                              .shift(0.5*DOWN)
        self.play(
            TransformMatchingTex(e5.copy(),E_coord),
            FadeOut(dash_lns),
            FadeOut(calc0),run_time=3)
        self.wait()

        void = Sphere(radius=0.2,color=GREEN).move_to(tetra.void)
        F = VGroup(Tex(r"F"),Tex(r"\left(\sfrac{1}{2},\sfrac{1}{2},\sfrac{1}{2}\right)"))\
                     .arrange(DOWN)\
                     .scale(0.6)\
                     .rotate(135*DEGREES)\
                     .rotate(PI/2,axis=UP-RIGHT)\
                     .move_to(tetra.void+0.2*OUT)
        txt4 = VGroup(
                    VGroup(Text("Void center",font="Lato"),
                           Tex(r"F"),
                           Text("will divide",font="Lato")).arrange(RIGHT),
                    Tex(r"DE"),
                    Text("line at a ratio of",font="Lato"),
                    Tex(r"3:1")).arrange(RIGHT)\
                    .scale(0.8)\
                    .fix_in_frame()\
                    .to_edge(DOWN)
        DE_line = Line(centroid,corners[0]).set_stroke(WHITE,2)

        self.play(frame.animate.set_theta(95*DEGREES),run_time=2)
        self.play(frame.animate.set_phi(70*DEGREES))
        self.wait()
        self.play(FadeTransform(txt3,txt4),run_time=2)
        self.wait()
        self.play(ShowCreation(DE_line),run_time=2)
        self.wait()
        self.play(ShowCreation(void),run_time=2)
        self.wait()
        self.play(FadeIn(F[0],shift=IN),run_time=2)
        self.wait()
        self.play(frame.animate.set_theta(120*DEGREES))
        self.play(frame.animate.set_phi(75*DEGREES))

        f1 = VGroup(Text("Coordinate of void center",font="Lato"),
                   Tex(r"F:")).arrange(RIGHT)
        f2 = Tex("{3\cdot ","E","+","1\cdot ","D","\over","3+1}")
        f3 = Tex("{3\cdot ","\left(\sfrac{1}{3},\sfrac{1}{3},\sfrac{1}{3}\\right)",
                  "+","1\cdot ","(1,1,1)","\over","4}")
        f4 = Tex("{(1,1,1)","+","(1,1,1)","\over","4}")
        f5 = Tex(r"\frac{1}{4}\times (2,2,2)")
        f6 = Tex(r"\therefore F\equiv \left(\sfrac{1}{2},\sfrac{1}{2},\sfrac{1}{2}\right)")

        calc1 = VGroup(f1,f2,f3,f4,f5,f6)\
                .arrange_in_grid(n_rows=6,n_cols=1,aligned_edge=LEFT)\
                .scale(0.7)\
                .fix_in_frame()\
                .to_corner(UL)
        
        self.play(Write(f1),run_time=2)
        self.wait()
        self.play(FadeIn(f2),run_time=2)
        self.wait()
        self.play(ReplacementTransform(f2[0].copy(),f3[0]),run_time=2)
        self.wait()
        self.play(
            ReplacementTransform(E_coord[1].copy(),f3[1]),
            FadeOut(E_coord),run_time=2)
        self.wait()
        self.play(TransformMatchingTex(f2[2:4].copy(),f3[2:4]),run_time=2)
        self.wait()
        self.play(ReplacementTransform(f2[4].copy(),f3[4]),run_time=2)
        self.wait()
        self.play(TransformMatchingTex(f2[5:].copy(),f3[5:]),run_time=2)
        self.wait()
        self.play(ReplacementTransform(f3[:2].copy(),f4[:1],
                  key_map={"3\cdot \left(\sfrac{1}{3},\sfrac{1}{3},\sfrac{1}{3} \\right)":"(1,1,1)"}),run_time=2)
        self.wait()
        self.play(ReplacementTransform(f3[2].copy(),f4[1]),run_time=2)
        self.wait()
        self.play(ReplacementTransform(f3[3:5].copy(),f4[2],
                  key_map={"1\cdot (1,1,1)":"(1,1,1)"}),run_time=2)
        self.wait()
        self.play(TransformMatchingTex(f3[5:].copy(),f4[3:]),run_time=2)
        self.wait()
        self.play(FadeTransform(f4.copy(),f5),run_time=2)
        self.wait()
        self.play(FadeTransform(f5.copy(),f6),run_time=2)
        self.wait()
        self.play(*[FadeOut(obj) for obj in [tetra,E,E_dot,DE_line]],run_time=2)
        self.wait()
        self.play(*[atoms[i].animate.set_color(BLUE) for i in [0,3,5,6]],run_time=2)
        self.wait()
        self.play(
            FadeIn(F[1],shift=IN),
            F.animate.shift(0.3*OUT),run_time=2)
        self.wait()
        self.play(FadeOut(calc1),run_time=2)
        self.wait()

        txt5 = VGroup(Text("Now we take a closer look at",font="Lato"),
                      Tex(r"\triangle AFB")).arrange(RIGHT)\
                    .scale(0.8)\
                    .fix_in_frame()\
                    .to_edge(DOWN)
        tri = Polyline(tetra.void,corners[3],corners[5],tetra.void)\
            .set_stroke(WHITE,1.5)\
            .set_fill(ORANGE,0.2)
        self.play(FadeTransform(txt4,txt5),run_time=2)
        self.wait()
        self.play(ShowCreation(tri),run_time=2)
        self.wait()
        self.play(
            SGroup(atoms[3],atoms[5],void).copy()\
                  .animate.shift(10*(UP-RIGHT)),
            VGroup(tri,F,A,B).copy()\
                  .animate.shift(10*(UP-RIGHT)),run_time=5
        )
        self.wait(5)
        #self.embed()

class Scene_2_1(Scene):
    def construct(self):
        f = 5   # scale factor
        d = f/math.sqrt(2)
        h = f*0.5
        vert = [d*LEFT,d*RIGHT,h*UP,d*LEFT]
        tri = Polyline(*vert)\
                .set_stroke(WHITE,2)\
                .set_fill(ORANGE,0.3)
        vert_lbs = VGroup(
                Tex(r"A",r"(1,0,0)").move_to(vert[0]+0.8*DOWN),
                Tex(r"B",r"(0,1,0)").move_to(vert[1]+0.8*DOWN),
                Tex(r"F",r"\left(\sfrac{1}{2},\sfrac{1}{2},\sfrac{1}{2}\right)")\
                    .move_to(vert[2]+0.8*UP)
        )
        mpt_lb = Tex(r"G",r"\left(\sfrac{1}{2},\sfrac{1}{2},0\right)")\
                    .move_to(0.8*DOWN)
        atoms = VGroup(*[Circle(radius=0.5)\
                        .set_color(BLUE,0.8)\
                        .move_to(p) for p in vert[:3]])
        atoms[2].scale(0.8)\
                .set_color(GREEN,0.8)
        gp = VGroup(tri,vert_lbs,atoms)
        gp.shift(15*LEFT)

        self.add(gp)
        self.play(gp.animate.shift(15*RIGHT),run_time=2)
        self.wait(2)

        arc = Arc(start_angle=215.265*DEGREES,angle=109.47*DEGREES,arc_center=vert[2],radius=0.8)
        theta = Tex(r"\theta").move_to(vert[2]+1.1*DOWN)
        txt1 = VGroup(Text("The tetrahedral angle is",font="Lato"),
                      Tex(r"\theta")).arrange(RIGHT)\
                      .scale(0.8)\
                      .to_edge(DOWN)

        self.play(FadeIn(txt1),run_time=2)
        self.wait()
        self.play(ShowCreation(arc),run_time=2)
        self.wait()
        self.play(FadeIn(theta),run_time=2)

        txt2 = VGroup(Text("We take the midpoint",font="Lato"),
                      Tex(r"(G)"),
                      Text("of line",font="Lato"),
                      Tex(r"AB"),
                      Text("and join it with",font="Lato"),
                      Tex(r"F")).arrange(RIGHT)\
                      .scale(0.8)\
                      .to_edge(DOWN)
        dot = Dot()
        dash_ln = DashedLine(vert[2],ORIGIN,dash_length=0.3).set_stroke(WHITE,3)
        perp = Polyline(0.3*UP,0.3*(UL),0.3*LEFT).set_stroke(WHITE,3)
        half_theta = VGroup(Tex(r"\theta/2").move_to(vert[2]+1.1*DOWN+0.5*LEFT),
                            Tex(r"\theta/2").move_to(vert[2]+1.1*DOWN+0.5*RIGHT))

        self.play(FadeTransform(txt1,txt2),run_time=2)
        self.wait()
        self.play(ShowCreation(dot),run_time=2)
        self.wait()
        self.play(ReplacementTransform(
            VGroup(vert_lbs[0],vert_lbs[1]).copy(),mpt_lb),
            run_time=2
        )
        self.wait()
        self.play(
            ShowCreation(dash_ln),
            TransformMatchingTex(theta,half_theta),
            run_time=3
        )
        self.play(ShowCreation(perp),run_time=2)
        self.wait()
        self.play(FadeOut(txt2))

        gp.add(arc,mpt_lb,dot,dash_ln,perp,half_theta)

        self.play(gp.animate.shift(2*LEFT),run_time=2)
        self.wait()

        calc1 = VGroup(Tex("\\therefore AG","=","\\sqrt{\\left(1-\\sfrac{1}{2}\\right)^2",
                                    "+","\\left(0-\sfrac{1}{2}\\right)^2",
                                    "+","(0-0)^2}",
                                    "=","\\frac{1}{\\sqrt{2}}"),
                       Tex("\\therefore FG","=","\\sqrt{\\left(\\sfrac{1}{2}-\\sfrac{1}{2}\\right)^2",
                                    "+","\\left(\\sfrac{1}{2}-\sfrac{1}{2}\\right)^2",
                                    "+","\\left(\\sfrac{1}{2}-0\\right)^2}",
                                    "=","\\frac{1}{2}")
                    ).arrange(DOWN)\
                     .scale(0.8)\
                     .next_to(gp,DOWN,buff=0.8)

        calc2 = VGroup(Tex("\\therefore AG","=","\\frac{1}{\\sqrt{2}}"),
                       Tex("\\therefore FG","=","\\frac{1}{2}")).arrange(DOWN)\
                     .scale(0.8)\
                     .next_to(gp,DOWN,buff=0.8)
        
        self.play(Indicate(VGroup(vert_lbs[0],mpt_lb)),run_time=2)
        self.play(Write(calc1[0]),run_time=8)
        self.wait()
        self.play(Indicate(VGroup(vert_lbs[2],mpt_lb)),run_time=2)
        self.play(Write(calc1[1]),run_time=8)
        self.wait()
        self.play(
            TransformMatchingTex(calc1[0],calc2[0]),
            TransformMatchingTex(calc1[1],calc2[1]),
            run_time=3
        )
        self.wait()

        vert_new = [atoms[0].get_center(),atoms[1].get_center(),atoms[2].get_center()]
        mdp = dot.get_center()
        AFG_tri = VGroup(
            Line(vert_new[0],mdp).set_stroke(YELLOW,2),
            dash_ln.copy().set_stroke(YELLOW,2),
            Line(vert_new[2],vert_new[0]).set_stroke(YELLOW,2)  
        )
        calc3 = VGroup(Text("From",font="Lato"),
                       Tex("\\triangle AFG:").set_color(YELLOW))\
                        .arrange(RIGHT)\
                        .scale(0.8)\
                        .to_edge(UP)\
                        .shift(4*RIGHT)
        calc4 = Tex("\\tan\\left(","\\theta/2","\\right)=","{AG","\\over ","FG}")\
                .scale(0.8)\
                .next_to(calc3,DOWN,aligned_edge=LEFT,buff=0.5)
        calc5 = Tex("\\theta/2","=\\tan^{-1}","\\left(","\\frac{AG}{FG}","\\right)")\
                .scale(0.8)\
                .next_to(calc4,DOWN,aligned_edge=LEFT,buff=0.5)
        calc6 = Tex("\\theta","=2\\tan^{-1}","{\\left(",
                    "\\sfrac{1}{\\sqrt{2}}","\\over","\\sfrac{1}{2}",
                    "\\right)}")\
                    .scale(0.8)\
                    .next_to(calc5,DOWN,aligned_edge=LEFT,buff=0.5)
        calc7 = Tex("\\theta=2\\tan^{-1}(\\sqrt{2})")\
                .scale(0.8)\
                .next_to(calc6,DOWN,aligned_edge=LEFT,buff=0.5)
        calc8 = Tex("\\theta=109.47^o")\
                .scale(0.8)\
                .next_to(calc7,DOWN,aligned_edge=LEFT,buff=0.5)
        box = SurroundingRectangle(calc8,buff=0.3).set_stroke(ORANGE,3)
        
        self.play(FadeIn(AFG_tri))
        self.wait()
        self.play(FadeIn(calc3),run_time=2)
        self.wait()
        self.play(FadeIn(calc4[0]),run_time=2)
        self.wait()
        self.play(ReplacementTransform(half_theta[0].copy(),calc4[1]),run_time=2)
        self.wait()
        self.play(FadeIn(calc4[2]))
        self.wait()
        self.play(ReplacementTransform(AFG_tri[0].copy(),calc4[3]),run_time=2)
        self.wait()
        self.play(Write(calc4[4]))
        self.wait()
        self.play(ReplacementTransform(AFG_tri[1].copy(),calc4[5]),run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(calc4.copy(),calc5),run_time=2)
        self.wait()
        self.play(
            TransformMatchingShapes(calc5[:3].copy(),calc6[:3]),
            TransformMatchingShapes(calc5[4].copy(),calc6[6]),
            run_time=2
        )
        self.wait()
        self.play(
            LaggedStart(
                ReplacementTransform(calc2[0][2].copy(),calc6[3]),
                Write(calc6[4]),
                ReplacementTransform(calc2[1][2].copy(),calc6[5]),
                lag_ratio=0.7
            ),run_time=4
        )
        self.wait()
        self.play(TransformMatchingShapes(calc6.copy(),calc7),run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(calc7.copy(),calc8),run_time=2)
        self.play(ShowCreation(box),run_time=2)
        self.play(FlashAround(box),run_time=3)
        self.wait(5)
        #self.embed()
                
class Scene_3_0(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera
    }
    def construct(self):
        frame = self.camera.frame
        frame.set_euler_angles(
            theta = -35*DEGREES,
            phi = 70*DEGREES
        )
        topic = Text("Critical Radius of Tetrahedral Void",font="Lato")\
                .scale(0.7)\
                .fix_in_frame()\
                .to_edge(UP)\
                .set_color_by_gradient(RED,GREEN,BLUE)
        sr2 = math.sqrt(2)        
        ang = math.atan(sr2)
        cube_corners = sr2*np.array([OUT,UP+RIGHT+OUT,UP,RIGHT])
        atoms = SGroup(*[Sphere(radius=1,color=BLUE).move_to(p) for p in cube_corners])
        atoms[0].rotate(-ang,axis=UP-RIGHT,about_point=(UP+RIGHT)/sr2)
        atoms[1].rotate(-ang,axis=UP-RIGHT,about_point=(UP+RIGHT)/sr2)
        vertices = [d.get_center() for d in atoms]
        tetra = Tetrahedron(*vertices)
        tetra.set_fill(RED,0.1)\
             .set_stroke(WHITE,0.5,1)
        void = Sphere(radius=0.225,color=GREEN).move_to(tetra.void)
        lines = SGroup(*[Line3D(np.array(p),np.array(tetra.void)) for p in vertices])
        shd = tetra.void - ORIGIN
        for obj in [tetra,atoms,void,lines]:
            obj.shift(-shd)
        vertices = [d.get_center() for d in atoms]

        self.play(Write(topic),run_time=2)
        self.wait()
        
        txt1 = VGroup(Text("We've seen that tetrahedral void forms",font="Lato"), 
                      Text("inside the space between four atoms",font="Lato"))\
                      .arrange(DOWN)\
                      .scale(0.6)\
                      .fix_in_frame()\
                      .to_edge(DOWN)
              
        self.play(FadeIn(txt1,shift=UP),run_time=2)
        self.wait()
        self.play(
            LaggedStart(
                FadeIn(atoms[0],shift=OUT),
                FadeIn(atoms[2],shift=OUT),
                FadeIn(atoms[3],shift=OUT),
                lag_ratio=0.5,run_time=5
            )
        )
        self.wait()
        self.play(FadeIn(atoms[1],shift=IN),run_time=2)
        self.wait()
        self.play(frame.animate.set_theta(20*DEGREES))
        self.play(frame.animate.set_phi(75*DEGREES))
        self.wait()
        self.play(frame.animate.set_width(12))
        self.wait()
        self.play(ShowCreation(tetra),run_time=2)
        self.play(ShowCreation(lines),run_time=2)
        self.play(GrowFromCenter(void),run_time=3)

        txt2 = Text("Now, we take a closer look",font="Lato")\
                .scale(0.7)\
                .fix_in_frame()\
                .to_edge(DOWN)

        self.play(FadeTransform(txt1,txt2),run_time=2)
        self.wait()
        self.play(frame.animate.set_theta(45*DEGREES),run_time=2)
        self.wait()
        self.play(
            atoms[2].animate.scale(0.1),
            atoms[3].animate.scale(0.1),
            frame.animate.set_theta(-70*DEGREES),
            frame.animate.set_phi(85*DEGREES),
            run_time=3
        )
        self.wait(2)

        tr = Polyline(void.get_center(),vertices[0],vertices[1],void.get_center())\
             .set_stroke(WHITE,1.5)

        self.play(ShowCreation(tr))
        self.wait()
        self.play(Indicate(tr))
        self.wait()
        self.play(FadeOut(txt2))
        self.wait(5)
        #self.embed()

class Scene_3_1(Scene):
    def construct(self):
        topic = Text("Critical Radius of Tetrahedral Void",font="Lato")\
                .scale(0.7)\
                .to_edge(UP)\
                .set_color_by_gradient(RED,GREEN,BLUE)
        
        self.add(topic)
        
        frame = self.camera.frame
        frame.set_width(9)
        d0 = Circle(radius=0.225,color=GREEN)\
            .set_fill(GREEN,0.2)\
            .set_stroke(GREEN,0.5)
        d1 = Circle(radius=1,color=BLUE)\
            .shift(UP*1.225)\
            .set_fill(BLUE,0.2)\
            .set_stroke(BLUE,0.5)
        d2 = d1.copy().rotate(109.47122*DEGREES,about_point=ORIGIN)
        vertices =  [d.get_center() for d in [d0,d1,d2,d0]]  
        poly = Polyline(*vertices)\
            .set_fill(BLUE,0.2)\
            .set_stroke(WHITE,1)

        self.add(poly)
        self.add(d0,d1,d2)

        r_atom = Tex("r_{atom}")\
                .scale(0.4)\
                .set_color(BLUE)\
                .move_to(midpoint(UP*0.225,vertices[1])+0.3*RIGHT)
        r_atom_cp = r_atom.copy().rotate(54.735*DEGREES,about_point=r_atom.get_center())\
                    .move_to(0.3*LEFT+UP)
        r_void = Tex("r_{void}")\
                .scale(0.4)\
                .set_color(GREEN)\
                .move_to(midpoint(ORIGIN,UP*0.225)+0.3*RIGHT)

        self.play(*[ShowCreation(obj) for obj in [r_atom,r_void]],run_time=2)
        self.wait()

        arc0 = AnnularSector(outer_radius=0.225,inner_radius=0,
                             start_angle=PI/2,angle=109.47*DEGREES,color=GREEN)\
                            .set_fill(GREEN,0.2)\
                            .set_stroke(GREEN,0.5)
        arc1 = AnnularSector(outer_radius=1,inner_radius=0,
                            start_angle=234.735*DEGREES,angle=35.265*DEGREES,
                            arc_center=vertices[1],color=BLUE)\
                            .set_fill(BLUE,0.2)\
                            .set_stroke(BLUE,0.5)
        arc2 = AnnularSector(outer_radius=1,inner_radius=0,
                             start_angle=19.47*DEGREES,angle=35.265*DEGREES,
                             arc_center=vertices[2],color=BLUE)\
                            .set_fill(BLUE,0.2)\
                            .set_stroke(BLUE,0.5)
        txt1 = VGroup(Text("We've seen that",font="Lato"),Text("the angle",font="Lato"))\
                .arrange(DOWN)\
                .scale(0.5)
        th = Tex(r"\theta")\
                .scale(0.3)\
                .next_to(ORIGIN,0.255*UL)
        theta,num = label = VGroup(Tex(r"\theta = "),
                                   DecimalNumber(0,unit="^o",num_decimal_place=2))
        label.arrange(0.2*RIGHT)\
             .scale(0.5)
        txt2 = VGroup(txt1,label)\
                .arrange(DOWN)\
                .next_to(ORIGIN,0.1*DOWN+1.2*RIGHT)
        txt3 = Tex(r"\theta = 109.47^o").to_corner(DL)
        val = ValueTracker(0,num_decimal_place=2)
        num.add_updater(lambda obj: obj.set_value(val.get_value()))
        arc = AnnularSector(inner_radius=0,outer_radius=0.225,start_angle=PI/2,angle=val.get_value()*DEGREES)\
              .set_fill(RED,0.2)\
              .set_stroke(RED,1)
        arc.add_updater(
            lambda obj: obj.become(AnnularSector(inner_radius=0,outer_radius=0.225,
                                   start_angle=PI/2,angle=val.get_value()*DEGREES)\
                                    .set_fill(RED,0.4)\
                                    .set_stroke(RED,1))
        )
        grp = VGroup(poly,arc0,arc1,arc2,r_atom,r_atom_cp,r_void,th)

        self.play(frame.animate.set_width(5),run_time=2)
        self.wait()
        self.play(ShowCreation(arc),run_time=2)
        self.play(FadeIn(th),run_time=2)
        self.play(FadeIn(txt2),run_time=2)
        self.play(val.animate.increment_value(109.47),run_time=3)
        self.play(FadeOut(arc),run_time=2)
        self.play(
            LaggedStart(
                ShowCreation(arc0),
                ShowCreation(arc1),
                ReplacementTransform(r_atom.copy(),r_atom_cp),
                ShowCreation(arc2)
            ), lag_ratio=0.5, run_time=6
        )
        self.wait()
        self.play(
            *[FadeOut(obj) for obj in [d0,d1,d2]],
            run_time=3
        )
        self.play(frame.animate.set_width(14.22),run_time=2)
        self.wait()
        self.play(ReplacementTransform(txt2,txt3),run_time=2)
        self.wait()
        self.play(grp.animate.scale(3),run_time=2)
        self.wait()
        self.play(grp.animate.to_edge(LEFT),run_time=2)
        self.wait(2)
        
        txt4 = VGroup(Text("Lets look at",font="Lato"),
                      Tex(r"\triangle ABC"))\
                      .arrange(RIGHT)\
                      .to_edge(DOWN)
        plv = poly.get_vertices()
        A,B,C = plv[0],midpoint(plv[1],plv[2]),plv[1]
        a,b,c = ABC_tri =  VGroup(Line(B,C).set_stroke(WHITE,3),
                                  Line(C,A).set_stroke(WHITE,3),
                                  DashedLine(A,B,dash_length=0.1).set_stroke(WHITE,3))
        a_dir,c_dir = [l.get_unit_vector() for l in [a,c]]
        perp_ln = Polyline(B+0.3*a_dir,B+0.3*(a_dir-c_dir),B-0.3*c_dir).set_stroke(WHITE,3)
        vert_labels = VGroup(Tex(r"A").move_to(A+0.1*DR).scale(0.5),
                             Tex(r"B").move_to(B+0.2*UL).scale(0.5),
                             Tex(r"C").move_to(C+0.2*UP).scale(0.5))
        half_theta = VGroup(Tex(r"\theta/2").move_to(A+0.42*UP+0.22*LEFT).scale(0.5),
                            Tex(r"\theta/2").move_to(A+0.45*LEFT).scale(0.5))
        half_th_lb = Tex(r"\theta/2 = 54.735^o").to_corner(DL)
        
        self.play(FadeIn(vert_labels), run_time=2)
        self.wait()
        self.play(FadeIn(txt4), run_time=2)
        self.wait()
        self.play(ShowCreation(ABC_tri), run_time=3)
        self.wait()
        self.play(ShowCreation(perp_ln), run_time=2)
        self.wait()
        self.play(FadeOut(txt4))
        self.wait()
        self.play(
            ReplacementTransform(th,half_theta),
            ReplacementTransform(txt3,half_th_lb), run_time=2)
        self.wait()

        tcm = {"r_{atom}":BLUE,"r_{void}":GREEN}
        calc0 = VGroup(Text("Using Sine Law at",font="Lato"),
                       Tex(r"\triangle ABC"))\
                        .arrange(RIGHT)\
                        .move_to(C+0.3*DOWN+6*RIGHT)
        calc1 = Tex("{r_{atom}+r_{void}","\\over","\\sin","90^o}",
                    "=","{r_{atom}","\\over","\\sin","\\theta/2}",
                    tex_to_color_map=tcm)\
                    .next_to(calc0,DOWN,buff=0.5)
        calc2 = Tex("{r_{atom}+r_{void}\\over","1}",
                    "=","{r_{atom}\\over\\sin","54.735^o}",
                    tex_to_color_map=tcm)\
                    .next_to(calc0,DOWN,buff=0.5)
        calc3 = Tex("{r_{atom}+r_{void}","\\over r_{atom}}","=","{1","\\over\\sin","54.735^o}",
                    tex_to_color_map=tcm)\
                    .next_to(calc0,0.5*DOWN,buff=0.5)
        calc4 = Tex("1","+","{r_{void}\\over r_{atom}}","=","\\mathrm{cosec}\\hspace{2pt}54.735^o",
                    tex_to_color_map=tcm)\
                    .next_to(calc3,DOWN,buff=0.5)
        calc5 = Tex("{r_{void}\\over r_{atom}}","=","\\mathrm{cosec}\\hspace{2pt}54.735^o","-","1",
                    tex_to_color_map=tcm)\
                    .next_to(calc3,DOWN,buff=0.5)
        calc6 = Tex("\\therefore","{r_{void}\\over r_{atom}}","\\approx 0.225",
                    tex_to_color_map=tcm)\
                    .next_to(calc5,DOWN,buff=0.5)
        box = SurroundingRectangle(calc6,buff=0.3).set_stroke(ORANGE,3)
        

        self.play(Write(calc0), run_time=2)
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(b,r_atom,r_void).copy(),calc1[:4]
            ), run_time=2)
        self.wait()
        self.play(FadeIn(calc1[4]),run_time=2)
        self.wait()
        self.play(ReplacementTransform(perp_ln.copy(),calc1[5]), run_time=2)
        self.wait()
        self.play(FadeIn(calc1[6]), run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(r_atom_cp.copy(),calc1[7:9]), run_time=2)
        self.wait()
        self.play(FadeIn(calc1[9]), run_time=2)
        self.wait()
        self.play(ReplacementTransform(half_theta[0].copy(),calc1[10]), run_time=2)
        self.wait(2)
        self.play(TransformMatchingTex(calc1[:7],calc2[:6]),run_time=2)
        self.wait()
        self.play(TransformMatchingTex(calc1[7:],calc2[6:]),run_time=2)
        self.wait(2)
        self.play(TransformMatchingTex(calc2,calc3),run_time=2)
        self.wait(2)
        self.play(FadeTransform(calc3.copy(),calc4),run_time=2)
        self.wait(2)
        self.play(TransformMatchingTex(calc4,calc5,key_map={"+":"-"}),run_time=2)
        self.wait(2)
        self.play(FadeTransform(calc5.copy(),calc6),run_time=2)
        self.wait()
        self.play(ShowCreation(box),run_time=2)
        self.wait()
        self.play(FlashAround(box),run_time=3)
        self.wait(5)
        #self.embed()

class Outro(Scene):
    def construct(self):
        outro = Text("Thank You For Watching",font="Lato")\
                .set_color_by_gradient(RED,BLUE)

        self.play(GrowFromCenter(outro),run_time=6)
        self.play(FlashAround(outro),run_time=3)
        self.wait(4)
        self.play(FadeOut(outro),run_time=3)
        