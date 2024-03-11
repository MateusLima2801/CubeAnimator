import math
from components.line import Line
from components.point import Point

class Rotation:
    axis: Line
    angle: float
    mat: list[list[float]]
    
    def __init__(self, axis_reference: Point, angle: float) -> None:
        self.axis = Line(Point(0,0,0), axis_reference)
        self.angle = math.radians(angle)
        self.mat = self.calculate_matrix_rotating_around_origin()
    
    def calculate_matrix_rotating_around_origin(self) -> list[list[float]]:
        dir = self.axis.get_unitary_direction()
        cos = math.cos(self.angle)
        sin = math.sin(self.angle)
        
        return [[cos + (1-cos) * dir.x ** 2, dir.x*dir.y*(1-cos) - dir.z*sin, dir.x*dir.z*(1-cos)+dir.y*sin], 
                [dir.y*dir.x*(1-cos) + dir.z*sin, cos + (1-cos) * dir.y ** 2 ,dir.y*dir.z*(1-cos) - dir.x*sin], 
                [dir.z*dir.x*(1-cos) - dir.y*sin, dir.z*dir.y*(1-cos) + dir.x*sin, cos + (1-cos) * dir.z ** 2]]
        
    def apply_rotation(self, p: Point) -> Point:
        return Point(p.x * self.mat[0][0] + p.y * self.mat[0][1] + p.z*self.mat[0][2],
                     p.x * self.mat[1][0] + p.y * self.mat[1][1] + p.z*self.mat[1][2],
                     p.x * self.mat[2][0] + p.y * self.mat[2][1] + p.z*self.mat[2][2])
            
    def __mul__(self, times: float):
        return Rotation(self.axis, self.angle*times)