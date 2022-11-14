from .crystallography import *  # Imported Custom class


def coord_to_tex(x,y,z):
    """ Creates Tex object from x, y, z coordinate values """
    return Tex(R"(",F"{x}",R",",F"{y}",R",",F"{z}",R")")

def coord_to_frac_tex(x,y,z):
    """ Creates Tex object in fractions from float values of x, y, z coordinates """
    numx,denx = x.as_integer_ratio()
    numy,deny = y.as_integer_ratio()
    numz,denz = z.as_integer_ratio()
    X = RF"{{{numx} \over {denx}}}" if denx!=1 else RF"{numx}"
    Y = RF"{{{numy} \over {deny}}}" if deny!=1 else RF"{numy}"
    Z = RF"{{{numz} \over {denz}}}" if denz!=1 else RF"{numz}"
    
    return Tex(r"(",X,r",",Y,r",",Z,r")") 

class Intro(Scene):
    def construct(self):
        banner = Tex("L \\sum \\Delta RN \\quad","\\sum","\\hat{i}t h","\\quad","\\sum","\\Lambda NIM").scale(1.5)
        banner.set_color(BLUE)
        banner[1].rotate(PI/2)
        banner[3].rotate(-PI/2)
        self.play(DrawBorderThenFill(banner),run_time=5)
        self.wait(3)
        
        topic = TexText(r"Tetrahedral Voids in BCC Structure",color=GREEN)\
                       .scale(1.5)
        self.play(ReplacementTransform(banner,topic),run_time=3)
        self.wait(5)
        self.play(FadeOut(topic),run_time=3)

class Scene_1(Scene):
    CONFIG = {"camera_class": ThreeDCamera}
    def construct(self):
        frame = self.camera.frame
        frame.reorient(-45,75,0)
        atom_r = 1.5*0.5*math.sqrt(3)
        void_r = 0.225*0.5*math.sqrt(3)

        t1 = VGroup(Text("We've already seen that Tetrahedral Void"),
                    Text("is the empty space surrounded by 4 atoms"))\
                            .scale(0.7)\
                            .arrange(DOWN,buff=0.1)
        
        vertices = [[1,0,-0.5],
                    [-0.5,math.sqrt(3)/2,-0.5],
                    [-0.5,-math.sqrt(3)/2,-0.5],
                    [0,0,(math.sqrt(2))-0.5]]          
        # Shifted version of points since original points creates a smaller drawing
        vertices = (1.5*np.array(vertices)).tolist()
        tetra = Tetrahedron(*vertices)
        tetra.set_fill(RED,0.1)\
             .set_stroke(WHITE,0.5,1)
        void = Sphere(radius=void_r,color=WHITE,opacity=0.6).move_to(tetra.void)
        atoms = SGroup(*[Sphere(radius=atom_r,color=BLUE,opacity=0.5).move_to(p) 
                        for p in vertices])
        lines = SGroup(*[Line3D(np.array(v),np.array(tetra.void)) 
                          for v in vertices]) 
        cube = CubicLattice(side_length=2.5)\
              .shift(1.5*DR+0.5*OUT)\
              .rotate(20*DEGREES,about_point=ORIGIN) 
        cube.set_fill(BLUE,0.2)\
             .set_stroke(WHITE,1.5)
        corner_atoms = SGroup(
            *[Sphere(radius=0.2,color=RED).move_to(p) for p in cube.corners])
        corner_atoms.shift(1.5*DR+0.5*OUT)\
                    .rotate(20*DEGREES,about_point=ORIGIN)
        center_atom = Sphere(radius=0.2,color=GREEN)\
                        .shift(1.5*DR+0.5*OUT)\
                        .rotate(20*DEGREES,about_point=ORIGIN)

        t1.fix_in_frame()\
          .to_edge(DOWN)
        self.play(FadeIn(t1))
        self.wait()
        self.play(ShowCreation(atoms))
        self.wait()
        self.play(ShowCreation(tetra))
        self.wait()
        self.play(*[atom.animate.scale(0.2) for atom in atoms])
        self.wait()
        self.play(ShowCreation(lines))
        self.wait()
        self.play(ShowCreation(void))
        self.wait()
        self.play(FadeOut(t1))

        t2 = VGroup(Text("In this video we will see how Tetrahedral voids"),
                    Text("are created in BCC Lattice",t2c={"BCC Lattice":GREEN}))\
                        .scale(0.7)\
                        .arrange(DOWN,buff=0.1)
        t2.fix_in_frame()\
          .to_edge(DOWN)
        self.play(
            *[obj.animate.shift(2*UL) for obj in [atoms,tetra,lines,void]],
            run_time=3
        )
        self.play(
            *[Rotate(obj,TAU,about_point=void.get_center()) 
              for obj in [atoms,tetra,lines,void]],
            *[FadeIn(obj,OUT) for obj in [cube,center_atom,corner_atoms]],
            Write(t2),run_time=4
        )
        self.wait(5)
        
       

