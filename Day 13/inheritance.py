class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows!")


class Cougor(Cat):
    def pour(self):
        print(f"{self.name} Purrs!")


class Lion(Cougor):
    def roar(self):
        print(f"{self.name} roars!")


myLion = Lion('tiddo')
myLion.roar()
