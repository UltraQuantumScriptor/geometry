import sys

file_path = sys.path.insert(1, "C:\\Users\\Sohaib\\Desktop\\cpython-main\\Lib\\geometry.py")

import math

class Area:

    def square(self, length):
        return length * length
    
    def rectangle(self, length, width):
        return length * width
    
    def triangle(self, base, height):
        return 0.5 * base * height
    
    def circle(self, radius):
        return math.pi * radius ** 2
    
    def ellipse(self, major_axis, minor_axis):
        return math.pi * major_axis * minor_axis
    
    def trapezoid(self, base1, base2, height):
        return 0.5 * (base1 + base2) * height
    
    def parallelogram(self, base, height):
        return base * height
    
    def hexagon(self, side_length):
        return 3 * math.sqrt(3) / 2 * side_length ** 2
    
    def pentagon(self, side_length):
        return (25 / 24) * math.sqrt(5) * (side_length ** 2)
    
    def octagon(self, side_length):
        return (25 / 12) * math.sqrt(2) * (side_length ** 2)
    
    def decagon(self, side_length):
        return (35 / 2) * side_length ** 2
    
    def polygon(self, sides, side_length):
        return (sides / 2) * side_length ** 2
    
    def equilateral_triangle(self, side_length):
        return (math.sqrt(3) / 4) * side_length ** 2
    
    def isosceles_triangle(self, side1, side2, base):
        if side1 == side2:
            return 0.5 * self.triangle(side1, (side1 + base) / 2)
        else:
            return self.triangle(side1, (side1 + side2) / 2)
        
    def right_triangle(self, side1, side2):
        return math.sqrt(side1 ** 2 + side2 ** 2)
    
    def equilateral_triangle_area(self, side_length):
        return (math.sqrt(3) / 4) * side_length ** 2
    
    def isosceles_triangle_area(self, side1, side2, base):
        if side1 == side2:
            return 0.5 * self.triangle(side1, (side1 + base) / 2)
        else:
            return self.triangle(side1, (side1 + side2) / 2)
        
    def right_triangle_area(self, side1, side2):
        return math.sqrt(side1 ** 2 + side2 ** 2)
    
    def scalene_triangle_area(self, side1, side2, side3):
        semi_perimeter = (side1 + side2 + side3) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    
    def cuboid(self, length, width, height):
        return length * width * height
    
    def cube(self, side_length):
        return side_length ** 3
    
    def sphere(self, radius):
        return (4 / 3) * math.pi * radius ** 3
    
    def cylinder(self, radius, height):
        return math.pi * radius ** 2 * height
    
    def cone(self, radius, height):
        return (1 / 3) * math.pi * radius ** 2 * height
    
    def pyramid(self, base_area, height):
        return 0.5 * base_area * height
        
    def frustum(self, major_radius1, major_radius2, minor_radius, height):
        return math.pi * (major_radius1 ** 2 + major_radius1 * minor_radius + major_radius2 ** 2 + major_radius2 * minor_radius) / 3 * height
    
    def torus(self, major_radius, minor_radius):
        return 2 * math.pi ** 2 * major_radius * minor_radius
    
    def tetrahedron(self, side_length):
        return (math.sqrt(24 + 10 * math.sqrt(6)) / 6) * side_length ** 3
    
    def octahedron(self, side_length):
        return (2 + math.sqrt(2)) / 4 * side_length ** 3
    
    def dodecahedron(self, side_length):
        return (1 + 2 * math.sqrt(5)) / 4 * side_length ** 3
    
    def icosahedron(self, side_length):
        return (5 * (3 + 2 * math.sqrt(5))) / 4 * side_length ** 3
    
    def polyhedron(self, vertices, edges, faces):
        return (vertices * (vertices - 3)) / 6 + (edges * (edges - 3)) / 2 - (faces * (faces - 3))
    
    def frustum_of_pyramid(self, base_area, slant_height, height):
        return 0.5 * base_area * slant_height + 0.5 * self.pyramid(base_area, height)
    
    def frustum_of_cone(self, major_radius1, major_radius2, slant_height, height):
        return (math.pi * (major_radius1 ** 2 + major_radius1 * major_radius2 + major_radius2 ** 2) / 3) * slant_height + 0.5 * self.cone(major_radius1, height) + 0.5 * self.cone(major_radius2, height)
    
    def frustum_of_torus(self, major_radius, minor_radius, slant_height):
        return (math.pi ** 2 * major_radius * minor_radius) * slant_height / 2
    
    def frustum_of_frustum(self, major_radius1, major_radius2, minor_radius, slant_height, height1, height2):
        return (math.pi * (major_radius1 ** 2 + major_radius1 * minor_radius + major_radius2 ** 2 + major_radius2 * minor_radius) / 3) * slant_height + 0.5 * self.frustum(major_radius1, major_radius2, minor_radius, height1) + 0.5 * self.frustum(major_radius1, major_radius2, minor_radius, height2)
    
    def frustum_of_pyramid_and_cone(self, base_area, slant_height, height, major_radius, height2):
        return 0.5 * base_area * slant_height + 0.5 * self.pyramid(base_area, height) + 0.5 * self.cone(major_radius, height2)
    
    def frustum_of_pyramid_and_torus(self, base_area, slant_height, height, major_radius, minor_radius):
        return 0.5 * base_area * slant_height + 0.5 * self.pyramid(base_area, height) + 0.5 * self.torus(major_radius, minor_radius)
    
    def frustum_of_pyramid_and_frustum(self, base_area, slant_height, height, major_radius1, major_radius2, minor_radius, height2):
        return 0.5 * base_area * slant_height + 0.5 * self.pyramid(base_area, height) + 0.5 * self.frustum(major_radius1, major_radius2, minor_radius, height2)
    
    def frustum_of_cone_and_torus(self, major_radius1, major_radius2, slant_height, height, major_radius, minor_radius):
        return (math.pi * (major_radius1 ** 2 + major_radius1 * major_radius2 + major_radius2 ** 2) / 3) * slant_height + 0.5 * self.cone(major_radius1, height) + 0.5 * self.torus(major_radius, minor_radius)

class Perimeter:

    def square(self,length):
        return 4 * length
    
    def rectangle(self, length, width):
        return 2 * (length + width)
    
    def triangle(self, base, side1, side2):
        if side2 < side1+base:
            return side1+base+side2
        else:
            return "Error: Invalid triangle"
        
    def parallelogram(self, base, height):
        return 2 * (base + height)
    
    def trapezoid(self, base1, base2, height):
        return base1 + base2 + 2 * math.sqrt((base1 - base2) ** 2 + height ** 2)
        
    def pentagon(self, side_length):
        return 5 * side_length
    
    def hexagon(self, side_length):
        return 6 * side_length
    
    def septagon(self, side_length):
        return 7 * side_length
    
    def octagon(self, side_length):
        return 8 * side_length
    
    def nonagon(self, side_length):
        return 9 * side_length
    
    def decagon(self, side_length):
        return 10 * side_length
    
    def polygon(self, sides, side_length):
        return sides * side_length
    
area = Area()
perimeter = Perimeter()