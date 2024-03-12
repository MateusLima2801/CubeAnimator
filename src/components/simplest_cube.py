
from components.point import Point
from components.figure import Figure
from components.polygonal_surface import PolygonalSurface

class SimplestCube(Figure):
    side: float
    
    def __init__(self, side: float):
        if side == 0:
            raise ValueError("Side must be >= 0")
        self.side = side
        self.points = [ Point(0,0,0), Point(side,0, 0), Point(0,side,0),
                    Point(0,0,side), Point(side, side, 0), Point(side, 0, side),
                    Point(0, side, side), Point(side, side, side)]
        self.lines = Figure.generate_min_lines(self.points)
        self.centroid = Point.calculate_centroid(self.points)
        self.surfaces = self.generate_surfaces(self.points)
        for i, surf in enumerate(self.surfaces):
            self.surfaces[i].calculate_normal_vector(self.centroid)
        
    def generate_surfaces(self, points: list[Point]) -> list[PolygonalSurface]:
        x_0, y_0, z_0, x_side, y_side, z_side = [],[],[],[],[],[]
        for p in points:
            if p.x == 0: x_0.append(p)
            else: x_side.append(p)
            if p.y == 0: y_0.append(p)
            else: y_side.append(p)
            if p.z == 0: z_0.append(p)
            else: z_side.append(p)
        return [PolygonalSurface(Figure.generate_min_lines(x_0)),
                PolygonalSurface(Figure.generate_min_lines(x_side)),
                PolygonalSurface(Figure.generate_min_lines(y_0)), 
                PolygonalSurface(Figure.generate_min_lines(y_side)),
                PolygonalSurface(Figure.generate_min_lines(z_0)), 
                PolygonalSurface(Figure.generate_min_lines(z_side))]
        
        
    
            