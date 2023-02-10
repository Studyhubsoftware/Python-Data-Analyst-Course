class Dog:
    def __init__(self,breed, age,color):
        self.breed = breed
        self.age = age
        self.color = color

class cat:
     def __init__(self, name, gender, is_wild):
        self. name = name
        self.gender = gender
        self.is_wild = is_wild


class Burger:
    def __init__(self, bread, topping, filling, is_veg, price):
        self. bread = bread
        self.topping = topping
        self.filling = filling
        self. is_veg = is_veg
        self.price = price
 
  # use the classes to create object
tiger = Dog('German Shepherd', 2, 'golden') 
sheru = Dog ('Pug', 3, 'black') 
tommy = Dog('Labrador', 1, 'white') 

mau = cat('mau', 'M', False) 
mini = cat('mini', 'F', False)  
max = cat('max', 'M', True)
orea = cat('orea', 'F', False)

Burger1= Burger('brown', 'lettuce', 'veg', True, 50)
Burger2= Burger('brown', 'cheese', 'chicken', False, 100)

print("tiger is a", tiger.breed, "dog")