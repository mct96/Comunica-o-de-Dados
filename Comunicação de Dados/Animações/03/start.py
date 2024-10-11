from manim import *
import numpy as np

class SquareToCircle(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-7, 7],
            y_range=[-1, 1],
            axis_config={"include_numbers": True},)

        X = np.arange(-2, 2, 100)
        Y = np.sin(X)
        sin_function = ax.plot_line_graph(X, Y)
        
        self.add(ax, sin_function)
