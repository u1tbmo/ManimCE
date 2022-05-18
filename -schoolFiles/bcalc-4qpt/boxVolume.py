from manim import *
import numpy as np
import text as t

class boxVolume(Scene):
    def construct(self):
        xV = ValueTracker(0)
        
        ax = Axes(
            x_length=7, y_length=5, x_range=[-0.2,8,1], y_range=[-20, 530, 80]
        ).to_edge(RIGHT)

        func = ax.plot(lambda x: (25-2*x)*(15-2*x)*(x), color=PINK)
        
        funcLabel = MathTex("V(x) = (25-2x)(15-2x)(x)", color=WHITE)
        funcLabel.next_to(func, UP, buff=0.5)

        volumeLabel = always_redraw(
            lambda: Text(
                'V(' + str(round(xV.get_value(),3)) + ') = ' + str(round(func.underlying_function(xV.get_value()),2)), font='CMU Serif'
                ).to_edge(LEFT, buff=1).scale(0.8)
            )

        funcprime = ax.plot(lambda x: (12*x**2) - (160*x) + (375), color=BLUE)
        funcprimeLabel = Text("V'(3.034) = 0", font='CMU Serif')
        funcprimeLabel.next_to(volumeLabel, DOWN, buff=0.5).shift(RIGHT*0.4).scale(0.8)

        tanLine = always_redraw(
            lambda: ax.get_secant_slope_group(
                xV.get_value(),
                graph=func,
                dx=0.01,
                secant_line_length=2,
                secant_line_color=GREEN
            )
        )
        point = always_redraw(
            lambda: Dot(color=WHITE).move_to(
                ax.c2p(
                    xV.get_value(),
                    func.underlying_function(xV.get_value())
                )
            ).scale(0.8)
        )
        dfpoint = always_redraw(
            lambda: Dot(color=WHITE).move_to(
                ax.c2p(
                    xV.get_value(),
                    funcprime.underlying_function(xV.get_value())
                )
            ).scale(0.8)
        )

        self.play(FadeIn(ax, func, funcprime ,tanLine, point, dfpoint, funcLabel, volumeLabel))
        self.wait(1)
        self.play(xV.animate.set_value(7.5), run_time=6, rate_func=there_and_back)
        self.wait(1)
        self.play(xV.animate.set_value(3.03425), run_time=5)
        self.wait(1)
        self.play(Write(funcprimeLabel))
        self.wait(2)

