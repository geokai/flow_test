"""Circuituous, LLC -
   An Advanced Circle Analytics Company

"""


import math

class Circle(object):
    """An Advance circle analytical toolkit"""

    version = '0.0.3'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Perform quadrature on a shape of uniform radius"""
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        """Calculate the perimeter of a circle of radius R"""
        return 2.0 * math.pi * self.radius


class Tire(Circle):
    """Tires are circles with a corrected perimeter"""


    def perimeter(self):
        """Circumference corrected for the rubber"""
        return Circle.perimeter(self) * 1.25
