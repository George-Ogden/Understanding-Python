from manim import *
import numpy as np

class IntroScene(Scene):
    def construct(self):
        title = Text("Lesson 98 - manim").move_to(DOWN * 1)
        banner = ManimBanner().move_to(UP)
        self.play(banner.create(),Write(title))
        self.play(banner.expand())
        self.wait()


class MainScene(Scene):
    def construct(self):
        shape = Square()
        new_shape = Triangle(stroke_color=WHITE).move_to(RIGHT * 4)
        self.play(Create(shape))
        self.play(Rotate(shape, np.pi))
        # self.play(shape.animate.rotate(np.pi))
        self.play(shape.animate.move_to(new_shape))
        # self.add(new_shape)
        self.play(Transform(shape, new_shape))
        self.play(shape.animate.set_color(PURPLE))
        self.play(shape.animate.move_to(shape.get_center() + UP * 2))
        self.play(shape.animate.move_to(ORIGIN))
        self.play(Uncreate(shape))


class DotScene(Scene):
    def construct(self):
        dot = Dot()
        title = Title("dot")
        tracker = ValueTracker(0)
        self.play(FadeIn(title, shift=DOWN))
        self.add(dot, tracker)
        dot.add_updater(lambda dot : dot.move_to(tracker.get_value() * RIGHT))
        self.play(tracker.animate.set_value(-6), run_time=5)
        self.play(tracker.animate.set_value(6), rate_func=linear, run_time=3)
        self.play(tracker.animate.set_value(0))
        self.play(Uncreate(dot))