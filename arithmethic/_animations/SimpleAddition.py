from manim import *


class SimpleAddition(Scene):
    def construct(self):

        num1 = Tex("1")
        num2 = Tex("1")
        plus_sign = Tex("+")
        equal_sign = Tex("=")
        sum = Tex("2")

        num1.shift(LEFT)
        plus_sign.next_to(num1, RIGHT)
        num2.next_to(plus_sign, RIGHT)
        equal_sign.next_to(num2, RIGHT)
        sum.next_to(equal_sign, RIGHT)

        self.play(Write(num1))
        self.play(Write(plus_sign))
        self.play(Write(num2))
        self.play(Write(equal_sign))

        self.play(Write(sum))
