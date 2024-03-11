from __future__ import annotations
from math import sqrt

class Point:
    x: float
    y: float
    z: float

    def __init__(self,  x:float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
          
    def __mul__(self, num: float) -> Point:
        return Point(self.x * num, self.y * num, self.z * num)
    
    def __div__(self, num: float | int) -> Point:
        if num == 0:
            raise ZeroDivisionError()
        return Point(self.x / num, self.y / num, self.z / num)
    
    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def is_origin(self):
        return self.x == 0 and self.y == 0 and self.z == 0
    
    def is_multiple(self, other: Point):
        cross_product = Point(self.y * other.z - self.z * other.y,
                              self.z * other.x - self.x * other.z,
                              self.x * other.y - self.y * other.x)
        return cross_product.is_origin()
    
    def get_norm(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self) -> Point:
        norm = self.get_norm()
        if norm > 0:
            return self.__div__(norm)
        else: return self
            
    def escalar_product(self, other: Point) -> float:
        return self.x *other.x + self.y * other.y + self.z * other.z
    
    def vectorial_product(self, other: Point) -> Point:
        return Point(self.y * other.z - other.y*self.z,
                     self.z * other.x - self.x * other.z,
                     self.x * other.y - self.y * other.z)
        
    def get_point_projection(self, p: Point) -> Point:
        if self.is_origin(): return self
        return self * (self.escalar_product(p) / self.escalar_product(self))
        
    @staticmethod
    def calculate_centroid(points: list[Point]):
        if points == None: return None
        centroid = Point(0,0,0)
        for p in points:
            centroid += p
        return centroid.__div__(len(points))
    
    def to_string(self):
        return f"( {self.x}, {self.y}, {self.z})"