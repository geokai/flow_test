"""Tutorial for the use of Circuituous, Circle.area method"""

from circuituous import Circle

print()
print('Circuituous version', Circle.version)

c = Circle(10)

print('To find the area of a circle:')
print('A circle of radius', c.radius)
print('has an area of', c.area())
print()

print('To find the perimeter of a circle:')
print('A circle of radius', c.radius)
print('has an perimeter of', c.perimeter())
print()
