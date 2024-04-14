class MyInt(type): # 메타클래스
    def __call__(cls, *args, **kwds): # 인스턴스 생성할 때 호출
        print('my int',args)
        print('now do whatever you want with these objects ...')
        # 기존의 타입 클래스의 __call__ 메서드를 호출하여 인스턴스 생성
        return type.__call__(cls,*args,**kwds)
    
# 메타클래스 MyInt 사용해서 int 클래스 정의
class int(metaclass=MyInt):
    def __init__(self,x,y):
        self.x=x
        self.y=y

# int 클래스의 인스턴스 생성
i=int(4,5)

'''
출력
my int (4, 5)
now do whatever you want with these objects ...
'''