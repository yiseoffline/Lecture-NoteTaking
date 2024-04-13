from abc import *
from copy import deepcopy

class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def clone(self):
        pass


class UnderlinePen(Product):
    def use(self, s: str):
        n = len(s)
        print(s)
        for i in range(n):
            print("~", end="")
        print()

    def clone(self):
        return deepcopy(self)

class MessageBox(Product):
    def __init__(self, deco: str):
        self.deco = deco

    def use(self, s: str):
        n = len(s) + 4
        for i in range(n):
            print(self.deco, end="")
        print()
        print(self.deco, s, self.deco)
        for i in range(n):
            print(self.deco, end="")
        print()

    def clone(self):
        return deepcopy(self)

class Manager:
    def __init__(self):
        self.showcase = {}

    def register(self, name: str, proto: Product):
        self.showcase[name] = proto

    def create(self, protoName):
        p = self.showcase.get(protoName)
        return p.clone()
    
# Manager 객체 생성
manager = Manager()

# MessageBox 및 UnderlinePen 객체 생성
m1 = MessageBox("**")
m2 = MessageBox("##")
p1 = UnderlinePen()

# 프로토타입 객체 등록
manager.register("msg*", m1)
manager.register("msg#", m2)
manager.register("pen", p1)

# 프로토타입을 이용하여 객체 생성
msg1 = manager.create("msg*")
msg2 = manager.create("msg#")
pen = manager.create("pen")

# 단어 설정
word = "hello"
msg1.use(word)
word = "world"
msg2.use(word)
pen.use(word)

'''
출력

******************
** hello **
******************
##################
## world ##
##################
world
~~~~~
'''