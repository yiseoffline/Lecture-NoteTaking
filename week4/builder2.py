class Pizza:
    def __init__(self):
        self.size = "Medium"
        self.cheese = False
        self.pepperoni = False
        self.bacon = False
        self.vegetables = []

    def pizza_state(self):
        print("size: {}, cheese: {}, pepperoni: {}, bacon: {}, vegetables: {}".format(
            self.size, self.cheese, self.pepperoni, self.bacon, self.vegetables))
        
class PizzaBuilder:
    def __init__(self):
        self.reset()

    # 이전에 설정된 피자의 상태를 지우고 새로운 피자를 생성
    def reset(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def add_vegetables(self, vegetables):
        self.pizza.vegetables.extend(vegetables)
        return self

    def build(self):
        finished_pizza = self.pizza
        self.reset()  # 준비된 피자를 반환한 후, 빌더를 리셋하여 다음 피자 준비
        return finished_pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def prepare_margherita(self):
        self.builder.reset()
        return self.builder.set_size("Large").add_cheese().build()
    
    def prepare_meat_lovers(self):
        self.builder.reset()
        return self.builder.set_size("Large").add_cheese().add_pepperoni().add_bacon().build()
    
    def prepare_vegetarian(self):
        self.builder.reset()
        return self.builder.set_size("Large").add_cheese().add_vegetables(["Bell peppers", "Olives", "Onions"]).build()

# 사용 예시
builder = PizzaBuilder()
director = PizzaDirector(builder)

margherita = director.prepare_margherita()
margherita.pizza_state()

meat_lovers = director.prepare_meat_lovers()
meat_lovers.pizza_state()

vegetarian = director.prepare_vegetarian()
vegetarian.pizza_state()

'''
출력
size: Large, cheese: True, pepperoni: False, bacon: False, vegetables: []
size: Large, cheese: True, pepperoni: True, bacon: True, vegetables: []
size: Large, cheese: True, pepperoni: False, bacon: False, vegetables: ['Bell peppers', 'Olives', 'Onions']
'''