class Scene_2(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera
    }
    def construct(self):
        frame = self.camera.frame
        frame.reorient(-35,75,0)

        topic = Text("Tetrahedral Voids in BCC")\
                    .set_color_by_gradient(BLUE,GREEN)\
                    .fix_in_frame()\
                    .to_edge(UP)

        self.play(FadeIn(topic),run_time=3)
        self.wait()

        cube1 = CubicLattice(side_length=2.5)
        cube1.set_fill(BLUE,0.2)\
             .set_stroke(WHITE,1.5)
        corner_atoms1 = SGroup(*[Sphere(radius=0.2,color=RED).move_to(p) for p in cube1.corners])
        center_atom1 = Sphere(radius=0.2,color=GREEN)

        self.play(
            FadeInFromPoint(cube1,2*IN),
            FadeInFromPoint(corner_atoms1,2*IN),
            FadeInFromPoint(center_atom1,2*IN), run_time=4
        )
        self.wait(2)
        
        cube2 = cube1.copy()
        corner_atoms2 = SGroup(*[Sphere(radius=0.2,color=RED).move_to(p) for p in cube2.corners])
        center_atom2 = center_atom1.copy()

        text0 = Text("Let's take two BCC lattices")\
                .fix_in_frame()\
                .to_edge(DOWN)

        self.play(Write(text0),run_time=2)
        self.play(
            *[obj.animate.shift(RIGHT*1.25) 
              for obj in [cube1,corner_atoms1,center_atom1]],
            *[obj.animate.shift(LEFT*1.25) 
              for obj in [cube2,corner_atoms2,center_atom2]], run_time=2
        )
        self.wait()
        self.play(frame.animate.set_theta(-25*DEGREES),run_time=2)
        self.wait()
        self.play(FadeOut(text0))

        atom_centers = [atom.get_center() for atom in corner_atoms1]
        body_centers = [center_atom1.get_center(),center_atom2.get_center()]
        tetra_verts = [[atom_centers[4],atom_centers[6],body_centers[0],body_centers[1]],
                      [atom_centers[5],atom_centers[7],body_centers[0],body_centers[1]],
                      [atom_centers[6],atom_centers[7],body_centers[0],body_centers[1]],
                      [atom_centers[4],atom_centers[5],body_centers[0],body_centers[1]]]
        
        tetras = [Tetrahedron(*verts)\
                  .set_fill(RED,0.3)\
                  .set_stroke(WHITE,1) for verts in tetra_verts]
        voids = SGroup(*[Sphere(radius=0.1,color=WHITE)\
                        .move_to(tetras[n].void) for n in range(4)])
        face_voids = [voids]
        face_voids.extend(
            [voids.copy().rotate(ang,axis=OUT,about_point=ORIGIN)\
             .shift(d*1.25)
             for (d,ang) in zip([UP,RIGHT,DOWN],[PI/2,PI,3*PI/2])]
        )
        face_voids.extend(
            [voids.copy().rotate(ang,axis=UP,about_point=ORIGIN)\
             .shift(d*1.25)
             for (d,ang) in zip([OUT,IN],[PI/2,3*PI/2])]
        )
        lines = [SGroup(*[Line3D(np.array(v),np.array(tetras[n].void)) 
                          for v in tetra_verts[n]]) 
                 for n in range(4)]
        
        text1 = Text("Tetrahedron can be created by joining the centers of")
        text2 = Text("2 corner atoms and 2 body center atoms",
                      t2c={"2 corner atoms":RED,"2 body center atoms":GREEN})
        text3 = VGroup(text1,text2).arrange(DOWN,buff=0.1)
        text3.fix_in_frame()\
             .to_edge(DOWN)
        text4 = VGroup(Text("Tetrahedral void is shown here using a White Sphere"),
                       Text("which lies on the common face of the two lattices"))\
                        .arrange(DOWN,buff=0.1)\
                        .fix_in_frame()\
                        .to_edge(DOWN)
        
        self.wait()       
        self.play(Write(text3[0]),run_time=3)
        self.play(Write(text3[1],run_time=3))
        self.wait()
        self.play(ShowCreation(tetras[0]))
        self.wait()
        self.play(ShowCreation(lines[0]))
        self.wait()
        self.play(FadeOut(text3,shift=DOWN))
        self.play(ShowCreation(voids[0]),run_time=2)
        self.wait()
        self.play(Write(text4[0]),run_time=3)
        self.play(Write(text4[1]),run_time=3)
        self.wait(2)
        self.play(FadeOut(text4))
        self.wait()
        self.play(
            FadeOut(lines[0]),
            FadeOut(tetras[0]),run_time=2
        )
        self.wait()

        text6 = VGroup(Text("Using different pairs of corner atoms and two body center atoms",
                            t2c={"corner atoms":RED,"body center atoms":GREEN}),
                       Text("tetrahedrons can be formed and voids can be found"))\
                        .arrange(DOWN,buff=0.1)\
                        .fix_in_frame()\
                        .to_edge(DOWN)
        
        self.play(Write(text6[0]),run_time=3)
        self.play(Write(text6[1]),run_time=3)
        self.wait()
        self.play(
            frame.animate.set_phi(85*DEGREES),
            frame.animate.set_theta(-150*DEGREES),
        )
        self.wait()
        self.play(ShowCreation(tetras[3]),run_time=2)
        self.wait()
        self.play(ShowCreation(lines[3]))
        self.wait()
        self.play(ShowCreation(voids[3]))
        self.wait()
        self.play(
            FadeOut(lines[3]),
            FadeOut(tetras[3]), run_time=2
        )
        self.wait()
        self.play(
            frame.animate.set_phi(90*DEGREES),
            frame.animate.set_theta(-25*DEGREES), run_time=2
        )
        self.wait()
        self.play(ShowCreation(tetras[1]),run_time=2)
        self.wait()
        self.play(ShowCreation(lines[1]),run_time=2)
        self.wait()
        self.play(ShowCreation(voids[1]))
        self.wait()
        self.play(
            FadeOut(lines[1]),
            FadeOut(tetras[1]), run_time=2
        )
        self.wait()
        self.play(frame.animate.set_phi(70*DEGREES))
        self.wait()
        self.play(ShowCreation(tetras[2]),run_time=2)
        self.wait()
        self.play(ShowCreation(lines[2]),run_time=2)
        self.wait()
        self.play(ShowCreation(voids[2]))
        self.wait(2)
        self.play(
            FadeOut(lines[2]),
            FadeOut(tetras[2]), run_time=2
        )
        self.wait()
        self.play(FadeOut(text6))
        self.wait()
        self.play(frame.animate.set_theta(-25*DEGREES),run_time=2)
        self.wait()
       
        self.play(
            FadeOut(cube2),
            FadeOut(corner_atoms2),
            FadeOut(center_atom2),
            *[obj.animate.shift(LEFT*1.25) 
              for obj in [cube1,corner_atoms1,center_atom1,voids]], run_time=2
        )
        self.wait()

        text7 = Text("Similarly, each face will have 4 tetrahedral voids")\
                      .fix_in_frame()\
                      .to_edge(DOWN)  
        
        self.play(Write(text7,shift=DOWN),run_time=3)
        self.wait()
        for i in range(1,4):
            self.play(frame.animate.increment_theta(-95*DEGREES),run_time=2)
            self.play(ShowCreation(face_voids[i]))
        self.play(
            ShowCreation(face_voids[4]),
            ShowCreation(face_voids[5]), run_time=2
        )
        self.wait()
        self.play(FadeOut(text7))
        self.play(
            *[Rotate(obj,TAU,about_point=ORIGIN) 
              for obj in [cube1,corner_atoms1,*face_voids]],run_time=20
        )
        self.wait(5)  