class details(Scene):
    def construct(self):
        # Set Image Directory
        imageDir = "D:\School Files\Grade 11 - Section P - SY 2021-2022\Basic Calculus\\4thQuarter\PT-Pics"
        
        # Word Problem
        problemHeader = Text(t.problemHeader, font='CMU Serif')
        problem = Text(t.problem, font='CMU Serif', font_size=24)

        # Text Headers of Images
        b1t = Text(t.b1t, font='CMU Serif').to_edge(UP).scale(0.8)
        b2t = Text(t.b2t, font='CMU Serif').to_edge(UP).scale(0.8)
        b3t = Text(t.b3t, font='CMU Serif').to_edge(UP).scale(0.8)
        at = Text(t.at, font='CMU Serif').to_edge(UP).scale(0.8)

        # Image of Box and Diagram
        b1 = ImageMobject(f"{imageDir}\\Before1.png").scale(0.75).to_edge(DOWN)
        b2 = ImageMobject(f"{imageDir}\\Before2.png").scale(0.75).to_edge(DOWN)
        b3 = ImageMobject(f"{imageDir}\\Before3.png").scale(0.75).to_edge(DOWN)
        a = ImageMobject(f"{imageDir}\\After.png").scale(0.75).to_edge(DOWN)

        # Optimization Function
        optFuncLabel = Text(t.optFuncLabel, font='CMU Serif').to_edge(UP)
        optFuncL = MathTex(t.optFuncL)
        optFuncX = MathTex(t.optFuncX)
        optFuncSimp = MathTex(t.optFuncSimp)

        # Range of x
        rangeOfX = Text(t.rangeOfX, font='CMU Serif').to_edge(UP)
        rangeFact1 = Text(t.rangeFact1, font='CMU Serif', font_size=24).next_to(rangeOfX, DOWN, buff=0.2)
        rangeFact2 = Text(t.rangeFact2, font='CMU Serif', font_size=24).next_to(rangeOfX, DOWN, buff=0.2)
        rf1eq = MathTex(t.rf1eq)
        rf2eqA = MathTex(t.rf2eqA)
        rf2eqB = MathTex(t.rf2eqB).next_to(rf2eqA, DOWN, buff=0.2)
        rf2eqC = MathTex(t.rf2eqC).next_to(rf2eqB, DOWN, buff=0.2)
        rf2eqD = MathTex(t.rf2eqD).next_to(rf2eqC, DOWN, buff=0.2)
        finalRange = MathTex(t.finalRange)

        # Derivative
        derivativeOfFunc = Text(t.derivativeOfFunc, font='CMU Serif').to_edge(UP)
        dxOfVx = MathTex(t.dxOfVx)

        # Critical Values
        criticalPoint = Text(t.criticalPoint, font='CMU Serif').to_edge(UP)
        cvPrompt = MathTex(t.cvPrompt)
        equateTo0 = MathTex(t.equateTo0)
        xValues = MathTex(t.xValues)
        removeX2 = Tex(t.removeX2, font_size=24).next_to(equateTo0, DOWN, buff=0.2)
        x1 = MathTex(t.x1)

        # Value of X
        valueOfX = Text(t.valueOfX, font='CMU Serif').to_edge(UP)
        finalXValue = MathTex(t.finalXValue)
        finalXValueMeaning = Text(t.finalXValueMeaning, font='CMU Serif',font_size=24).next_to(finalXValue, DOWN, buff=0.2)

        # Max Volume
        maxVolume = Text(t.maxVolume, font='CMU Serif').to_edge(UP)
        maxVolume1 = MathTex(t.maxVolume1)
        maxVolume2 = MathTex(t.maxVolume2)
        maxVolumeValue = MathTex(t.maxVolumeValue)

        # Rendering
        self.next_section("Problem")
        self.play(Write(problemHeader))
        self.wait()
        self.play(problemHeader.animate.to_edge(UP))
        self.wait()
        self.play(Write(problem))
        self.wait(3)
        self.play(FadeOut(problemHeader), FadeOut(problem))
        self.wait(3)

        self.next_section("Images")
        self.play(FadeIn(b1t, b1))
        self.wait(2)
        self.play(FadeOut(b1t, b1), FadeIn(b2t, b2))
        self.wait(2)
        self.play(FadeOut(b2t, b2), FadeIn(b3t, b3))
        self.wait(2)
        self.play(FadeOut(b3t, b3), FadeIn(at, a))
        self.wait(2)
        self.play(FadeOut(at, a))
        self.wait(3)

        self.next_section("Optimization Function")
        self.play(Write(optFuncLabel))
        self.wait()
        self.play(Write(optFuncL))
        self.wait()
        self.play(ReplacementTransform(optFuncL, optFuncX))
        self.wait(2)
        self.play(ReplacementTransform(optFuncX, optFuncSimp))
        self.wait(2)
        self.play(FadeOut(optFuncLabel), FadeOut(optFuncSimp))
        self.wait()

        self.next_section("Range")
        self.play(Write(rangeOfX))
        self.wait()
        self.play(Write(rangeFact1))
        self.wait()
        self.play(Write(rf1eq))
        self.wait(2)
        self.play(FadeOut(rangeFact1,rf1eq))
        self.wait()
        self.play(Write(rangeFact2))
        self.wait()
        self.play(Write(
            VGroup(rf2eqA, rf2eqB, rf2eqC, rf2eqD)
        ))
        self.wait(3)
        self.play(FadeOut(rangeFact2, rf2eqA, rf2eqB, rf2eqC, rf2eqD))
        self.wait()
        self.play(Write(finalRange))
        self.wait(2)
        self.play(FadeOut(rangeOfX,finalRange))
        self.wait(3)

        self.next_section("Derivative")
        self.play(Write(derivativeOfFunc))
        self.wait()
        self.play(Write(optFuncSimp))
        self.wait()
        self.play(ReplacementTransform(optFuncSimp, dxOfVx))
        self.wait(2)
        self.play(FadeOut(derivativeOfFunc, dxOfVx))
        self.wait(3)

        self.next_section("Critical Values")
        self.play(Write(criticalPoint))
        self.wait()
        self.play(Write(cvPrompt))
        self.wait()
        self.play(ReplacementTransform(cvPrompt, equateTo0))
        self.wait()
        self.play(ReplacementTransform(equateTo0, xValues))
        self.wait()
        self.play(Write(removeX2))
        self.wait()
        self.play(FadeOut(removeX2))
        self.play(ReplacementTransform(xValues,x1))
        self.wait(2)
        self.play(FadeOut(criticalPoint, x1))
        self.wait(3)

        self.next_section("Value of X")
        self.play(Write(valueOfX))
        self.wait()
        self.play(Write(finalXValue))
        self.wait(2)
        self.play(Write(finalXValueMeaning))
        self.wait(2)
        self.play(FadeOut(valueOfX, finalXValue, finalXValueMeaning))
        self.wait(3)

        self.next_section("Max Volume")
        self.play(Write(maxVolume))
        self.wait()
        self.play(Write(maxVolume1))
        self.wait()
        self.play(ReplacementTransform(maxVolume1, maxVolume2))
        self.wait()
        self.play(ReplacementTransform(maxVolume2, maxVolumeValue))
        self.wait(2)
        self.play(FadeOut(maxVolume, maxVolumeValue))
        self.wait(3)

class credits(Scene):
    def construct(self):
        # Credits
        creditsHeader = Text("Thank you for listening!", font='CMU Serif')
        voiceover = Text(t.voiceover, font='CMU Serif', font_size=36)
        videoEditor = Text(t.videoEditor, font='CMU Serif', font_size=36)
        script = Text(t.script, font='CMU Serif', font_size=36)
        
        self.next_section("Credits")
        self.wait()
        self.play(Write(creditsHeader))
        self.wait()
        self.play(creditsHeader.animate.to_edge(UP))
        self.wait()
        self.play(Write(voiceover))
        self.wait(3)
        self.play(FadeOut(voiceover))
        self.wait()
        self.play(Write(script))
        self.wait(3)
        self.play(FadeOut(script))
        self.wait()
        self.play(Write(videoEditor))
        self.wait(3)
        self.play(FadeOut(videoEditor))
        self.wait()
        self.play(FadeOut(creditsHeader))
        self.wait(3)
        