반복문 연습 3p 문자열로 코드 짜는 법! (사진 찍어놓음)
%d 에서는 %안에 못쓰니까 %%로 써준다! (\\ 처럼)

break는 반복문 for 또는 while을 빠져나가게 해준다!

(중요!) 홀짝 문제 시험에서 낼 때 홀수인지 짝수인지를 잘 따져주기!!

for문을 while문으로 바꿀 때
while에서 증가값은 마지막에!(어디다가 두는지가 큰 차이를 발생시킨다!)

break와 continue 차이 꼭 알아두기!!

잘 안되면 순서잘못됐는지 생각하기!
컴퓨터처럼 순서대로 생각해보자~ 그러다가 오류 발견할 때 있다!

<오늘의 코드>
"""while True :
    print("ㅋ", end = " ")"""

"""hap = 0
a, b = 0, 0

while True :
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
    b = int(input("더할 두 번째 수를 입력하세요 : "))
    hap = a + b
    print("%d + %d = %d" % (a, b, hap))"""

"""ch = ""
a, b = 0, 0 -> 여기에 변수들 써주는 건 그냥 참고한 책과 예시의 스타일이다.
                    파이썬에서는 이렇게 변수 선언을 꼭 안해주어도 괜찮다.

while True :
    a = int(input("계산할 첫 번째 수를 입력하세요 : "))
    b = int(input("계산할 두 번째 수를 입력하세요 : "))
    ch = input("계산할 연산자를 입력하세요 : ")

    if (ch == "+") :
        print("%d + %d = %d" %(a, b, a+b))
    elif (ch == "-") :
        print("%d - %d = %d" %(a, b, a-b))
    elif (ch == "%") :
        print("%d %% %d = %d" %(a, b, a%b))
    else :
        print("연산자를 잘못 입력했습니다.")"""

"""hap = 0
a, b = 0, 0

while True :
    a = int(input("더할 첫 번쨰 수를 입력하세요 : "))
    if a == 0 :
        break
    b = int(input("더할 두 번째 수를 입력하세요 : "))
    hap = a + b
    print("%d + %d = %d" %(a, b, hap))

print("0을 입력해 반복문을 탈출했습니다.")"""

"""hap = 0
i = 1
while i < 101 :
    hap += i
   
    if hap >= 1000 :
        break

    i = i +1

print("1~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d" %i)"""

"""hap, i = 0, 0

for i in range(1, 101) :
    if i % 3 == 0 :
        continue

    hap += i

print("1~100의 합계(3의 배수 제외) : %d" %hap)"""

"""while True :
    color = input("신호등 색상을 입력하시요: ")
    if color == "green" :
        break"""

"""
#반복문 연습 7p
hap = 0

while True :
    number = int(input("숫자를 입력하시오: "))
    hap += number
    con = input("계속?(y/n) :")
    if con == "Y" or con == "y" :
        continue
    else :
        break
print("합계는 : %d" %hap)"""
