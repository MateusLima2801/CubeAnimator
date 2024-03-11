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
            self.p2.normalize()
        elif self.p2.is_origin():
            self.p1.normalize()
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
            return  (self.p2-self.p1) / norm

    def get_point_projection(self, p: Point) -> Point:
        dir = self.get_unitary_direction()
        return dir * (dir.vectorial_product(p) / dir.vectorial_product(dir))
    
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
        return v * (p.vectorial_product(v) / v.vectorial_product(v) ) + self.p2
    
    def to_2D_string(self):
        return f"{self.p1.x} {self.p1.y} {self.p2.x} {self.p2.y}"
    
def are_lines_crossing(l1: Line, l2: Line) -> bool:
    n1, n2 = get_normal_components_of_extremes(l1, l2)
    n3, n4 = get_normal_components_of_extremes(l2, l1)
    if n1.is_origin() or n2.is_origin or n3.is_origin() or n4.is_origin():
        return False
    return n1.vectorial_product(n2) < 0 or n3.vectorial_product(n4) < 0 
        
def get_normal_components_of_extremes(l1: Line, l2: Line) -> list[Point]: 
        n1 = l1.get_normal_component_of_point(l2.p1)
        n2 = l1.get_normal_component_of_point(l2.p2)
        return n1, n2

def check_intersection(line1: Line, line2: Line):
    # Extract points
    x1, y1 = line1.p1.x, line1.p1.y
    x2, y2 = line1.p2.x, line1.p2.y
    x3, y3 = line2.p1.x, line2.p1.y
    x4, y4 = line2.p2.x, line2.p2.y

    # Calculate slopes
    slope1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
    slope2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else float('inf')

    # Check if lines are parallel
    if abs(slope1 - slope2) > 10**(-6): return False

    # Calculate intersection point
    div = ((y2 - y1) * (x4 - x3) - (y4 - y3) * (x2 - x1))
    if div == 0: return False
    intersection_x = ((x2*y1 - y2*x1) * (x4 - x3) - (x4*y3 - y4*x3) * (x2 - x1)) / div
    intersection_y = ((x2*y1 - y2*x1) * (y4 - y3) - (x4*y3 - y4*x3) * (y2 - y1)) / (-div)

    # Check if intersection point lies within the line segments
    if min(x1, x2) <= intersection_x <= max(x1, x2) and \
       min(y1, y2) <= intersection_y <= max(y1, y2) and \
       min(x3, x4) <= intersection_x <= max(x3, x4) and \
       min(y3, y4) <= intersection_y <= max(y3, y4):
        return True  # Lines intersect
    else: return False  # Lines do not intersect 