class Scene_2_SideNote(Scene):
    def construct(self):
        lines = VGroup(
            TexText("Number of voids"),
            Tex("=","4\\times6(\\text{face})","\\quad","\\text{per 2 unit cell}"),
            Tex("=","24","\\quad","\\text{per 2 unit cell}"),
            Tex("=","\\dfrac{24}{2}","\\quad","\\text{per unit cell}"),
            Tex("=","12","\\quad","\\text{per unit cell}")
        ).arrange_in_grid(5,1,aligned_edge=LEFT)\
         .shift(2*LEFT+0.5*UP)
        self.play(Write(lines[0]),run_time=2)
        for i in range(4):
            self.play(TransformMatchingTex(lines[i].copy(),lines[i+1]),run_time=2)
            self.wait(2)
        self.wait(5)

#   #   #

class Scene_3(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera
    }
    def construct(self):
        frame = self.camera.frame
        frame.reorient(120,75,0)
        
        topic = Text("Lattice Positions of Tetrahedral Voids")\
                    .set_color_by_gradient(RED,GREEN,BLUE)\
                    .fix_in_frame()\
                    .to_edge(UP)
                
        cube = CubicLattice(side_length=3)\
                .set_fill(BLUE,0.2)\
                .set_stroke(WHITE,1.5)
        cube.shift(0.5*DR)
        
        self.play(Write(topic),run_time=2)
        self.wait()
        self.play(FadeIn(cube,shift=OUT),run_time=2)
        self.wait()
        ax = ThreeDAxes(
            x_range = np.array([0,1,0.25]),
            y_range = np.array([0,1,0.25]),
            z_range = np.array([0,1,0.25]),
            height = 3,
            width = 3,
            depth = 3
        )
        ax.shift(cube.get_corner(DL+IN) - ax.c2p(0,0,0))     # Shifting the Origin of the axis to cube corner
        x_lb = Tex("x").rotate(PI/2)\
                    .rotate(PI/2,axis=UP,about_point=ORIGIN)\
                    .rotate(PI/4)\
                    .move_to(ax.c2p(1.1,0,0))
        y_lb = Tex("y").rotate(PI/2)\
                    .rotate(PI/2,axis=UP,about_point=ORIGIN)\
                    .rotate(PI/4)\
                    .move_to(ax.c2p(0,1.1,0))
        z_lb = Tex("z").rotate(PI/2)\
                    .rotate(PI/2,axis=UP,about_point=ORIGIN)\
                    .rotate(PI/4)\
                    .move_to(ax.c2p(0,0,1.1))
        labels = VGroup(x_lb,y_lb,z_lb)
        self.play(ShowCreation(ax),run_time=2)
        self.play(Write(labels),run_time=2)
        self.wait()

        voids_cords = [(0.25,0.5,0),(0.75,0.5,0),(0.5,0.25,0),(0.5,0.75,0),
                       (0.25,0,0.5),(0.75,0,0.5),(0.5,0,0.25),(0.5,0,0.75),
                       (0,0.25,0.5),(0,0.75,0.5),(0,0.5,0.25),(0,0.5,0.75)]
        voids_xy = SGroup(*[Sphere(radius=0.1,color=WHITE).move_to(ax.c2p(x,y,z)) 
                            for (x,y,z) in voids_cords[:4]])
        xy_plane = Square(side_length=3)\
                    .set_fill(BLUE,0.1)\
                    .set_stroke(WHITE,1)
        xy_plane.shift(ax.c2p(0,0,0)-xy_plane.get_corner(DL))
        txt1 = Text("First lets look at the voids of xy-plane")\
              .scale(0.7)\
              .fix_in_frame()\
              .to_edge(DOWN)
        self.play(FadeIn(txt1,shift=UP),run_time=2)
        self.wait()
        self.play(ShowCreation(voids_xy),run_time=2)
        self.wait()
        self.add(xy_plane)
        self.play(
            xy_plane.animate.shift(10*UP),
            voids_xy.animate.shift(10*UP),run_time=3
        )
        self.wait(5)

