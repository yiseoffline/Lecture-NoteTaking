class Pizza: 
    # Product 클래스
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.bacon = False

    def pizza_state(self):
        print("size: {}, cheese: {}, pepperoni: {}, bacon: {}".format(self.size, self.cheese, self.pepperoni, self.bacon))

class PizzaBuilder: # Builder 인터페이스
    def set_size(self, size):
        pass
    def add_cheese (self) :
        pass
    def add_pepperoni (self):
        pass
    def add_bacon(self):
        pass
    def build (self):
        pass

class MargheritaBuilder(PizzaBuilder):  # ConcreteBuilder
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        # 마르게리타에는 페퍼로니가 들어가지 않으므로 pass
        pass

    def add_bacon(self):
        # 마르게리타에는 베이컨이 들어가지 않으므로 pass
        pass

    def build(self):
        return self.pizza

class MeatLoversBuilder(PizzaBuilder):
    # ConcreteBuilder
    def __init__(self):
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

    def build(self):
        return self.pizza

class PizzaDirector:  # Director 클래스
    def __init__(self, builder):
        self._builder = builder
    
    def construct(self, size="Medium"):
        self._builder.set_size(size)
        self._builder.add_cheese()
        self._builder.add_pepperoni()
        self._builder.add_bacon()
        return self._builder.build()

# 마르게리타 피자 생성
margherita_builder = MargheritaBuilder()
director = PizzaDirector(margherita_builder)
margherita_pizza = director.construct(size="Large")
print("Margherita Pizza:", margherita_pizza)

# Meat Lovers 피자 생성
meat_lovers_builder = MeatLoversBuilder()
director = PizzaDirector(meat_lovers_builder)
meat_lovers_pizza = director.construct(size="Large")
print("Meat Lovers Pizza:", meat_lovers_pizza)

'''
출력 : 
Margherita Pizza: <user_code.Pizza object at 0x7f7e87c2f5d0>
Meat Lovers Pizza: <user_code.Pizza object at 0x7f7e87c2e590>
'''