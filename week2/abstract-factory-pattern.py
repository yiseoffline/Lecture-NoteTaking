# 버튼
class Button:
    def click(self):
        pass

class DarkButton(Button):
    def click(self):
        print("dark click")

class LightButton(Button):
    def click(self):
        print('light click')

# 스크롤
class Scroll:
    def scroll(self):
        pass

class DarkScroll(Scroll):
    def scroll(self):
        print("dark scroll")

class LightScroll(Scroll):
    def scroll(self):
        print('light scroll')

# 체크박스
class CheckBox:
    def check(self):
        pass

class DarkCheckBox(CheckBox):
    def check(self):
        print('dark checkbox')

class LightCheckBox(CheckBox):
    def check(self):
        print("light checkbox")


# 제품 생성
class UIFactory:
    def getButton(self):
        pass

    def getCheck(self):
        pass

    def getScroll(self):
        pass

# 다크 모드
class DarkFactory(UIFactory):
    def getButton(self):
        return DarkButton()

    def getCheck(self):
        return DarkCheckBox()

    def getScroll(self):
        return DarkScroll()

# 라이트 모드
class LightFactory(UIFactory):
    def getButton(self):
        return LightButton()

    def getCheck(self):
        return LightCheckBox()

    def getScroll(self):
        return LightScroll()
    

df = DarkFactory()
bt = df.getButton()
ck = df.getCheck()
sc = df.getScroll()

bt.click()
ck.check()
sc.scroll()