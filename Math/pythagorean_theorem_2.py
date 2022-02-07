from manimlib.imports import *
import numpy as np

class Bhaskara(Scene):
    def construct(self):
        
        intro = TextMobject("Pythagorean Theorem")
        intro.set_color_by_gradient(BLUE,PURPLE)
        self.play(Write(intro),run_time = 5)
        self.wait()
        self.play(FadeOut(intro),run_time = 2)
        self.remove(intro)
        self.wait(2)
        info1 = TextMobject("This proof was given by")
        info2 = TexMobject("Bh\\bar{a}skara","-\\textrm{II} ","(1114-1185)")
        info3 = TextMobject("also known as ")
        info4 = TexMobject("Bh\\bar{a}skar\\bar{a}ch\\bar{a}rya")
        info5 = TextMobject("He was an Indian mathematician and astronomer")

        info2.set_color_by_gradient(RED,BLUE)
        info4.set_color_by_gradient(RED,BLUE)
        
        info1.to_edge(LEFT+UP)
        info2.next_to(info1,RIGHT,buff = 0.1)
        info3.next_to(info1,DOWN,buff = 0.5)
        info3.align_to(info1,LEFT)
        info4.next_to(info3,RIGHT,buff = 0.1)
        info5.next_to(info3,DOWN,buff = 0.5)
        info5.align_to(info3,LEFT)
        
        self.play(
            FadeIn(info1),
            Write(info2),
            FadeIn(info3),
            Write(info4),
            FadeIn(info5), run_time = 6
        )
        self.wait(4)
        info = VGroup(info1,info2,info3,info4,info5)
        self.play(FadeOut(info))

        l1 = Line(np.array([0,-2,0]),np.array([-3,-2,0]))
        l2 = Line(np.array([-3,-2,0]),np.array([-3,0,0]))
        l3 = Line(np.array([-3,0,0]),np.array([0,-2,0]))
        l1.set_color(ORANGE)
        l2.set_color(BLUE)
        l3.set_color(GREEN)

        l4 = Line(np.array([0,-2,0]),np.array([2,-2,0]))
        l5 = Line(np.array([2,-2,0]),np.array([2,1,0]))
        l6 = Line(np.array([2,1,0]),np.array([0,-2,0]))
        l4.set_color(BLUE)
        l5.set_color(ORANGE)
        l6.set_color(GREEN)

        l7 = Line(np.array([2,1,0]),np.array([2,3,0]))
        l8 = Line(np.array([2,3,0]),np.array([-1,3,0]))
        l9 = Line(np.array([-1,3,0]),np.array([2,1,0]))
        l7.set_color(BLUE)
        l8.set_color(ORANGE)
        l9.set_color(GREEN)

        l10 = Line(np.array([-3,0,0]),np.array([-3,3,0]))
        l11 = Line(np.array([-3,3,0]),np.array([-1,3,0]))
        l12 = Line(np.array([-1,3,0]),np.array([-3,0,0]))
        l10.set_color(ORANGE)
        l11.set_color(BLUE)
        l12.set_color(GREEN)

        a  = TexMobject("a")
        b = TexMobject("b")
        c = TexMobject("c")
        a.set_color(ORANGE)
        b.set_color(BLUE)
        c.set_color(GREEN)

        a1, a2, a3 = a.copy(), a.copy(), a.copy()
        b1, b2, b3 = b.copy(), b.copy(), b.copy()
        c1, c2, c3 = c.copy(), c.copy(), c.copy()

        a.next_to(l1,DOWN, buff = SMALL_BUFF)
        b.next_to(l2,LEFT, buff = SMALL_BUFF)
        c.move_to(np.array([-1.5,-0.7,0]))
        a1.next_to(l5,RIGHT, buff = SMALL_BUFF)
        b1.next_to(l4,DOWN, buff = SMALL_BUFF)
        c1.move_to(np.array([0.7,-0.5,0]))
        a2.next_to(l8,UP, buff = SMALL_BUFF)
        b2.next_to(l7,RIGHT, buff = SMALL_BUFF)
        c2.move_to(np.array([0.5,1.7,0]))
        a3.next_to(l10,LEFT, buff = SMALL_BUFF)
        b3.next_to(l11,UP, buff = SMALL_BUFF)
        c3.move_to(np.array([-1.9,1.3,0]))

        tri_area1 = TexMobject("\\frac{1}{2}","a","b")
        tri_area1[0].set_stroke(WHITE,2)
        tri_area1[1].set_stroke(ORANGE,2)
        tri_area1[2].set_stroke(BLUE,2)
        tri_area1.scale(0.7)
        tri_area2,tri_area3,tri_area4 = tri_area1.copy(),tri_area1.copy(),tri_area1.copy()
        tri_area1.move_to(np.array([-2.2,-1.3,0]))
        tri_area2.move_to(np.array([1.3,-1.3,0]))
        tri_area3.move_to(np.array([1.5,2.3,0]))
        tri_area4.move_to(np.array([-2.3,2.2,0]))

        c_sq = TexMobject("c^2")
        c_sq.set_color(GREEN)
        c_sq.move_to([-0.5,0.5,0])
        
        self.play(
            ShowCreation(l1),
            ShowCreation(l2),
            ShowCreation(l3), run_time = 4
        )
        self.play(
            Write(a),
            Write(b),
            Write(c), run_time = 3
        )
        self.wait(2)
        self.play(
            ReplacementTransform(l2.copy(),l4),
            ReplacementTransform(a.copy(),a1),
            ReplacementTransform(l1.copy(),l5),
            ReplacementTransform(b.copy(),b1), run_time = 3
        )
        self.play(
            ShowCreation(l6)
        )
        self.play(Write(c1))
        self.wait(2)
        self.play(
            ReplacementTransform(l4.copy(),l7),
            ReplacementTransform(a1.copy(),a2),
            ReplacementTransform(l5.copy(),l8),
            ReplacementTransform(b1.copy(),b2),
            ReplacementTransform(l1.copy(),l10),
            ReplacementTransform(a.copy(),a3),
            ReplacementTransform(l2.copy(),l11),
            ReplacementTransform(b.copy(),b3),
            ReplacementTransform(l3.copy(),l12),
            ReplacementTransform(c.copy(),c3),
            ReplacementTransform(l6.copy(),l9),
            ReplacementTransform(c1.copy(),c2), run_time = 4
        )
        self.wait(2)
        ab = VGroup(a,b)
        a1b1 = VGroup(a1,b1)
        a2b2 = VGroup(a2,b2)
        a3b3 = VGroup(a3,b3)
        cc1c2c3 = VGroup(c,c1,c2,c3)
        self.play(
            ReplacementTransform(ab.copy(),tri_area1),
            ReplacementTransform(a1b1.copy(),tri_area2),
            ReplacementTransform(a2b2.copy(),tri_area3),
            ReplacementTransform(a3b3.copy(),tri_area4), run_time = 4
        )
        self.wait(2)
        self.play(ReplacementTransform(cc1c2c3.copy(),c_sq))
        self.wait(3)
        scene1 = VGroup(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,a,b,c,a1,b1,c1,a2,b2,c2,a3,b3,c3,tri_area1,tri_area2,tri_area3,tri_area4,c_sq)
        self.play(
            ApplyMethod(scene1.to_edge,LEFT), run_time = 3
        )
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12 = l1.copy(),l2.copy(),l3.copy(),l4.copy(),l5.copy(),l6.copy(),l7.copy(),l8.copy(),l9.copy(),l10.copy(),l11.copy(),l12.copy()
        a_1,a_2,a_3,a_4 = a.copy(),a1.copy(),a2.copy(),a3.copy()
        b_1,b_2,b_3,b_4 = b.copy(),b1.copy(),b2.copy(),b3.copy()
        c_1,c_2,c_3,c_4 = c.copy(),c1.copy(),c2.copy(),c3.copy()
        tri_1,tri_2,tri_3,tri_4 = tri_area1.copy(),tri_area2.copy(),tri_area3.copy(),tri_area4.copy()
        c_square = c_sq.copy()

        self.wait()
        scene2 = VGroup(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,c_1,c_2,c_3,c_4,tri_1,tri_2,tri_3,tri_4,c_square)
        self.play(
            ApplyMethod(scene2.to_edge, RIGHT) , run_time = 3
        )
        line7_cp = line7.copy()
        line8_cp = line8.copy()
        line9_cp = line9.copy()
        line10_cp = line10.copy()
        line11_cp = line11.copy()
        line12_cp = line12.copy()
        line7_9 = VGroup(line7_cp,line8_cp,line9_cp,tri_3)
        line10_12 = VGroup(line10_cp,line11_cp,line12_cp,tri_4)

        self.wait(2)
        self.play(
            ApplyMethod(line7_9.shift, 2*LEFT+3*DOWN), run_time = 3
        )
        self.play(
            ApplyMethod(line10_12.shift, 3*RIGHT+2*DOWN),run_time = 3
        )
        self.play(
            FadeOut(line3),
            FadeOut(line9_cp),
            FadeOut(line6),
            FadeOut(line12_cp),
            FadeOut(line9),
            FadeOut(line12),
            FadeOut(c_1),
            FadeOut(c_2),
            FadeOut(c_3),
            FadeOut(c_4),
            FadeOut(c_square), run_time = 4
        )
        self.remove(line3)
        self.remove(line9_cp)
        self.remove(line6)
        self.remove(line12_cp)
        self.remove(line9)
        self.remove(line12)
        self.remove(c_1)
        self.remove(c_2)
        self.remove(c_3)
        self.remove(c_4)
        self.remove(c_square)
        self.wait(2)

        ab_area1 = TexMobject("a","b")
        ab_area1[0].set_stroke(ORANGE,2)
        ab_area1[1].set_stroke(BLUE,2)
        ab_area2 = ab_area1.copy()
        ab_area1.next_to(line1,UP,buff = 1)
        ab_area2.next_to(line4,UP, buff = 1)

        tri_2_tri_4 = VGroup(tri_2,tri_4)
        tri_1_tri_3 = VGroup(tri_1,tri_3)

        self.play(
            ReplacementTransform(tri_2_tri_4,ab_area2),
            ReplacementTransform(tri_1_tri_3,ab_area1), run_time = 3
        )
        self.wait(2)
        line8_a_3 = VGroup(line8,a_3)
        line11_b_4 = VGroup(line11,b_4)
        self.play(
            ApplyMethod(line8_a_3.shift, 2*LEFT),
            ApplyMethod(line11_b_4.shift, 3*RIGHT), run_time = 3
        )
        self.wait(2)
        line7_cpp = line7.copy()
        self.play(
            ApplyMethod(line7_cpp.shift, 2*LEFT), run_time = 2
        )
        self.wait(2)
        a_sqaure = TexMobject("a^2")
        b_square = TexMobject("b^2")
        a_sqaure.set_stroke(ORANGE,2)
        b_square.set_stroke(BLUE,2)
        a_sqaure.next_to(line8_a_3,DOWN, buff = 1.2)
        b_square.next_to(line11_b_4,DOWN, buff = 0.7)
        
        a_3_a_4 = VGroup(a_3,a_4)
        b_3_b_4 = VGroup(b_3,b_4)
        self.play(
            ReplacementTransform(a_3_a_4.copy(),a_sqaure),
            ReplacementTransform(b_3_b_4.copy(),b_square), run_time = 3
        )
        scene2 = VGroup(line1,line2,line4,line5,line7,line8,line10,line11,a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,ab_area1,ab_area2,a_sqaure,b_square,line7_cp,line8_cp,line10_cp,line11_cp,line7_cpp)
        self.wait(3)
        self.play(
            ApplyMethod(scene1.scale, 0.6),
            ApplyMethod(scene2.scale, 0.6), run_time =2
        )
        self.play(
            ApplyMethod(scene1.to_edge, UP+RIGHT),
            FadeOutAndShift(a,UP),
            FadeOutAndShift(b,UP),
            FadeOutAndShift(c,UP),
            FadeOutAndShift(a1,UP),
            FadeOutAndShift(b1,UP),
            FadeOutAndShift(c1,UP),
            FadeOutAndShift(a2,UP),
            FadeOutAndShift(b2,UP),
            FadeOutAndShift(c2,UP),
            FadeOutAndShift(a3,UP),
            FadeOutAndShift(b3,UP),
            FadeOutAndShift(c3,UP),
            ApplyMethod(scene2.to_edge, DOWN+RIGHT),
            FadeOutAndShift(a_1,UP),
            FadeOutAndShift(b_1,UP),
            FadeOutAndShift(c_1,UP),
            FadeOutAndShift(a_2,UP),
            FadeOutAndShift(b_2,UP),
            FadeOutAndShift(c_2,UP),
            FadeOutAndShift(a_3,UP),
            FadeOutAndShift(b_3,UP),
            FadeOutAndShift(c_3,UP),
            FadeOutAndShift(a_4,UP),
            FadeOutAndShift(b_4,UP),
            FadeOutAndShift(c_4,UP), run_time = 3
        )
        self.remove(a)
        self.remove(b)
        self.remove(c)
        self.remove(a1)
        self.remove(b1)
        self.remove(c1)
        self.remove(a2)
        self.remove(b2)
        self.remove(c2)
        self.remove(a3)
        self.remove(b3)
        self.remove(c3)
        self.remove(a_1)
        self.remove(b_1)
        self.remove(a_2)
        self.remove(b_2)
        self.remove(a_3)
        self.remove(b_3)
        self.remove(a_4)
        self.remove(b_4)

        text1 = TextMobject("Total Area will be same in both cases")
        text1.to_edge(LEFT+UP)
        
        text2 = TexMobject("\\therefore","c^2","+","4","\\times","\\frac{1}{2}","a","b","=","a^2","+","b^2","+","2","a","b")
        text2[1].set_stroke(GREEN,2)
        text2[6].set_stroke(ORANGE,2)
        text2[7].set_stroke(BLUE,2)
        text2[9].set_stroke(ORANGE,2)
        text2[11].set_stroke(BLUE,2)
        text2[14].set_stroke(ORANGE,2)
        text2[15].set_stroke(BLUE,2)
        text2.next_to(text1,DOWN)
        text2.align_to(text1,LEFT)
        
        text3 = TexMobject("\\Rightarrow","c^2","+","2","a","b","=","a^2","+","b^2","+","2","a","b")
        text3[1].set_stroke(GREEN,2)
        text3[4].set_stroke(ORANGE,2)
        text3[5].set_stroke(BLUE,2)
        text3[7].set_stroke(ORANGE,2)
        text3[9].set_stroke(BLUE,2)
        text3[12].set_stroke(ORANGE,2)
        text3[13].set_stroke(BLUE,2)
        text3.next_to(text2,DOWN)
        text3.align_to(text2,LEFT)

        text4 = TexMobject("c^2","=","a^2","+","b^2")
        text4[0].set_stroke(GREEN,2)
        text4[2].set_stroke(ORANGE,2)
        text4[3].set_stroke(BLUE,2)
        text4.next_to(text3,DOWN,buff = 1)
        
        self.play(Write(text1),run_time = 3)
        self.wait(2)
        area_scene1 = VGroup(tri_area1,tri_area2,tri_area3,tri_area4)
        area_scene2 = VGroup(ab_area1,ab_area2,a_sqaure,b_square)
        self.play(
            ReplacementTransform(c_sq.copy(),text2[0:2]),
            FadeIn(text2[2]),
            ReplacementTransform(area_scene1.copy(),text2[3:8]),
            FadeIn(text2[8]),
            ReplacementTransform(area_scene2.copy(),text2[9:]), run_time = 4
        )
        self.wait(2)
        self.play(
            FadeIn(text3[0:2]),
            ReplacementTransform(text2[2:7].copy(),text3[2:5]),
            FadeIn(text3[5]),
            TransformFromCopy(text2[8:],text3[6:])
        )
        self.wait(2)
        box = SurroundingRectangle(text4,buff = SMALL_BUFF)
        box.set_stroke(WHITE, 2)
        self.play(
            ReplacementTransform(text3.copy(),text4)
        )
        self.wait()
        self.play(ShowCreation(box))
        self.wait(4)
        
        scene1 = VGroup(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,tri_area1,tri_area2,tri_area3,tri_area4,c_sq)
        scene2 = VGroup(line1,line2,line4,line5,line7,line8,line10,line11,ab_area1,ab_area2,a_sqaure,b_square,line7_cp,line8_cp,line10_cp,line11_cp,line7_cpp)
        scene3 = VGroup(text1,text2,text3,text4,box)
        
        self.play(
            FadeOut(scene1),
            FadeOut(scene2),
            FadeOut(scene3), run_time = 2
        )
        

        thank = TextMobject("Thank You For Watching")
        thank.set_color_by_gradient(PURPLE,RED)
        self.play(
            Write(thank), run_time = 4
        )
        self.wait(2)
        self.play(FadeOut(thank))
        self.wait(3)
