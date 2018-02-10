"""Tutorial for the use of Circuituous, Circle.area method"""

from circuituous import Circle

print()
print('Circuituous version', Circle.version)

c = Circle(10)

print('A circle of radius', c.radius)
print('has an area of', c.area())
print()
