import sqlite3

class MetaSingleton(type):
    _instances = {}  # 클래스 당 인스턴스를 저장하기 위한 사전

    def __call__(cls, *args, **kwds):
        # 클래스의 인스턴스가 아직 생성되지 않은 경우에만 실행
        if cls not in cls._instances:
            # 새 인스턴스를 생성하고 사전에 저장
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwds)
        # 이미 존재하는 경우에는 기존 인스턴스를 반환
        return cls._instances[cls]

# 메타클래스 MetaSingleton을 사용하여 Database 클래스를 정의
class Database(metaclass=MetaSingleton):
    connection = None
    
    def connect(self):
        # 이미 연결이 되어있지 않은 경우에만 연결
        if self.connection is None:
            # SQLite 데이터베이스에 연결하고 커서 객체 생성
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursorobj = self.connection.cursor()
        # 커서 객체 반환
        return self.cursorobj

# Database 클래스의 connect 메서드를 호출하여 커서 객체를 얻음
db1 = Database().connect()  # Database 클래스의 인스턴스를 생성하고 connect 메서드 호출
db2 = Database().connect()  # Database 클래스의 인스턴스를 생성하고 connect 메서드 호출

# db1과 db2가 같은지 비교하여 True 또는 False 출력
print(db1)
print(db2)
print(db1 is db2)