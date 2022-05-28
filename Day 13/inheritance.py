class Cat:
    def __init__(self, name):
        print('inside Cat init')
        self.name = name

    def meow(self):
        print(f"{self.name} meows!")


class Cougor(Cat):
    def pour(self):
        print(f"{self.name} Purrs!")


class Lion(Cat):
    def __init__(self, name):
        print("inside Lion init")
        super().__init__(name)

    def roar(self):
        print(f"{self.name} roars!")


myLion = Lion('tiddo')
myLion.roar()
