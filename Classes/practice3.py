class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return 22.0/7.0 * self.radius ** 2 * self.height
    
    def surface_area(self):
        return 2 * 22.0/7.0 * self.radius * ( self.radius + self.height)
        

c = Cylinder(2,3)

print(c.volume())

print(c.surface_area())