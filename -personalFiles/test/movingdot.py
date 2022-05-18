from manim import *

class UpdaterTypes(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        pointer = Arrow(ORIGIN, RIGHT).next_to(red_dot, LEFT)
        pointer.add_updater( # place arrow left of dot
            lambda mob: mob.next_to(red_dot, LEFT)
        )
    
        def shifter(mob, dt): #make the dot move
            mob.shift(RIGHT*dt*2)

        red_dot.add_updater(shifter)

        def scene_scaler(dt): #scale mobj depending on distance from origin
            for mob in self.mobjects:
                mob.set(width=2/(1 + np.linalg.norm(mob.get_center())))
        self.add_updater(scene_scaler)

        self.add(red_dot, pointer)
        self.update_self(0)
        self.wait(5)