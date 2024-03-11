from components.line import Line
from components.point import Point
from components.rotation import Rotation

class Transformator:
    @staticmethod
    def translate_point(p: Point, translation: Point) -> Point:
        return p + translation
    
    @staticmethod
    def translate_line(l: Line, translation: Point) -> Line:
        l.p1 = Transformator.translate_point(l.p1, translation)
        l.p2 = Transformator.translate_point(l.p2, translation)
        return l
    
    @staticmethod
    def rotate_point(p: Point, rotation: Rotation) -> Point:
        return  rotation.apply_rotation(p)
    
    @staticmethod
    def rotate_line(l: Line, rotation: Rotation) -> Line:
        return Line(Transformator.rotate_point(l.p1, rotation), Transformator.rotate_point(l.p2, rotation))
    
    @staticmethod
    def project_point_with_perspective(p: Point, focus_distance: float)-> Point:
        factor = focus_distance / ( p.z + focus_distance )
        return Point(p.x * factor, p.y * factor, 0)
    
    @staticmethod
    def project_line_with_perspective(l: Line, focus_distance: float) -> Line:
        p1 = Transformator.project_point_with_perspective(l.p1, focus_distance)
        p2 = Transformator.project_point_with_perspective(l.p2, focus_distance)
        return Line(p1,p2)
    
    @staticmethod
    def project_point_orthogonally(p: Point)-> Point:
        return Point(p.x, p.y, 0)
    
    @staticmethod
    def project_line_orthogonally(l: Line) -> Line:
        p1 = Transformator.project_point_orthogonally(l.p1)
        p2 = Transformator.project_point_orthogonally(l.p2)
        return Line(p1,p2)
        