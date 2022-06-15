from manim import *
import manimpango

class TextMobjects(Scene):
    def construct(self):

        fdp = Text("Freezing Point Depression", font="Archivo", color=WHITE)
        deffdp = Text(
            'Freezing Point Depression, which is a colligative property,\nis the amount that the freezing point of a solution decreases\nfrom the freezing point of the pure solvent.'
,font='Archivo',color=WHITE, font_size=24
        )

        self.play(Write(fdp))
        self.wait(2)
        self.play(fdp.animate.to_edge(UP))
        self.wait(1)

        self.play(Write(deffdp),run_time=4)
        self.wait(4)

        self.play(
            FadeOut(fdp),
            FadeOut(deffdp)
        )
        self.wait(1)

class TableMobjects(Scene):
    def construct(self):

        table = MobjectTable(
            [
                [MathTex(r'{1.86}^o C/m'),Tex('0m'),Tex('N/A'), MathTex(r'{0}^o C'), MathTex(r'{0}^o C')],
                [MathTex(r'{1.86}^o C/m'),Tex('1.711m'),Tex('2'), MathTex(r'{6.36}^o C'), MathTex(r'{-6.36}^o C')],
                [MathTex(r'{1.86}^o C/m'),Tex('4.107m'),Tex('2'), MathTex(r'{15.28}^o C'), MathTex(r'{-15.28}^o C')]
            ],
            row_labels=[Tex('Trial 1'), Tex('Trial 2'), Tex('Trial 3')],
            col_labels=[MathTex('K_f'), MathTex('m'), MathTex('i'), MathTex('\Delta T_f'), MathTex('T_f')],
            ).scale(0.6)

        self.play(FadeIn(table))
        self.wait(2)
        self.play(FadeOut(table))
        self.wait(1)

class NaCl(Scene):
    def construct(self):
        sodiumChloride = Tex('NaCl')
        sodiumIon = Tex('Na$^-$')
        chlorineIon = Tex('Cl$^+$')
        ice = Tex('H$_2$O')
        p = Tex(' + ')

        s1 = MathTex('NaCl')
        s2 = MathTex('H_2O + NaCl')
        s3 = MathTex('H_2O + Na^- + Cl^+')

        
        self.play(
            Write(
                s1
            )
        )
        self.wait(2)
        self.play(
            Transform(
                s1,s2
            )
        )
        self.wait()
        self.play(
            Transform(
                s1,s3
            )
        )
        self.wait()

class phaseTrans(Scene):
    def construct(self):
        line = Line(
            start=LEFT*7,
            end=RIGHT*7,
        )
        line.set_color(BLUE)

        iceSaltMixture = Tex('Ice-Salt Mixture').to_edge(UP)
        iceCreamMixture = Tex('Ice Cream Mixture').to_edge(DOWN)

        iceSaltNL = NumberLine(
            x_range=[-3,3]
        ).shift(UP*1.5)

        iceCreamNL = NumberLine(
            x_range=[-3,3]
        ).shift(DOWN*1.5)

        solidIS = Tex('Solid').next_to(iceSaltNL,LEFT)
        solidIC = Tex('Solid').next_to(iceCreamNL,LEFT)
        liquidIS = Tex('Liquid').next_to(iceSaltNL,RIGHT)
        liquidIC = Tex('Liquid').next_to(iceCreamNL,RIGHT)

        a = ValueTracker(-3)
        b = ValueTracker(3)

        aDot = always_redraw(lambda: Dot(iceSaltNL.n2p(a.get_value())))
        bDot = always_redraw(lambda: Dot(iceCreamNL.n2p(b.get_value())))

        #iceSaltA = always_redraw(lambda: Arrow(
        #    DOWN
        #).next_to(iceSaltNL, UP))
#
        #iceCreamA = always_redraw(lambda: Arrow(
        #    DOWN
        #).next_to(iceCreamNL, UP))

        self.add(iceCreamMixture, iceSaltMixture, solidIC, solidIS, liquidIC, liquidIS)
        self.add(line, iceSaltNL, aDot, iceCreamNL, bDot,)#, iceSaltA, iceCreamA)
        self.wait(1)
        self.play(a.animate.set_value(3), b.animate.set_value(-3),run_time=6,rate_func=smooth)
        self.wait()