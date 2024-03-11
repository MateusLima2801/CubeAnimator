from components.line import Line, calculate_points, equal
from components.point import Point


class PolygonalSurface:
    lines: list[Line]
    points: list[Point]
    normal_vector: Point
    center: Point
    draw: bool = False
    
    def __init__(self, lines: list[Line], normal_vector: Point = None) -> None:
        if len(lines) < 3:
            raise Exception("A polygonal surface must have at least 3 lines contouring it.")
        self.lines = lines
        self.points = calculate_points(lines)
        self.center = Point.calculate_centroid(self.points)
        self.normal_vector = normal_vector
        
    def calculate_normal_vector(self, figure_centroid: Point):
        v1 = self.lines[0]
        v2: Line
        principal = self.center - figure_centroid
        for line in self.lines[1:]:
            if line.p1 == v1.p1 or line.p2 == v1.p2:
                v2 = line
        v1, v2 = v1.get_unitary_direction(), v2.get_unitary_direction()
        comp1, comp2 = v1.get_point_projection(principal), v2.get_point_projection(principal)
        normal_vector = principal - comp1 - comp2
        self.normal_vector = normal_vector
        
    def contains_line(self, line: Line):
        for l in self.lines:
            if equal(l, line): return True
        return False