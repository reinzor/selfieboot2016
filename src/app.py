'''
Selfiebooth Baas van Horst aan de Maas 2016 - CameraPuzzle
===========================

This demonstrates using Scatter widgets with a live camera.
You should see a shuffled grid of rectangles that make up the
camera feed. You can drag the squares around to see the
unscrambled camera feed or double click to scramble the grid
again.
'''

from kivy.app import App
from kivy.uix.widget import Widget

from puzzle import Puzzle

class SelfieboothApp(App):
    def build(self):
        root = Widget()
        puzzle = Puzzle(resolution=(640, 480), play=True)

        root.add_widget(puzzle)

        return root

SelfieboothApp().run()
