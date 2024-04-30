from abc import *

class Strategy1(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass

class Strategy2(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass

class Walk(Strategy1):
    def move(self):
        print("walk")

class Run(Strategy1):
    def move(self):
        print("run")

class Shoot(Strategy2):
    def attack(self):
        print("shoot")

class Launch(Strategy2):
    def attack(self):
        print("launch")

class Context:
    def __init__(self, move_strategy, attack_strategy):
        self.move_strategy = move_strategy()
        self.attack_strategy = attack_strategy()

    def move(self):
        self.move_strategy.move()

    def attack(self):
        self.attack_strategy.attack()

    def set_move_strategy(self, move_strategy):
        self.move_strategy = move_strategy()

    def set_attack_strategy(self, attack_strategy):
        self.attack_strategy = attack_strategy()

# Client
context = Context(Walk, Shoot)

# 초기 : 걷기 & 총 쏘기
context.move()
context.attack()

# 변경 : 뛰기 & 로켓 발사
context.set_move_strategy(Run)
context.set_attack_strategy(Launch)

# 변경된 것으로 수행
context.move()
context.attack()