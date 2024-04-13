# 3주차 Factory Pattern

# 기능이 추가될 때마다 수정이 필요한 코드
class Animal:
    def __init__(self,a_type):
        self.a_type=a_type
    def hey(animal:Animal):
        if animal.a_type == 'Cat':
            print('meow')
        elif animal.a_type == 'Dog':
            print('bark')
        else:
            raiseError('wrong a_type')

kitty = Animal('Cat')
bingo = Animal('Dog')
cow = Animal('Cow')
sheep = Animal('Sheep')

hey(kitty)
hey(bingo)
hey(cow)
hey(sheep)

# 기능이 추가 되어도 수정이 안 필요한 코드임

class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print('meow')

class Dog(Animal):
    def speak(self):
        print('bark')

class Sheep(Animal):
    def speak(self):
        print('meh')

class Cow(Animal):
    def speak(self):
        print('moo')

def hey(animal:Animal):
    animal.speak()

cow = Cow()
sheep = Sheep()

hey(cow)
hey(sheep)
