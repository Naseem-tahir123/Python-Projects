class Laptop:
    def __init__(self,Brand,Model, Generation):
        print("hello constructor")
        self.Laptop_brand = Brand
        self.Laptop_Model = Model
        self.Laptop_Generation = Generation

Laptop1 = Laptop("Hp","Model: 7604","6th Generation")
Laptop2 = Laptop("Dell","Model: 7240","7th Generation")
print(Laptop1.Laptop_brand,Laptop1.Laptop_Generation)
print(Laptop2.Laptop_brand,Laptop2.Laptop_Generation)