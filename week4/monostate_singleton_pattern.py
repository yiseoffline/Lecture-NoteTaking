class MonoState:
    __shared_state = {}
    def __init__(self): 
        self.__dict__ = self.__shared_state

        self.x = 1
        self.y = 2
        self.z = 3
        pass

ms1=MonoState()
ms2=MonoState()

print (ms1)
print (ms2)

ms2.x = 20
ms1. y = 20
ms2.z = 30

print(ms1.x, ms1.y, ms1.z)
print(ms2.x, ms2.y, ms2.z)
print(ms1.__dict__)
print(ms2.__dict__)