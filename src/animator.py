from components.cube import Cube
from components.point import Point
from components.rotation import Rotation
from components.figure import Figure
from drawer import Drawer


class FigureAnimator:
    frame_amount: int
    delay:  float
    
    def __init__(self, duration_in_sec: float, delay: float = 0.1):
        self.frame_amount = int( duration_in_sec // delay)
        self.delay = delay
                
    def animate_sequence_01(self, figure: Figure, drawer: Drawer):
        rotation = Rotation(Point(1,1,1), 2)
        drawer.open_file()
        for i in range(self.frame_amount):
            drawer.draw_figure(figure)
            drawer.draw_delay(self.delay)
            drawer.clean_screen()
            figure.apply_rotation(rotation)
        drawer.close_file()
        
    def animate_sequence_02(self, figure: Figure, drawer: Drawer):
        rotation = Rotation(Point(1,1,1), 2)
        drawer.open_file()
        for i in range(self.frame_amount):
            drawer.reset_hidden_lines(figure)
            drawer.draw_figure(figure)
            drawer.draw_delay(self.delay)
            drawer.clean_screen()
            figure.apply_rotation(rotation)
        drawer.close_file()
        