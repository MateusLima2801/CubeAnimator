from components.point import Point

class Line:
    p1: Point
    p2: Point
    draw: bool = True
    
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
        
    def passes_by_origin(self) -> bool:
        return self.p1.is_multiple(self.p2)
    
    def normalize(self):
        if self.p1.is_origin():
            self.p2 = self.p2.normalize()
        elif self.p2.is_origin():
            self.p1 = self.p1.normalize()
        else:
            norm = self.get_segment_size()
            self.p2 = self.p1 + (self.p2-self.p1) / norm
    
    def get_unitary_direction(self) -> Point:
        if self.p1.is_origin():
            return self.p2.normalize()
        elif self.p2.is_origin():
            return self.p1.normalize()
        else:
            norm = self.get_segment_size()
            return  (self.p2-self.p1).__div__(norm)

    def get_point_projection(self, p: Point) -> Point:
        dir = self.get_unitary_direction()
        return dir * (dir.escalar_product(p) / dir.escalar_product(dir))
    
    def get_segment_size(self) -> float:
        return (self.p1-self.p2).get_norm()
    
    def set_draw(self, draw: bool):
        self.draw = draw
        
    def get_normal_component_of_point(self, p: Point):
        if self.p1 == self.p2: 
            if p.is_origin(): return p
            else: return p.__div__( p.get_norm() )
        else: return p - self.get_projection_of_point(p)
    
    def get_projection_of_point(self, p: Point):
        v = self.p1 - self.p2
        return v * (p.escalar_product(v) / v.escalar_product(v) ) + self.p2
    
    def to_2D_string(self):
        return f"{self.p1.x} {self.p1.y} {self.p2.x} {self.p2.y}"
    
def equal(l1: Line, l2: Line):
    return ( l1.p1 == l2.p1 and l1.p2 == l2.p2 ) or ( l1.p2 == l2.p1 and l1.p1 == l2.p2 ) 
    
@staticmethod
def calculate_points(lines: list[Line]):
    points = []
    for l in lines:
        if l.p1 not in points:
            points.append(l.p1)
            
        if l.p2 not in points:
            points.append(l.p2)
    return points
    
    