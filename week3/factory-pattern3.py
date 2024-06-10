# Abstract Class
class Product:
    def use(self):
        pass

class Factory:
    def create(self, owner) -> Product:
        p = self.createProduct(owner)
        self.registerProduct(p)
        return p

    # 하위에서 구현됨
    def createProduct(self, owner) -> Product:
        pass

    # 하위에서 구현됨
    def registerProduct(self, product):
        pass

# Concrete Class
class IDCard(Product):
    def __init__(self, owner):
        print("owner", "의 카드를 만듭니다.")
        self.owner = owner

    def use(self):  # abstract method
        print(self.owner, "의 카드를 사용합니다.")

    def getOwner(self):
        return self.owner

class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []  # 카드 발급자 리스트

    def createProduct(self, owner) -> Product:  # abstract method
        return IDCard(owner)

    def registerProduct(self, product):  # abstract method
        self.owners.append(product.getOwner())

    def getOwners(self):
        return self.owners

# 코드 실행 부분
factory = IDCardFactory()
card1 = factory.create("홍길동")
card2 = factory.create("이순신")
card3 = factory.create('강감찬')

card1.use()
card2.use()
card3.use()