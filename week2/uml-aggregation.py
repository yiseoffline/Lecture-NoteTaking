class Color:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

class Fruit:
    def __init__(self):
        self.color = Color()

class Basket:
    def __init__(self):
        self.fruits = []
        for i in range(10):
            self.fruits.append(Fruit())

# 실행 코드
basket = Basket()

# basket 객체의 과일 목록을 출력하여 확인
for idx, fruit in enumerate(basket.fruits):
    print(f"Fruit {idx+1}: (R: {fruit.color.r}, G: {fruit.color.g}, B: {fruit.color.b})")
