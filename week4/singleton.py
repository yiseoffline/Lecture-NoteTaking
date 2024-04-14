class Singleton(object):
    def __new__(cls):
        # hasattr() : 객체가 주어진 속성을 가지고 있는지 여부를 확인하는 함수 / 있으면 true, 없으면 false 반환
        if not hasattr(cls,'instance'):
            print('create')
            # 부모 클래스의 __new__ 메서드 호출해서 새 인스턴스 생성
            cls.instance = super(Singleton, cls).__new__(cls)
        else:
            print('recycle')
        return cls.instance # 인스턴스 반환

s1=Singleton() # Singleton 클래스의 인스턴스 생성
print(s1)

# Singleton 클래스의 인스턴스 생성 (이미 존재하는 인스턴스를 반환)
s2=Singleton()
print(s2) # s1을 하던 s2를 하던 똑같이 나오네

# 같은 인스턴스인지 확인
print(s1 is s2)