#   #   #   #

class Scene_4(Scene):
    def construct(self):
        topic = Text("Lattice Positions of Tetrahedral Voids")\
                    .set_color_by_gradient(RED,GREEN,BLUE)\
                    .to_edge(UP)
        sq = Square(side_length=5)\
                .set_fill(BLUE,0.3)\
                .set_stroke(WHITE,2)
        voids_coords = [[0.25,0.5,0],[0.75,0.5,0],[0.5,0.25,0],[0.5,0.75,0]]
        xy_plane = NumberPlane(
            x_range = np.array([0.0,1.0,0.25]),
            y_range = np.array([0.0,1.0,0.25]),
            axis_config = {
                "include_ticks":True
            },
            height = 5,
            width = 5,
            faded_line_ratio=0
        )
        
        clbs = xy_plane.add_coordinate_labels(num_decimal_places = 2)
        x_lbs,y_lbs = clbs[0],clbs[1]
        #self.embed()
        lbs = VGroup(
                xy_plane.get_x_axis_label("x",direction=RIGHT),
                xy_plane.get_y_axis_label("y",direction=UP)
        ).shift(3*LEFT)
        xy_plane.add_updater(lambda m: m.shift(sq.get_corner(DL)-xy_plane.c2p(0,0)))
        voids = VGroup(*[Dot(point=xy_plane.c2p(x,y),color=WHITE)
                         for (x,y,_) in voids_coords])
        
        self.add(topic)
        self.play(
            FadeIn(sq,shift=RIGHT),
            FadeIn(voids,shift=RIGHT),run_time=2
        )
        self.wait()
        self.play(
            sq.animate.shift(3*LEFT),
            voids.animate.shift(3*LEFT),run_time=2
        )
        self.play(
            Write(xy_plane,lag_ratio=0.01),
            Write(lbs,lag_ratio=0.01),
            run_time=3
        )
        
        coords = VGroup(
            *[coord_to_tex(x,y,z) for x,y,z in voids_coords]
        ).arrange(DOWN,buff=1.0)\
         .scale(0.8)\
         .shift(1.5*RIGHT)
        
        h_lines = [xy_plane.get_h_line(voids[i].get_left()).set_color(YELLOW) for i in range(4)]
        v_lines = [xy_plane.get_v_line(voids[i].get_bottom()).set_color(YELLOW) for i in range(4)]

        lbs_idx = [0,2,1,1]
        lbs_idy = [1,1,0,2]
        for i in range(4):
            self.play(voids[i].animate.set_color(YELLOW))
            self.play(
                x_lbs[lbs_idx[i]].animate.set_color(YELLOW),
                y_lbs[lbs_idy[i]].animate.set_color(YELLOW),
                ShowCreation(h_lines[i]),
                ShowCreation(v_lines[i]),run_time=2
            )
            self.wait()
            self.play(*[FadeIn(coords[i][j]) for j in [0,2,4,5,6]],run_time=2)
            self.wait()
            self.play(
                TransformFromCopy(x_lbs[lbs_idx[i]],coords[i][1]),
                TransformFromCopy(y_lbs[lbs_idy[i]],coords[i][3]),run_time=2
            )
            self.wait()
            self.play(
                FadeOut(h_lines[i]),
                FadeOut(v_lines[i]),
                x_lbs[lbs_idx[i]].animate.set_color(WHITE),
                y_lbs[lbs_idy[i]].animate.set_color(WHITE),
                voids[i].animate.set_color(WHITE),run_time=2
            )
        
        r_arrow = Tex("\\Rightarrow")\
                        .scale(1.5)\
                        .next_to(coords,RIGHT,buff=0.5)
        coords_frac = VGroup(
            *[coord_to_frac_tex(x,y,z) for x,y,z in voids_coords]
        ).arrange(DOWN,buff=0.5)\
         .next_to(r_arrow,RIGHT)

        self.play(Write(r_arrow),run_time=2)
        for i in range(4):
            self.play(
                TransformMatchingTex(coords[i].copy(),coords_frac[i])
            )
            self.wait()
        self.wait(3)
        self.play(coords_frac.copy().animate.shift(5*RIGHT))

