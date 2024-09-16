class circle:
   def __init__(self,radius,area):
    self.radius=radius
    self.area=area

   def area_c(self):
    area = 3.14 * self.radius ** 2
    return area
  
   

   def circumference_c(self):
     circumference=2*3.14**self.radius
     return circumference
   
   def greater_c(self):
      if (self.area>20):
        print("area is greater")
      else:
       print("ci cumference is greater")



c1=circle(4,56)
print(c1.area_c())
print(c1.circumference_c())
print(c1.greater_c())
