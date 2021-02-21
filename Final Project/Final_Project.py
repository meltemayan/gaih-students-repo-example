class Recipe:
    def __init__(self,materials):
        self.matdict = 0
        self.materials = materials
        self.quantity = 0

    def PrintMaterials(self):
        print(self.materials)

    def Materials(self):
        print(self.matdict)

    def SetQuantity(self,quantity):
        self.quantity = quantity
        self.matdict = list(zip(self.materials,self.quantity))
    
    def Cook(self):
        print("Cooked")
    
    def Stir(self):
        print("Stirred")

    def Bake(self):
        print("Baked")

class Cake(Recipe):
    pass

class Omlette(Recipe):
    pass

class BakedVegetables(Recipe):
    pass

print("Cake")
cake = Cake(["egg","milk","sugar","butter","flour","vanilla","baking powder"])
cake.SetQuantity([3,1,1,1,1,1,1])
cake.Materials()
cake.Stir()
cake.Cook()

print("Omlette")
omlette = Omlette(["egg","olive oil","salt"])
omlette.SetQuantity([3,0.5,0.2])
omlette.Materials()
omlette.Stir()
omlette.Cook()

print("Baked Vegetables")
vegetables = BakedVegetables(["potato","carrot","broccoli","salt","olive oil"])
vegetables.SetQuantity([3,2,1,0.2,0.4])
vegetables.Materials()
vegetables.Bake()
