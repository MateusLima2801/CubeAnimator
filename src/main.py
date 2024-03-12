
from animator import FigureAnimator
from components.cube import SimplestCube
from components.point import Point
from drawer import OrthoDrawer, PerspectiveDrawer


def main():
    generate_animation_01()
    generate_animation_02()
    generate_animation_03()
    generate_animation_04()
    
def generate_animation_01():
    cube = SimplestCube(0.5)
    drawer = OrthoDrawer("src\drawing_annotations\\animation01.txt")
    animator = FigureAnimator(60)
    animator.animate_sequence_01(cube, drawer)

def generate_animation_02():
    cube = SimplestCube(0.5)
    drawer = OrthoDrawer("src\drawing_annotations\\animation02.txt")
    animator = FigureAnimator(60)
    animator.animate_sequence_02(cube, drawer)
    
def generate_animation_03():
    cube = SimplestCube(0.5)
    drawer = PerspectiveDrawer("src\drawing_annotations\\animation03.txt", -1.5)
    animator = FigureAnimator(60)
    animator.animate_sequence_01(cube, drawer)
    
def generate_animation_04():
    cube = SimplestCube(0.5)
    drawer = PerspectiveDrawer("src\drawing_annotations\\animation04.txt", -1.5)
    animator = FigureAnimator(60)
    animator.animate_sequence_02(cube, drawer)
    
if __name__ == "__main__":
    main()