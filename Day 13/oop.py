class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    def bark(self):
        print(f"{self.name} says WOOF!")

    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} does not know {trick}")


myDog = Dog("Fido", "Mixed", "Indon")
myDog.bark()
myDog.learn_trick("roll over")
myDog.perform_trick("roll over")
myDog.perform_trick("sit")
