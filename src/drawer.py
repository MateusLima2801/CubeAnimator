
from io import TextIOWrapper
from components.figure import Figure
from components.line import Line, are_lines_crossing, check_intersection
from components.point import Point
from components.transformator import Transformator


class Drawer:
    output_name: str
    output: TextIOWrapper
    
    def __init__(self, output_name: str):
        self.output_name = output_name
        
    def open_file(self):
        self.output = open(self.output_name, "w")
    
    def close_file(self):
        self.output.close()
    
    def draw_line(self, line: Line):
        if not line.draw: return
        self.output.write(f"line\n{self.get_projection_str(line)}\n")
        
    def draw_figure(self, figure: Figure):
        for line in figure.lines:
            self.draw_line(line)
            
    def draw_delay(self, delay: float):
        self.output.write(f"delay\n{delay}\n")
        
    def clean_screen(self):
        self.output.write(f"clrscr\n")
        
    def get_projection_str(self, l: Line):
        proj = self.project_line(l)
        return proj.to_2D_string()
    
    def reset_hidden_lines(self, figure: Figure):
        figure.set_figure_lines()
        figure.lines.sort(key=lambda l: max(l.p1.z, l.p2.z), reverse=True)
        projected_figure = self.get_projected_figure(figure)
        
        for i, l in enumerate(projected_figure.lines):
            if l.get_segment_size() == 0:
                figure.lines[i].set_draw(False)
                
        for i, l1 in enumerate(projected_figure.lines):
            for j, l2 in enumerate(projected_figure.lines[i+1:]):
                if figure.lines[i].draw == False: break
                if figure.lines[i+j+1].draw and check_intersection(l1, l2):
                    figure.lines[i+j+1].set_draw(False)
 
    def get_projected_figure(self, figure: Figure) -> Figure:
        lines = figure.lines.copy()
        for j, line in enumerate(lines):
            lines[j] = self.project_line(line)
        return Figure(lines)
    
    def project_line(self, l: Line) -> Line:
        raise NotImplementedError()   
        
class OrthoDrawer(Drawer):
    
    def __init__(self, output_name: str):
        super().__init__(output_name)
    
    def project_line(self, l: Line) -> Line:
        return Transformator.project_line_orthogonally(l)
    
class PerspectiveDrawer(Drawer):
    focus_distance: float 
    
    def __init__(self, output_name: str, focus_distance: float):
        super().__init__(output_name)
        self.focus_distance = focus_distance
        
    def project_line(self, l: Line) -> Line:
        return Transformator.project_line_with_perspective(l,self.focus_distance)
    
    
    
