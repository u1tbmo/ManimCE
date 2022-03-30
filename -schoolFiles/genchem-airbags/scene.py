from manim import *

class Intro(MovingCameraScene):
    def construct(self):
        airbags = Tex("Airbags").scale(1.2)
        trials = Tex("Trials").scale(1.2)

        introGroup = VGroup(airbags,trials).arrange(DOWN,buff=1.5)

        self.next_section("Airbags")

        self.play(Write(airbags))
        self.wait(0.2)
        self.play(Write(trials))
        self.wait()

        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.set(width=airbags.width * 2.75).move_to(airbags))
        self.wait()
        self.play(FadeOut(introGroup))
        self.wait()

        self.play(Restore(self.camera.frame))

        self.next_section("Trials")

        self.play(Write(airbags))
        self.wait(0.2)
        self.play(Write(trials))
        self.wait()

        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.set(width=trials.width * 2.75).move_to(trials))
        self.wait()
        self.play(FadeOut(introGroup))
        self.wait()

        self.play(Restore(self.camera.frame))

class Airbags(MovingCameraScene):
    def construct(self):
        airbags = Tex("Airbags")
        flores = Tex("Flores").scale(1.25)
        floresRatio = Tex("20g Baking Soda, 30ml Vinegar").scale(0.75)
        dayao = Tex("Dayao").scale(1.25)
        dayaoRatio = Tex("30g Baking Soda, 40ml Vinegar").scale(0.75)

        self.next_section("Dayao")
        self.play(Write(dayao))
        self.wait()
        self.play(dayao.animate.to_edge(UP))
        self.wait()
        self.play(Write(dayaoRatio.next_to(dayao,DOWN)))
        self.wait(2)
        self.play(Unwrite(dayao), Unwrite(dayaoRatio))
        self.wait()

        self.next_section("Flores")
        self.play(Write(flores))
        self.wait()
        self.play(flores.animate.to_edge(UP))
        self.wait()
        self.play(Write(floresRatio.next_to(flores,DOWN)))
        self.wait(2)
        self.play(Unwrite(flores),Unwrite(floresRatio))
        self.wait()

class Trials(MovingCameraScene):
    def construct(self):
        trial1 = Tex("Trial 1")
        trial2 = Tex("Trial 2")
        flores = Tex("Flores").scale(1.25)
        floresRatio = Tex("20g Baking Soda, 30ml Vinegar").scale(0.75)
        dayao = Tex("Dayao").scale(1.25)
        dayaoRatio = Tex("30g Baking Soda, 40ml Vinegar").scale(0.75)

        self.camera.frame.save_state()

        self.next_section("Dayao Trial 1")

        self.play(Write(dayao))
        self.wait()
        self.play(dayao.animate.to_edge(UP))
        self.wait()
        self.play(Write(dayaoRatio.next_to(dayao,DOWN)))
        self.wait()
        self.play(Write(trial1.to_edge(DOWN)))
        self.wait(1)
        self.play(FadeOut(trial1))
        
        self.next_section("Dayao Trial 2")

        self.wait()
        self.play(Write(trial2.to_edge(DOWN)))
        self.wait(1)
        self.play(
            FadeOut(dayao),
            FadeOut(dayaoRatio),
            FadeOut(trial2)
        )

        self.next_section("Flores Trial 1")

        self.play(Write(flores))
        self.wait()
        self.play(flores.animate.to_edge(UP))
        self.wait()
        self.play(Write(floresRatio.next_to(flores,DOWN)))
        self.wait()
        self.play(Write(trial1.to_edge(DOWN)))
        self.wait(1)
        self.play(FadeOut(trial1))

        self.next_section("Flores Trial 2")

        self.wait()
        self.play(Write(trial2.to_edge(DOWN)))
        self.wait(1)
        self.play(
            FadeOut(flores),
            FadeOut(floresRatio),
            FadeOut(trial2)
        )
