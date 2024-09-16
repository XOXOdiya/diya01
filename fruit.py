class fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color
 
    def fruitname(self):
        return'{} {}'.format(fruit1,fruit2)
    
fruit1=("mango","yellow")
fruit2=("apple","red")

print(fruit.fruitname(fruit1))
#print(fruit.fruitname(fruit2))