#   #   #   #   #

class Scene_5(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera
    }
    def construct(self):
        frame = self.camera.frame
        frame.reorient(120,75,0)

        topic = Text("Lattice Positions of Tetrahedral Voids")\
                    .set_color_by_gradient(RED,GREEN,BLUE)\
                    .fix_in_frame()\
                    .to_edge(UP)
                
        cube = CubicLattice(side_length=3)\
                .set_fill(BLUE,0.2)\
                .set_stroke(WHITE,1.5)
        cube.shift(0.5*DR)
        ax = ThreeDAxes(
            x_range = np.array([0,1,0.25]),
            y_range = np.array([0,1,0.25]),
            z_range = np.array([0,1,0.25]),
            height = 3,
            width = 3,
            depth = 3
        )
        ax.shift(cube.get_corner(DL+IN) - ax.c2p(0,0,0))     # Shifting the Origin of the axis to cube corner
        x_lb = Tex("x").rotate(PI/2)\
                    .rotate(PI/2,axis=UP,about_point=ORIGIN)\
                    .rotate(PI/4)\
                    .move_to(ax.c2p(1.1,0,0))
        y_lb = Tex("y").rotate(PI/2)\
                    .rotate(PI/2,axis=UP,about_point=ORIGIN)\
                    .rotate(PI/4)\
                    .move_to(ax.c2p(0,1.1,0))
        z_lb = Tex("z").rotate(PI/2)\
                    .rotate(PI/2,axis=UP,about_point=ORIGIN)\
                    .rotate(PI/4)\
                    .move_to(ax.c2p(0,0,1.1))
        labels = VGroup(x_lb,y_lb,z_lb)
        
        self.add(topic,cube,ax,labels)

        voids_cords = [[(0.25,0.5,0),(0.75,0.5,0),(0.5,0.25,0),(0.5,0.75,0)],
                       [(0.25,0,0.5),(0.75,0,0.5),(0.5,0,0.25),(0.5,0,0.75)],
                       [(0,0.25,0.5),(0,0.75,0.5),(0,0.5,0.25),(0,0.5,0.75)]]
        voids_xy = SGroup(*[Sphere(radius=0.1,color=ORANGE).move_to(ax.c2p(x,y,z)) 
                            for (x,y,z) in voids_cords[0]])
        
        voids_zx = SGroup(*[Sphere(radius=0.1,color=GREEN).move_to(ax.c2p(x,y,z)) 
                            for (x,y,z) in voids_cords[1]])
                            
        voids_yz = SGroup(*[Sphere(radius=0.1,color=RED).move_to(ax.c2p(x,y,z)) 
                            for (x,y,z) in voids_cords[2]])
        
        xy_plane = NumberPlane(
            x_range = np.array([0.0,1.0,0.25]),
            y_range = np.array([0.0,1.0,0.25]),
            axis_config = {
                "include_ticks":True
            },
            height = 3,
            width = 3,
            faded_line_ratio=0
        ).set_fill(RED,0.3)
        xy_plane.shift(ax.c2p(0,0,0)-xy_plane.c2p(0,0))
        zx_plane = xy_plane.copy()\
                   .rotate(PI/2,axis=RIGHT,about_point=ax.c2p(0,0,0))\
                   .set_fill(RED,0.3)
        yz_plane = xy_plane.copy()\
                   .rotate(-PI/2,axis=UP,about_point=ax.c2p(0,0,0))\
                   .set_fill(RED,0.3)
        
        self.play(
            FadeIn(xy_plane),
            FadeIn(voids_xy),run_time=2
        )
        self.wait(8) # <- Run SideNote
        
        self.play(
            TransformFromCopy(voids_xy,voids_zx),
            FadeIn(zx_plane),run_time=2
        )
        self.wait(8) # <- Run SideNote
        
        self.play(
            TransformFromCopy(voids_zx,voids_yz),
            FadeIn(yz_plane),run_time=2
        )
        self.wait(3)
        
        self.play(
            *[FadeOut(obj) for obj in 
             [xy_plane,zx_plane,yz_plane,voids_xy,voids_yz,voids_zx]],
             run_time=3
        )
        xy_plane.shift(3*OUT)
        voids_xy.shift(3*OUT)
        zx_plane.shift(3*UP)
        voids_zx.shift(3*UP)
        yz_plane.shift(3*RIGHT)
        voids_yz.shift(3*RIGHT) 

        self.play(
            *[FadeIn(obj) for obj in 
             [xy_plane,zx_plane,yz_plane,voids_xy,voids_yz,voids_zx]],
             run_time=3
        )
        self.wait(3)

        cube_cp = VGroup(*[cube.copy() for _ in range(3)])

        self.play(
            *[FadeOut(obj) for obj in 
             [zx_plane,voids_zx,yz_plane,voids_yz]],run_time=2
        )
        self.wait(3)

        self.play(
            *[obj.animate.shift(OUT) for obj in
             [cube_cp[0],ax,labels]],
            *[obj.animate.shift(2*IN) for obj in
             [cube,xy_plane,voids_xy]],
             run_time=2
        )
        self.wait(4)
        self.play(
            *[obj.animate.shift(IN) for obj in
             [cube_cp[0],ax,labels]],
            *[obj.animate.shift(2*OUT) for obj in
             [cube,xy_plane,voids_xy]],
             FadeOut(cube_cp[0]),
             run_time=2
        )
        self.wait(2)
        self.play(
            FadeIn(zx_plane),
            FadeIn(voids_zx),
            FadeOut(xy_plane),
            FadeOut(voids_xy), run_time=2
        )
        self.wait(2)
        self.play(
            *[obj.animate.shift(1.5*UP) for obj in
             [cube_cp[1],ax,labels]],
            *[obj.animate.shift(1.5*DOWN) for obj in
             [cube,zx_plane,voids_zx]],
             run_time=2
        )
        self.wait(4)
        self.play(
            *[obj.animate.shift(1.5*DOWN) for obj in
             [cube_cp[1],ax,labels]],
            *[obj.animate.shift(1.5*UP) for obj in
             [cube,zx_plane,voids_zx]],
             FadeOut(cube_cp[1]),
             run_time=2
        )
        self.wait(2)
        self.play(
            FadeOut(zx_plane),
            FadeOut(voids_zx),
            FadeIn(yz_plane),
            FadeIn(voids_yz),run_time=2
        )
        self.wait(2)
        self.play(
            *[obj.animate.shift(1.5*RIGHT) for obj in
             [cube_cp[2],ax,labels]],
            *[obj.animate.shift(1.5*LEFT) for obj in
             [cube,yz_plane,voids_yz]],
             run_time=2
        )
        self.wait(4)
        self.play(
            *[obj.animate.shift(1.5*LEFT) for obj in
             [cube_cp[2],ax,labels]],
            *[obj.animate.shift(1.5*RIGHT) for obj in
             [cube,yz_plane,voids_yz]],
             FadeOut(cube_cp[2]),
             run_time=2
        )
        self.wait(2)
        self.play(
            *[FadeIn(obj) for obj in
             [xy_plane,voids_xy,zx_plane,voids_zx]],run_time=2
        )
        self.wait()
        
        self.play(
            zx_plane.animate.shift(3*DOWN),
            voids_zx.animate.shift(3*DOWN),run_time=2
        )
        self.play(
            yz_plane.animate.shift(3*LEFT),
            voids_yz.animate.shift(3*LEFT),run_time=2
        )
        self.play(
            xy_plane.animate.shift(3*IN),
            voids_xy.animate.shift(3*IN),run_time=2
        )
        self.wait(4)

