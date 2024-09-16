class cars:
    def __init__(self,name,speed,millage):
        self.name=name
        self.speed=speed
        self.millage=millage

    def car(self):
       return'{} {} {}'.format(self.name,self.speed,self.millage*10)

car1= cars(name="mercedes",speed=250,millage=23)
print(car1.car())