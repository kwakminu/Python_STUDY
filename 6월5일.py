self 뜻 : 그 객체가 가진

15분 ~ 32분

인스턴스와 객체는 같은말.

<오늘의 코드>

"""class Car :
    color = ""
    speed = 0

    def __init__(self, value1, value2) :
        self.color = value1
        self.speed = value2
       

    def upSpeed(self, value) :
        self.speed += value

    def downSpeef(self, value) :
        self.speed -= value


myCar1 = Car("빨강", 30)
myCar2 = Car("파랑", 60)

print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar1.color,myCar1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar2.color,myCar2.speed))"""

"""class Car :
    color = ""
    speed = 0
    count = 0

    def __init__(self) :
        self.speed = 0
        Car.count += 1

myCar1, myCar2 = None, None

myCar1 = Car()
myCar1.speed = 30
print("자동차1의 현재 속도는 %dkm, 생산된 자동차는 총 %d대입니다." %(myCar1.speed,Car.count))

myCar2 = Car()
myCar2.speed = 60
print("자동차2의 현재 속도는 %dkm, 생산된 자동차는 총 %d대입니다." %(myCar2.speed,Car.count))"""
