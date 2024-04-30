class CarColor:
    def __init__(self, color_name, rgb_value):
        self.color_name = color_name
        self.rgb = rgb_value
    
    def __str__(self):
        return f"{self.color_name} ({self.rgb})"

class ColorFactory:
    _color_cache = {}

    @classmethod
    def get_car_color(cls, color_name, rgb_value):
        if color_name not in cls._color_cache:
            cls._color_cache[color_name] = CarColor(color_name, rgb_value)
        return cls._color_cache[color_name]

    @classmethod
    def total_colors_created(cls):
        return len(cls._color_cache)

class Car:
    def __init__(self, year, brand, model, fuel, car_color):
        self.year = year
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.car_color = car_color

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.fuel}, 색상: {self.car_color}"

# 색상 객체 생성
red = ColorFactory.get_car_color("red", (255, 0, 0))
blue = ColorFactory.get_car_color("blue", (0, 0, 255))

# 자동차 객체 생성 및 색상 공유
car1 = Car(2020, "현대", "그랜저", "가솔린", red)
car2 = Car(2021, "기아", "K5", "가솔린", blue)

# 자동차 정보 출력
print(car1)
print(car2)

# 생성된 고유 색상 수 출력
print(f"총 생성된 고유 색상 수: {ColorFactory.total_colors_created()}")
