"""Tutorial for the use of Circuituous, Circle.area method"""

from circuituous import Circle, Tire

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


print()
t = Tire(22)

print('To find the perimeter of a Tire:')
print('A tire of radius', t.radius)
print('has an inner area of', t.area())
print('and an odometer corrected perimeter or', t.perimeter())
print()
