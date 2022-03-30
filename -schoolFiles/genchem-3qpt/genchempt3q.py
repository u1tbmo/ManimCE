from manim import *

class Intro(Scene):
    def construct (self):
        introA = Tex("Intermolecular Forces")
        introB = Tex("and Experiments")

        intro =  VGroup(introA, introB).arrange(DOWN).scale(1.4)

        self.play(Write(intro))
        self.wait(1.5)
        self.play(Unwrite(intro))
        self.wait()

class Exp1(Scene):
    def construct (self):
        exp1A = Tex('Experiment 1').scale(0.8)
        exp1B = Tex('The Weight of Layers').scale(1.2)
        exp1C = Tex('by Mariano, Eunice Reign')
        exp1 = VGroup(exp1A,exp1B,exp1C).arrange(DOWN)

        self.play(Write(exp1))
        self.wait(1.5)
        self.play(FadeOut(exp1))
        self.wait()

class Exp2(Scene):
    def construct(self):
        exp2A = Tex('Experiment 2').scale(0.8)
        exp2B = Tex('The Density of Layers').scale(1.2)
        exp2C = Tex('by Flores, Andrea Gerard')
        exp2 =  VGroup(exp2A,exp2B,exp2C).arrange(DOWN)

        self.play(Write(exp2))
        self.wait(1.5)
        self.play(FadeOut(exp2))
        self.wait()

class Exp3(Scene):
    def construct (self):
        exp3A = Tex('Experiment 3').scale(0.8)
        exp3B = Tex('The Bubble Volcano').scale(1.2)
        exp3C = Tex('by Chua, Arliyah Carmen')
        exp3 = VGroup(exp3A,exp3B,exp3C).arrange(DOWN)

        self.play(Write(exp3))
        self.wait(1.5)
        self.play(FadeOut(exp3))
        self.wait()

class Outro(Scene):
    def construct (self):
        thx = Tex('Thank you for watching!').scale(1.2)
        animA = Tex('Animated and Edited by:')
        animB = Tex('Tabamo, Euan Jed S.')
        anim = VGroup(animA,animB).arrange(DOWN)
        voiceA = Tex('Voiced and Scripted by:')
        voiceB = Tex('Dayao, Sophia Nicole')
        voice = VGroup(voiceA,voiceB).arrange(DOWN)

        self.play(Write(thx))
        self.wait(1.5)
        self.play(FadeOut(thx))
        self.wait()

        self.play(Write(anim))
        self.wait(1.5)
        self.play(FadeOut(anim))
        self.wait()

        self.play(Write(voice))
        self.wait(1.5)
        self.play(FadeOut(voice))
        self.wait()

class BG(Scene):
    def construct(self):
        imf = Tex('Intermolecular Forces').scale(1.2)
        defA = Text("The pull between molecules keeping them\nin either a solid or liquid phase.",font="CMU Serif", font_size=24, line_spacing=1.5)
        
        propLiq = Tex('Properties of Liquids').scale(1.2)
        defB = Text("The characteristics they hold or the features\nthey are capable of displaying, such as\nsurface tension, viscosity, capillary action,\nand many more.", font="CMU Serif", font_size=24, line_spacing=1.5)

        self.play(Write(imf))
        self.wait(1.5)
        self.play(imf.animate.to_edge(UP))
        self.wait(0.5)
        self.play(Write(defA))
        self.wait(1.5)
        self.play(
            FadeOut(imf),
            FadeOut(defA)
        )
        self.wait()

        self.play(Write(propLiq))
        self.wait(1.5)
        self.play(propLiq.animate.to_edge(UP))
        self.wait(0.5)
        self.play(Write(defB))
        self.wait(1.5)
        self.play(
            FadeOut(propLiq),
            FadeOut(defB)
        )
        self.wait()