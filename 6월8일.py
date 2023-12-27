38p. 변수 선언 부분 없어도 되는데, 이 책은 선언하는 책이다~

class 서클, 반지름이라는 필드

시험을 실습 3처럼 복잡하게 내진 않는다! 풀수있으면 좋지만 못풀어도 이렇게까지는 안내니까
부담 안가져도 된다!

대신 복습으로 주는 자료들은 다 할 수 있어야함!

<오늘의 코드>

"""class Car :
    speed = 0
    def upSpeed(self, value) :
        self.speed += value

        print("현재 속도(슈퍼 클래스) : %d" %self.speed)

class Sedan(Car) :
    def upSpeed(self, value) :
        self.speed += value

        if self.speed > 150 :
            self.speed =150

        print("현재 속도(서브 클래스) : %d" %self.speed)

class Truck(Car) :
    pass

class Sonata(Sedan) :
    pass

s1, t1 = None, None

t1 = Truck()
s1 = Sedan()
so1 = Sonata()

print("트럭 --> ", end = "")
t1.upSpeed(200)

print("승용차 --> ", end = "")
s1.upSpeed(200)

print("소나타 --> ", end = "")
so1.upSpeed(200)"""

"""
class Circle :
    반지름 =0
    넓이=0
    둘레=0
   
    def __init__(self, 반지름) :
        self.반지름 = 반지름

    def 넓이(self) :
        self.넓이 = (3.14)*(self.반지름)**2
        print("원의 넓이는 %.1f" %self.넓이)

    def 둘레(self) :
        self.둘레 = 2*(3.14)*(self.반지름)
        print("원의 둘레는 %.1f" %self.둘레)

print("원의 넓이와 둘레를 알려드립니다.")
반지름 = int(input("반지름을 입력하세요: "))
원 = Circle(반지름)
원.넓이()
원.둘레()"""