class Scene_5_SideNote(Scene):
    def construct(self):
        voids_cords = [[(0.25,0.5,0),(0.75,0.5,0),(0.5,0.25,0),(0.5,0.75,0)],
                       [(0.25,0,0.5),(0.75,0,0.5),(0.5,0,0.25),(0.5,0,0.75)],
                       [(0,0.25,0.5),(0,0.75,0.5),(0,0.5,0.25),(0,0.5,0.75)]]
        coords_frac = VGroup(
            VGroup(*[coord_to_frac_tex(x,y,z) for (x,y,z) in voids_cords[0]])\
                    .set_color(ORANGE)\
                    .arrange(DOWN,buff=0.5),
            VGroup(*[coord_to_frac_tex(x,y,z) for (x,y,z) in voids_cords[1]])\
                    .set_color(GREEN)\
                    .arrange(DOWN,buff=0.5),
            VGroup(*[coord_to_frac_tex(x,y,z) for (x,y,z) in voids_cords[2]])\
                    .set_color(RED)\
                    .arrange(DOWN,buff=0.5)
            ).arrange(RIGHT,buff=0.5)\
                .scale(0.8)
        txt1 = VGroup(Text("Notice that, for the voids of xy-plane"),
                      Text("the z-coordinate is zero"))\
                      .arrange(DOWN)\
                      .scale(0.7)\
                      .to_edge(DOWN)
        txt2 = VGroup(Text("Similarly for zx-plane the y-coordinate will be zero"),
                      Text("and for yz-plane the x-coordinate will be zero")
                     ).arrange(DOWN)\
                      .scale(0.7)\
                      .to_edge(DOWN)
        txt3 = Text("But what about the voids of other three planes?")\
                .scale(0.7)\
                .to_edge(DOWN)
        txt4 = VGroup(Text("Those planes are actually equivalent to xy, zx, yz planes"),
                      Text("of the adjacent unit cells")
                     ).arrange(DOWN)\
                      .scale(0.7)\
                      .to_edge(DOWN)

        self.play(
            LaggedStart(
                *(FadeIn(obj,LEFT) for obj in coords_frac[0]),
                lag_ratio=0.5,run_time=3
            )
        )
        self.play(FadeIn(txt1,DOWN),run_time=2)
        self.wait(2)
        self.play(FadeOut(txt1),run_time=2)

        self.wait()

        self.play(
            FadeIn(txt2[0]),
            LaggedStart(
                *(FadeIn(obj,UL) for obj in coords_frac[1]),
                lag_ratio=0.5,run_time=3
            ),
            run_time=3
        )
        self.wait(3)
        self.play(
            FadeIn(txt2[1]),
            LaggedStart(
                *(FadeIn(obj,UL) for obj in coords_frac[2]),
                lag_ratio=0.5,run_time=3
            ),
            run_time=3
        )
        self.wait(3)
        self.play(FadeOut(txt2),run_time=2)
        self.wait(3)
        self.play(FadeIn(txt3))
        self.wait(3)
        self.play(FadeTransform(txt3,txt4))
        self.wait(2)    

#   #   #   #   #

class Outro(Scene):
    def construct(self):
        thank = Text("Thank You For Watching")\
                .scale(1.5)\
                .set_color_by_gradient(RED,GREEN,BLUE)
        self.play(DrawBorderThenFill(thank),run_time=8)
        self.wait(4)
        self.play(FadeOut(thank),run_time=3)                          