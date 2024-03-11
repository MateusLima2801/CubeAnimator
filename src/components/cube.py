
from components.point import Point
from components.figure import Figure

class Cube(Figure): 
    side: float
    
    def __init__():
        raise NotImplementedError()    

class SimplestCube(Cube):
    def __init__(self, side: float):
        if side == 0:
            raise ValueError("Side must be >= 0")
        self.side = side
        self.points = [ Point(0,0,0), Point(side,0, 0), Point(0,side,0),
                    Point(0,0,side), Point(side, side, 0), Point(side, 0, side),
                    Point(0, side, side), Point(side, side, side)]
        self.lines = Figure.generate_min_lines(self.points)
        
    
            