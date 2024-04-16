class System:
    def __init__(self):
        pass
    
    def start_test(self):
        pass

class Android(System):
    def __init__(self, test_unit):
        self.test_unit = test_unit
    
    def start_test(self):
        result = self.test_unit.run()
        print(f"Android에서 {result}")

class IOS(System):
    def __init__(self, test_unit):
        self.test_unit = test_unit
    
    def start_test(self):
        result = self.test_unit.run()
        print(f"iOS에서 {result}")

class TestUnit:
    def run(self):
        pass

class Dijkstra(TestUnit):
    def run(self):
        return "Dijkstra 실행"

class MinimumSpanningTree(TestUnit):
    def run(self):
        return "Minimum Spanning Tree 실행"

class AStar(TestUnit):
    def run(self):
        return "A_star 실행"
    
android_dijkstra = Android(Dijkstra())
android_dijkstra.start_test()

ios_mst = IOS(MinimumSpanningTree())
ios_mst.start_test()
