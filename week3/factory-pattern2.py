# Robot interface
class Robot:
    def speak(self):
        pass

class Cat(Robot):
    def speak(self):
        print("meow")

class Dog(Robot):
    def speak(self):
        print("bark")

# Factory interface
class Factory:
    def createRobot(self):
        pass

class CatFactory(Factory):
    def __init__(self):
        self.cat_count = 0

    def createRobot(self):
        self.cat_count += 1
        return Cat()

    def catCount(self):
        return self.cat_count

class DogFactory(Factory):
    def haveDog(self):
        self.dog = self.createRobot()

    def createRobot(self):
        return Dog()

    def addWing(self, dog: Dog):
        print("dog wings added")
        return dog

cat_factory = CatFactory()
cat1 = cat_factory.createRobot()
cat2 = cat_factory.createRobot()
print(cat_factory.catCount())

dog_factory = DogFactory()
dog1 = dog_factory.createRobot()
dog_factory.addWing(dog1)
