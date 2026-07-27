#class line:
    #def __init__(self, cord1, cord2):
    #    self.cord1 = cord1
   #     self.cord2 = cord2

  #  def distance(self):
  #      return ((self.cord1[0] - self.cord1[1])**2 + (self.cord2[0] - self.cord2[1])**2)**0.5
    
  #  def slope(self):
 #       return ((self.cord2[1]-self.cord2[0])/(self.cord1[1]-self.cord1[0]))
    

#print(line((3,2),(8,0)).distance())
#print(line((2,5),(2,7)).slope())

class cylinder:
    pi=3.14
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
    
    def __str__(self):
            return f'cylinder with height: {self.height} and radius: {self.radius}'

    def volume(self):
        return f'Volume is: {self.pi * self.radius**2 * self.height}'

    def surface_area(self):
        return f'surface area is: {2 * self.pi * self.radius * (self.radius + self.height)}'
    
print(str((cylinder(4,7))))
print((cylinder(4,7)).volume())
print((cylinder(4,7)).surface_area())