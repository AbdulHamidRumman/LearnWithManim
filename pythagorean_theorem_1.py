from manimlib.imports import *

class Pytha(Scene):
    def construct(self):
        intro = TextMobject("Pythagorean Theorem")
        intro.set_color_by_gradient(BLUE,PURPLE)
        self.play(Write(intro),run_time = 5)
        self.wait()
        self.play(FadeOut(intro),run_time = 2)
        self.wait(2)
        l1 = Line(np.array([0,-1,0]),np.array([-3,-1,0]))
        l2 = Line(np.array([-3,-1,0]),np.array([-3,3,0]))
        l3 = Line(np.array([-3,3,0]),np.array([0,-1,0]))
        l1.set_color(BLUE)
        l2.set_color(PINK)
        l3.set_color(YELLOW)
        
        l4 = Line(np.array([0,-1,0]),np.array([4,-1,0]))
        l5 = Line(np.array([4,-1,0]),np.array([4,2,0]))
        l6 = Line(np.array([4,2,0]),np.array([0,-1,0]))
        l4.set_color(PINK)
        l5.set_color(BLUE)
        l6.set_color(YELLOW)

        l7 = Line(np.array([-3,3,0]),np.array([4,2,0]))
        l7.set_color(ORANGE)

        angl1 = TexMobject("90^\\circ")
        angl2 = TexMobject("90^\\circ")
        angl3 = TexMobject("90^\\circ")
        arc1 = ArcBetweenPoints(np.array([-2.5,-1,0]),np.array([-3,-0.5,0]),angle = PI/2)
        arc2 = ArcBetweenPoints(np.array([3.5,-1,0]),np.array([4,-0.5,0]),angle = -PI/2)
        arc3 = ArcBetweenPoints(np.array([0.6,-0.6,0]),np.array([-0.4,-0.5,0]),angle = PI/2)
        angl1.move_to([-2.5,-0.2,0])
        angl2.move_to([3.5,-0.2,0])
        angl3.move_to([0,0,0])
        angl1.scale(0.7)
        angl2.scale(0.7)
        angl3.scale(0.7)

        a = TexMobject("a")
        b = TexMobject("b")
        c = TexMobject("c")
        a1 = TexMobject("a")
        b1 = TexMobject("b")
        c1 = TexMobject("c")
        a.set_color(BLUE)
        b.set_color(PINK)
        c.set_color(YELLOW)
        a1.set_color(BLUE)
        b1.set_color(PINK)
        c1.set_color(YELLOW)
        a.next_to(l1, DOWN, buff = SMALL_BUFF)
        b.next_to(l2, LEFT, buff = SMALL_BUFF)
        c.move_to(np.array([-1.5,1.5,0]))
        a1.next_to(l5,RIGHT,buff = SMALL_BUFF)
        b1.next_to(l4,DOWN,buff = SMALL_BUFF)
        c1.move_to(np.array([2,1,0]))
        area1 = TexMobject("\\frac{1}{2}","a","b")
        area2i = TexMobject("\\frac{1}{2}","b","a")
        area2f = TexMobject("\\frac{1}{2}","a","b")
        area3 = TexMobject("\\frac{1}{2}","c","c")
        area4 = TexMobject("\\frac{1}{2}","c","^2")
        
        area1[1].set_color(BLUE)
        area1[2].set_color(PINK)
        area2i[1].set_color(PINK)
        area2i[2].set_color(BLUE)
        area2f[1].set_color(BLUE)
        area2f[2].set_color(PINK)
        area3[1].set_color(YELLOW)
        area3[2].set_color(YELLOW)
        area4[1].set_color(YELLOW)
        area4[2].set_color(YELLOW)
        area1.move_to(np.array([-1.6,0.33,0]))
        area2i.move_to(np.array([2.67,0,0]))
        area2f.move_to(np.array([2.67,0,0]))
        area3.move_to(np.array([0.33,1,0]))
        area4.move_to(np.array([0.33,1,0]))
        
        self.play(
            ShowCreation(l1),
            ShowCreation(l2),
            ShowCreation(l3),run_time = 3
            )
        self.play(
            Write(a),
            Write(b),
            Write(c), run_time = 2
            )
        self.play(
            ShowCreation(arc1),
            FadeIn(angl1)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(l2.copy(),l4),
            ReplacementTransform(b.copy(),b1), run_time = 3
        )
        self.wait()
        self.play(
            ReplacementTransform(l1.copy(),l5),
            ReplacementTransform(a.copy(),a1), run_time = 3
            )
        self.play(ShowCreation(l6))
        self.play(
            ShowCreation(arc2),
            FadeIn(angl2)
        )
        self.play(Write(c1))
        self.play(Write(l7))
        self.play(
            ShowCreation(arc3),
            FadeIn(angl3)
        )
        self.wait()
        self.play(Write(area1))
        self.wait(2)
        self.play(
            Write(area2i)
            )
        self.wait(2)
        self.play(
            ReplacementTransform(area2i,area2f)
            )
        self.wait(2)
        self.play(Write(area3))
        self.wait(2)
        self.play(
            ReplacementTransform(area3,area4)
            )
        self.wait(2)
        
        scene1 = VGroup(l1,l2,l3,l4,l5,l6,l7,a,b,c,a1,b1,c1,area1,area2f,area4,arc1,arc2,arc3,angl1,angl2,angl3)
        self.play(ApplyMethod(scene1.scale,0.7),run_time = 2)
        self.play(ApplyMethod(scene1.to_edge,UP), run_time = 1)
        trapezium = Polygon(np.array([-3,-3,0]),np.array([4,-3,0]),np.array([4,0,0]),np.array([-3,1,0]))
        trapezium.set_color(WHITE)
        a2 = TexMobject("a")
        b2 = TexMobject("b")
        a2_b2 = TexMobject("(","a","+","b",")")
        area_trap = TexMobject("\\frac{1}{2}","(","a","+","b",")","(","a","+","b",")")
        area_trape = TexMobject("\\frac{1}{2}","(","a","+","b",")^2")
      
        a2.set_color(BLUE)
        b2.set_color(PINK)
        a2_b2[1].set_color(BLUE)
        a2_b2[3].set_color(PINK)
        area_trap.set_color_by_tex("a",BLUE)
        area_trape.set_color_by_tex("a",BLUE)
        area_trap.set_color_by_tex("b",PINK)
        area_trape.set_color_by_tex("b",PINK)
        area_trap[0].set_color(WHITE)
        area_trape[0].set_color(WHITE)
        a2.move_to(np.array([4.2,-1.5,0]))
        b2.next_to(trapezium,LEFT,buff = SMALL_BUFF)
        a2_b2.next_to(trapezium,DOWN,buff = SMALL_BUFF)
        area_trap.move_to(np.array([0.7,-1.2,0]))
        area_trape.move_to(np.array([0.7,-1.2,0]))
        area_trap.scale(0.7)
        area_trape.scale(0.7)
        trap = VGroup(trapezium,a2,b2,a2_b2)
        trap.scale(0.7)
        tri = VGroup(l1,l2,l4,l5,l7,a,b,a1,b1)
        ab_group = VGroup(a2,b2)
        self.play(
            ReplacementTransform(tri.copy(),trap), run_time = 3)
        self.wait()
        self.play(
            Write(area_trap[0]),
            ReplacementTransform(a2_b2.copy(),area_trap[1:5]),
            ReplacementTransform(ab_group.copy(),area_trap[5:]),run_time = 3
        )
        self.wait(2)
        self.play(ReplacementTransform(area_trap,area_trape))
        self.remove(area_trap)
        scene2 = VGroup(trap,area_trape)
        self.play(
            ApplyMethod(scene1.to_edge,LEFT+UP),
            ApplyMethod(scene2.to_edge,LEFT+DOWN),run_time = 3)
        self.wait(3)

        eq1 = TextMobject("$\\sum$ Area of Triangle = Area of Trapezium")
        eq1.to_edge(RIGHT+UP)
        eq2 = TexMobject("\\frac{1}{2}","a","b","+","\\frac{1}{2}","c^2","+","\\frac{1}{2}","a","b","=","\\frac{1}{2}","(","a","+","b",")^2")
        g1 = VGroup(eq2[0],eq2[1],eq2[2],eq2[7],eq2[8],eq2[9])
        eq2.set_color_by_tex("a",BLUE)
        eq2.set_color_by_tex("b",PINK)
        eq2[5].set_color(YELLOW)
        eq2.set_color_by_tex("\\frac{1}{2}",WHITE)
        eq2.next_to(eq1,DOWN)
        eq3 = TexMobject("a","b","+","\\frac{1}{2}","c^2","=","\\frac{1}{2}","(","a^2","+","2","a","b","+","b^2",")")
        eq3.set_color_by_tex("a",BLUE)
        eq3.set_color_by_tex("b",PINK)
        eq3[4].set_color(YELLOW)
        eq3[8].set_color(BLUE)
        eq3[14].set_color(PINK)
        eq3.set_color_by_tex("\\frac{1}{2}",WHITE)
        eq3.next_to(eq2,DOWN)
        eq4 = TexMobject("a","b","+","\\frac{1}{2}","c^2","=","\\frac{1}{2}","a^2","+","a","b","+","\\frac{1}{2}","b^2")
        eq4.set_color_by_tex("a",BLUE)
        eq4.set_color_by_tex("b",PINK)
        eq4[4].set_color(YELLOW)
        eq4[7].set_color(BLUE)
        eq4[13].set_color(PINK)
        eq4.set_color_by_tex("\\frac{1}{2}",WHITE)
        eq4.next_to(eq3,DOWN)
        eq5 = TexMobject("\\frac{1}{2}","c^2","=","\\frac{1}{2}","a^2","+","\\frac{1}{2}","b^2")
        eq5[1].set_color(YELLOW)
        eq5[4].set_color(BLUE)
        eq5[7].set_color(PINK)
        eq5.set_color_by_tex("\\frac{1}{2}",WHITE)
        eq5.next_to(eq4,DOWN)
        eq6 = TexMobject("c^2","=","a^2","+","b^2")
        eq6.next_to(eq5,DOWN)
        eq6[0].set_color(YELLOW)
        eq6[2].set_color(BLUE)
        eq6[4].set_color(PINK)

        eq = VGroup(eq1,eq2,eq3,eq4,eq5,eq6)
        eq.scale(0.7)
        self.play(FadeIn(eq1))
        self.wait(2)
        self.play(FadeIn(eq2))
        self.wait(2)
        self.play(ReplacementTransform(g1.copy(),eq3[0:2]))
        self.wait()
        self.play(FadeIn(eq3[2:6]))
        self.play(ReplacementTransform(eq2[12:].copy(),eq3[6:]))
        self.wait(2)
        self.play(FadeIn(eq4))
        self.wait(2)
        self.play(FadeIn(eq5))
        self.wait(2)
        box = SurroundingRectangle(eq6,buff = SMALL_BUFF)
        box.set_color(WHITE)
        scene3 = VGroup(eq,box)
        self.play(
            FadeIn(eq6),
            ShowCreation(box),run_time = 2
        )

        self.wait(5)

        self.play(
            FadeOut(scene1),
            FadeOut(scene2),
            FadeOut(scene3), run_time = 2
        )
        james = TextMobject("James Abram Garfield (1831-1881)",)
        img  = ImageMobject("James_Abram_Garfield.jpg")
        img.scale(2)
        img.to_edge(LEFT+UP)
        james.scale(0.5)
        james.next_to(img,DOWN,buff = SMALL_BUFF)
        self.play(
            FadeIn(img),
            FadeIn(james),run_time = 3
        )
        text1 = TextMobject("This proof was given by")
        text1.to_edge(UP)
        text2 = TextMobject("James A. Garfield")
        text2.set_color(GREEN)
        text3 = TextMobject("who was surprisingly not a mathematician.")
        text4 = TextMobject("He was the $20^{th}$ president of")
        text5 = TextMobject("United States of America in 1881")
        text2.next_to(text1,DOWN)
        text3.next_to(text2,DOWN)
        text3.align_to(text2,LEFT)
        text4.next_to(text3,DOWN)
        text4.align_to(text3,LEFT)
        text5.next_to(text4,DOWN)
        text5.align_to(text4,LEFT)
        text = VGroup(text4,text1,text3,text2,text5)
        text.scale(0.7)
        self.play(Write(text1))
        self.wait()
        self.play(Write(text2))
        self.wait(2)
        self.play(
            FadeIn(text3),run_time = 2
        )
        self.wait(2)
        self.play(
            FadeIn(text4),
            FadeIn(text5)
        )
        self.wait(5)
        self.play(
            FadeOut(text),
            FadeOut(img),
            FadeOut(james),run_time = 3
        )
        thank = TextMobject("Thank You For Watching")
        thank.set_color_by_gradient(PURPLE,RED)
        self.play(Write(thank),run_time = 4)
        self.wait(4)


        
