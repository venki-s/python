class Circle():

    def __init__(self, radius):
        self.radius = radius
        

    def get_circumfrance(self):
        return 3.14 * self.radius ** 2

my_circle = Circle(4)

print(my_circle.get_circumfrance())

