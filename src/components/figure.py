from numpy import mean
from components.polygonal_surface import PolygonalSurface
from components.rotation import Rotation
from components.line import Line, calculate_points
from components.point import Point
from components.transformator import Transformator

class Figure:
    lines: list[Line]
    points: list[Point]
    centroid: Point
    surfaces: list[PolygonalSurface]
    
    def __init__(self, lines: list[Line]):
        self.lines = lines
        self.points = calculate_points(lines)
        self.centroid = Point.calculate_centroid(self.points)
        
    def apply_rotation(self, rotation: Rotation):
        for i, point in enumerate(self.points):
            self.points[i] = Transformator.rotate_point(point, rotation)
        
        self.centroid = Point.calculate_centroid(self.points)
    
        for j, line in enumerate(self.lines):
            self.lines[j] = Transformator.rotate_line(line, rotation)
            
        for j, surface in enumerate(self.surfaces):
            s = Transformator.rotate_surface(surface, rotation)
            s.calculate_normal_vector(self.centroid)
            self.surfaces[j] = s
            
    def apply_translation(self, translation: Point):
        for i, point in enumerate(self.points):
            self.points[i] = Transformator.translate_point(point, translation)
    
        for j, line in enumerate(self.lines):
            self.lines[j] = Transformator.translate_line(line, translation)
            
    def set_figure_lines(self, draw: bool = True):
        for i in range(len(self.lines)):
            self.lines[i].set_draw(draw)
            
    @staticmethod
    def generate_min_lines(points: list[Point]):
        lines_by_norm: dict[float, list] = {}
        for i, p1 in enumerate(points):
            for p2 in points[i+1:]:
                if p1 == p2: continue
                l = Line(p1,p2)
                size = l.get_segment_size()
                if size not in lines_by_norm.keys():
                    lines_by_norm[size] = []
                lines_by_norm[size].append(l)
        side = min(lines_by_norm.keys())
        return lines_by_norm[side]