class Line:
    
    def __init__(self,coor1,coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]

        self.x2 = coor2[0]
        self.y2 = coor2[1]
    
    def distance(self):
        ycord = (self.y2-self.y1) ** 2
        xcord = (self.x2-self.x1) ** 2

        return (xcord + ycord) ** 0.5

    
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)


coordinate1 = (3.0,2.0)
coordinate2 = (8.0,10.0)

li = Line(coordinate1,coordinate2)

print(li.distance())

print(li.slope())