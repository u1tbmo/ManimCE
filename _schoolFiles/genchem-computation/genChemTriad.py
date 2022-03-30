from manim import *

class GroupIntroVideo(Scene):
    def construct(self):
        
        #Objects
        group4 = Tex("Group 4 | STEM 11P", font_size=96, color=BLUE_A)
        tabamo = Tex("Tabamo, Euan Jed")
        mariano = Tex("Mariano, Eunice Reign")
        inocencio = Tex("Inocencio, John Ray")
        gayatin = Tex("Gayatin, Jyegan")

        #Mobjects
        set1 = Tex("Set 1")

        #VGroups
        group4Names = VGroup(tabamo, gayatin, mariano, inocencio).arrange(DOWN)

        #Animation
        self.camera.background_color = "#1e1e1e"
        self.play(
            DrawBorderThenFill(group4, run_time=2)
        )
        self.wait()
        self.play(Transform(group4,Title("Group 4 | STEM 11P", color=BLUE_A).scale(1.4).shift(DOWN*0.4)))
        self.wait()
        self.play(
            Write(group4Names, run_time=8)
        )
        self.wait(4)
        self.play(FadeOut(group4,group4Names))
        self.wait()

class Set1Problems(Scene):
    def construct(self):
        #ObjectsIntroEtc
        set1 = Tex("Set 1", color=BLUE_B, font_size=96)
        
        set1a = Tex("$3.51\cdot 10^{11}$ atoms of silver is equal to how many moles of silver?", font_size=28)
        set1b = Tex("Calculate the moles of $267.354g$ of $K_{2}CrO_{4}$", font_size=28)
        set1c = Tex("Calculate the mass of $4.721 moles$ of $HCN$", font_size = 28)
        
        pr1 = Tex("Problem A")
        pr2 = Tex("Problem B")
        pr3 = Tex("Problem C") 

        #MobjectsIntro
        avogadroNum = MathTex(r"6.022\cdot10^{23}\ atoms", font_size=26)
        grid = NumberPlane()
        
        #Mobjects1A
        atoms1a = MathTex(r"3.51\cdot10^{11}\ atoms", font_size=26)
        conversionA = Tex(r"Atoms $\cdot \frac{Moles}{ 6.022\cdot10^{23}\ Atoms}$ =\ Moles").scale(0.75)
        s1a = MathTex(r"3.51\cdot{10}^{11}\cdot\frac{mol}{ 6.022\cdot{10}^{23} }")
        s2a = MathTex(r"=\frac{3.51\cdot{10}^{11}}{6.022\cdot{10}^{23}}mol")
        s3a = MathTex(r"=\frac{3.51}{ 6.022\cdot{10}^{12} }mol")
        s4a = MathTex(r"=\frac{0.58286\ldots}{ {10}^{12} }mol")
        sRa = MathTex(r"\approx5.83\cdot{10}^{-13}\ mol")
        sRaCopy = sRa.copy().scale(1.5)

        #VGroups1A
        pr1a = VGroup(pr1,set1a).arrange(DOWN)
        sA = VGroup(s1a,s2a,s3a,s4a,sRa).arrange(DOWN).shift(DOWN*0.6,RIGHT*3)

        #AnimationIntro
        self.camera.background_color = "#1e1e1e"
        self.play(DrawBorderThenFill(set1,run_time=2))
        self.wait(0.2)
        self.play(Unwrite(set1))
        self.wait(2)

        #Animation1A
        self.next_section("Problem A")

        self.play(Write(pr1))
        self.wait()
        self.play(Write(set1a,run_time=2.5),)
        self.wait()
        self.play(pr1a.animate.to_edge(UP))
        self.wait(1.5)
        self.play(Write(conversionA))
        self.wait()
        self.play(conversionA.animate.to_edge(LEFT).shift(RIGHT*0.2))
        self.play(FadeIn(s1a, run_time=1.5),)
        self.wait(0.5)
        self.play(
            Indicate(conversionA),
            Indicate(s1a)
        )
        self.wait(2)
        self.play(Write(s2a, run_time=1.5))
        self.wait(0.5)
        self.play(TransformFromCopy(s2a, s3a, run_time=1.5))
        self.wait(0.5)
        self.play(TransformFromCopy(s3a, s4a, run_time=1.5))
        self.wait(0.5)
        self.play(TransformFromCopy(s4a, sRa, run_time=1.5))
        self.wait(0.5)
        self.play(ShowPassingFlash(Underline(sRa)))
        self.wait(2)
        self.play(
            TransformFromCopy(sRa, sRaCopy,run_time=1.5),
            FadeOut(conversionA, sA,run_time=0.5)
        )
        self.wait(2)
        self.play(
            FadeOut(sRaCopy),
            FadeOut(pr1a)
        )
        self.wait(1)
        
        self.next_section("Problem B")
        #Objects1B


        #Mobjects1B
        elemK = Tex("Molar Mass of K: ")
        elemCr= Tex("Molar Mass of Cr: ")
        elemO = Tex("Molar Mass of O: ")

        molMassElemK = MathTex(r"39.10g/mol")
        molMassElemCr = MathTex(r"52.00g/mol")
        molMassElemO = MathTex(r"16.00g/mol")
        
        multiplyK = MathTex(r"39.10g/mol \cdot 2")
        multiplyCr = MathTex(r"52.00g/mol \cdot 1")
        multiplyO = MathTex(r"16.00g/mol \cdot 4")

        finalK = MathTex(r"78.20g/mol")
        finalCr = MathTex(r"52.00g/mol")
        finalO = MathTex(r"64.00g/mol")

        ConversionB = Tex(r"Mass$\cdot\frac{Moles}{Mass}$ = Moles").scale(0.75)

        givenMoleculeA = MathTex("K_{2}CrO_{4}")
        givenMoleculeA.set_color_by_tex("K_{2}CrO_{4}", YELLOW)
        
        solutionB1_1 = MathTex(r"K_{2}CrO_{4}")
        solutionB1_2 = MathTex(r"194.20\frac{g}{mol}")

        solutionB2_1 = MathTex(r"267.354g\cdot\frac{mol}{194.20g}")
        solutionB2_2 = MathTex(r"=\frac{267.354}{194.20}mol")
        solutionB2_3 = MathTex(r"=1.37669mol")
        solutionB2_R = MathTex(r"\approx1.38mol")
        solutionB2_RCopy = solutionB2_R.copy().scale(1.5)

        #Groups1B
        pr2b = VGroup(pr2,set1b).arrange(DOWN)
        elem = VGroup(elemK, elemCr, elemO).arrange(DOWN)
        molMassElem = VGroup(molMassElemK, molMassElemCr, molMassElemO).arrange(DOWN)
        multiplyElem = VGroup(multiplyK, multiplyCr, multiplyO).arrange(DOWN)
        finalAdd = VGroup(finalK, finalCr, finalO).arrange(DOWN)
        solutionB2 = VGroup(solutionB2_1,solutionB2_2,solutionB2_3,solutionB2_R).arrange(DOWN).shift(RIGHT*3,DOWN*0.6)

        #Animation1B
        self.play(Write(pr2))
        self.wait()
        self.play(Write(set1b,run_time=2.5),)
        self.wait()
        self.play(pr2b.animate.to_edge(UP))
        self.wait(1)

        self.play(Write(solutionB1_1))
        self.wait()
        self.play(solutionB1_1.animate.next_to(pr2b,DOWN))
        self.wait()
        self.play(Write(elem,run_time=1.5))
        self.wait()
        self.play(elem.animate.to_edge(LEFT).shift(DOWN*0.8))
        self.wait()
        self.play(Write(molMassElem.next_to(elem, RIGHT),run_time=1.5))
        self.wait()
        self.play(ReplacementTransform(solutionB1_1, givenMoleculeA.next_to(pr2b,DOWN)))
        self.wait(0.4)
        self.play(ReplacementTransform(molMassElem, multiplyElem.next_to(elem,RIGHT)))
        self.wait()
        self.play(Circumscribe(solutionB1_1),Circumscribe(multiplyElem))
        self.wait(0.4)
        givenMoleculeA.set_color_by_tex("K_{2}CrO_{4}",WHITE)
        self.play(
            FadeOut(elem),
            FadeOut(solutionB1_1),
            ReplacementTransform(solutionB1_1.move_to(givenMoleculeA.get_center()),givenMoleculeA)
        )
        self.wait()
        self.play(ReplacementTransform(multiplyElem,finalAdd.shift(DOWN*0.8)))
        self.wait()
        self.play(ReplacementTransform(finalAdd,solutionB1_2.scale(1.4)))
        self.wait(2)
        self.play(solutionB1_2.animate.to_edge(LEFT).shift(UP*0.5,RIGHT*2).scale(0.75))
        self.wait()
        self.play(Write(ConversionB.next_to(solutionB1_2, DOWN*1.4)))
        self.wait(0.75)
        self.play(FadeIn(solutionB2_1))
        self.wait(0.5)
        self.play(
            Indicate(ConversionB),
            Indicate(solutionB1_2),
            Indicate(solutionB2_1)
        )
        self.wait(2)
        self.play(TransformFromCopy(solutionB2_1,solutionB2_2))
        self.wait(0.5)
        self.play(TransformFromCopy(solutionB2_2,solutionB2_3))
        self.wait(0.5)
        self.play(TransformFromCopy(solutionB2_3,solutionB2_R))
        self.wait()
        self.play(ShowPassingFlash(Underline(solutionB2_R)))
        self.wait(2)
        self.play(
            TransformFromCopy(solutionB2_R,solutionB2_RCopy,run_time=1.5),
            FadeOut(solutionB1_2,ConversionB,solutionB2,run_time=0.5)
        )
        self.wait(2)
        self.play(
            FadeOut(solutionB2_RCopy),
            FadeOut(givenMoleculeA),
            FadeOut(pr2b)
        )
        self.wait(1)

        self.next_section("Problem C")
        #Objects1C
        givenMoleculeB = Tex("HCN")
        elemH = Tex("Molar Mass of H: ")
        elemC = Tex("Molar Mass of C: ")
        elemN = Tex("Molar Mass of N: ")

        molMassElemH = MathTex(r"1.01g/mol")
        molMassElemC = MathTex(r"12.01g/mol")
        molMassElemN = MathTex(r"14.01g/mol")
        finalMolMassC = MathTex(r"27.12\frac{g}{mol}")

        ConversionC = MathTex(r"Moles\cdot\frac{Mass}{Moles}=Mass").scale(0.75)
        
        #MobObjects1C
        solutionC1 = MathTex(r"4.721\cdot\frac{27.12g}{mol}")
        solutionC2 = MathTex(r"=128.03352g")
        solutionC3 = MathTex(r"\approx128.03g")
        solutionC3Copy = solutionC3.copy().scale(1.5)
        
        #Group1C
        pr3c = VGroup(pr3,set1c).arrange(DOWN)
        elemCGroup = VGroup(elemH, elemC, elemN).arrange(DOWN)
        molMassElemCGroup = VGroup(molMassElemH, molMassElemC, molMassElemN).arrange(DOWN)
        solutionC = VGroup(solutionC1, solutionC2, solutionC3).arrange(DOWN).shift(RIGHT*3,DOWN*0.6)

        #Animation1C
        self.play(Write(pr3))
        self.wait()
        self.play(Write(set1c,run_time=2.5),)
        self.wait()
        self.play(pr3c.animate.to_edge(UP))
        self.wait(1)

        self.play(Write(givenMoleculeB))
        self.wait()
        self.play(givenMoleculeB.animate.next_to(pr3c,DOWN))
        self.wait()
        self.play(Write(elemCGroup,run_time=1.5))
        self.wait()
        self.play(elemCGroup.animate.to_edge(LEFT).shift(DOWN*0.8))
        self.wait()
        self.play(Write(molMassElemCGroup.next_to(elemCGroup, RIGHT)),run_time=1.5)
        self.wait()
        self.play(
            FadeOut(elemCGroup)
        )
        self.wait()
        self.play(molMassElemCGroup.animate.move_to(ORIGIN))
        self.wait()
        self.play(ReplacementTransform(molMassElemCGroup,finalMolMassC.scale(1.4)))
        self.wait()
        self.play(finalMolMassC.animate.to_edge(LEFT).shift(DOWN*0.5,RIGHT*2).scale(0.75))
        self.wait(0.75)
        self.play(Write(ConversionC.next_to(finalMolMassC,DOWN)))
        self.wait(0.5)
        self.play(FadeIn(solutionC1))
        self.wait(0.5)
        self.play(
            Indicate(ConversionC),
            Indicate(solutionC1),
            Indicate(finalMolMassC)
        )
        self.wait(2)
        self.play(TransformFromCopy(solutionC1,solutionC2))
        self.wait(0.5)
        self.play(TransformFromCopy(solutionC2,solutionC3))
        self.wait()
        self.play(ShowPassingFlash(Underline(solutionC3)))
        self.wait(2)
        self.play(
            TransformFromCopy(solutionC3, solutionC3Copy,run_time=1.5),
            FadeOut(solutionC, ConversionC, finalMolMassC,run_time=0.5)
        )
        self.wait(2)
        self.play(
            FadeOut(solutionC3Copy),
            FadeOut(givenMoleculeB),
            FadeOut(pr3c)
        )
        self.wait(1)

        self.next_section("End")
        thankYou = Tex("Thank You for Watching!").scale(1.5)
        thankYou.generate_target()
        thankYou.target.shift(UP*6)

        coder = Tex("Video by: Tabamo, Euan Jed S.")
        coder.generate_target()
        coder.target.shift(UP*6)

        compute = Tex("Computation by: Tabamo, Mariano, Inocencio, Gayatin")
        compute.generate_target()
        compute.target.shift(UP*6)

        codeUse = Tex("Animated using Manim Community Edition")
        codeUse.generate_target()
        codeUse.target.shift(UP*6)

        music =  Tex("Music from: The Music of 3Blue1Brown").scale(1.4)
        etude = Tex("Grant's Etude - Grant Sanderson").scale(0.85)
        newEtude = Tex("Grant's New Etude - Vincent Rubinetti · Grant Sanderson").scale(0.85)
        zeta = Tex("Zeta - Vincent Rubinetti").scale(0.85)
        oneTwoZeta = Tex("One, Two, Zeta - Vincent Rubinetti · Nathaniel Schroeder").scale(0.85)
        sixes = Tex("Sixes - Vincent Rubinetti").scale(0.85)

        musicGroup = VGroup(music,etude,newEtude,zeta,oneTwoZeta,sixes).arrange(DOWN)
        musicGroup.generate_target()
        musicGroup.target.shift(UP*10)

        self.play(
            DrawBorderThenFill(thankYou)
        )
        self.wait(2)
        self.play(
           MoveToTarget(thankYou)
        )
        self.wait(0.5)
        self.play(
            DrawBorderThenFill(coder),
            DrawBorderThenFill(codeUse.next_to(coder,DOWN))
        )
        self.wait(2)
        self.play(
            MoveToTarget(coder),
            MoveToTarget(codeUse)
        )
        self.wait(0.5)
        self.play(
            DrawBorderThenFill(compute)
        )
        self.wait(2)
        self.play(
            MoveToTarget(compute)
        )
        self.wait(0.5)
        self.play(
            DrawBorderThenFill(music)
        )
        self.wait(1)
        self.play(TransformFromCopy(music,etude))
        self.wait(0.4)
        self.play(TransformFromCopy(music,newEtude))
        self.wait(0.4)
        self.play(TransformFromCopy(music,zeta))
        self.wait(0.4)        
        self.play(TransformFromCopy(music,oneTwoZeta))
        self.wait(0.4)
        self.play(TransformFromCopy(music,sixes))
        self.wait(6)
        self.play(MoveToTarget(musicGroup))
        self.wait(2)

class BehindTheScenes(Scene):
    def construct (self):
        bts = Tex("Behind The Scenes")
        sideNoteBTS = Tex("mostly code...").scale(0.6)

        introBTS = VGroup(bts,sideNoteBTS).arrange(DOWN)

        self.play(DrawBorderThenFill(bts))
        self.wait(1.5)
        self.play(Write(sideNoteBTS))
        self.wait(2)
        self.play(Unwrite(introBTS))
        self.wait(1)