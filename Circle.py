class Circle():

  pi=3.14
# default value of radius is 1.
  def __init__(self,radius=1):
      self.radius=radius
      self.area=radius*radius*Circle.pi

  def circumference(self):
       self.area=self.radius*self.pi*2  
 
my_circle=Circle()
print my_circle.radius
print my_circle.circumference(2)
