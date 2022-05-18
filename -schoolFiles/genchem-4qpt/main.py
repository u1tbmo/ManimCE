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