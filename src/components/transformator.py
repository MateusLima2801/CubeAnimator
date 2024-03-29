from components.line import Line
from components.point import Point
from components.polygonal_surface import PolygonalSurface
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
    def rotate_surface(s: PolygonalSurface, rotation: Rotation) -> PolygonalSurface:
        lines = []
        for l in s.lines:
            lines.append(Transformator.rotate_line(l, rotation))
        return PolygonalSurface(lines)
    
    @staticmethod
    def project_point_with_perspective(p: Point, focus_distance: float, unproject: bool = False)-> Point:
        z = 0
        if unproject: z = p.z
        factor = focus_distance / ( p.z + focus_distance )
        return Point(p.x * factor, p.y * factor, z)
    
    @staticmethod
    def project_line_with_perspective(l: Line, focus_distance: float, unproject: bool = False) -> Line:
        p1 = Transformator.project_point_with_perspective(l.p1, focus_distance, unproject)
        p2 = Transformator.project_point_with_perspective(l.p2, focus_distance, unproject)
        return Line(p1,p2,l.draw)
    
    @staticmethod
    def project_point_orthogonally(p: Point, unproject: bool = False)-> Point:
        z = 0
        if unproject: z = p.z
        return Point(p.x, p.y, z)
    
    @staticmethod
    def project_line_orthogonally(l: Line, unproject: bool = False) -> Line:
        p1 = Transformator.project_point_orthogonally(l.p1, unproject)
        p2 = Transformator.project_point_orthogonally(l.p2, unproject)
        return Line(p1,p2)
        