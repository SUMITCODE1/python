class Car:

    wheels = 4
    def __init__(self, color, style):
        self.color = color
        self.style = style

c = Car('Black', 'Sedan')
print(c.style)
print(c.color)
c.style = 'SUV'
print(c.style)