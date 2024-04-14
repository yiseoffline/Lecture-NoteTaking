class MetaSingleton(type):
    _instances = {}  # 클래스 당 인스턴스를 저장하기 위한 사전

    def __call__(cls, *args, **kwds):
        # 클래스의 인스턴스가 아직 생성되지 않은 경우에만 실행
        if cls not in cls._instances:
            # 새 인스턴스를 생성하고 사전에 저장
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwds)
        # 이미 존재하는 경우에는 기존 인스턴스를 반환
        return cls._instances[cls]

# 메타클래스 MetaSingleton을 사용하여 Box 클래스를 정의
class Box(metaclass=MetaSingleton):
    pass

# Box 클래스의 인스턴스 생성
b1 = Box()
b2 = Box()

# 두 인스턴스가 같은지 비교하여 True 또는 False 출력
print(b1 == b2) # True
