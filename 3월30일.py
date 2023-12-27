12p 실습 2 다 연습하자!((내 견해)
4분~6분 다시 듣기 (조건문연습파트) (그냥 저런 것도 있구나~ 하면서 가볍게 봐두기!)

중첩 for 문
시계를 생각하자! (시 바늘이 한번 갈때 분 바늘이 한바퀴 도는 느낌)
19p 같은 특이한건 안낸다!
시험에 새로운 타입은 안 내는데, 기존에 우리가 배웠던 코드로
활용할 수 있는 내용을 가지고는 시험을 냄.

중간고사 공부? : 여태 까지 했던 내용과 문제 잘 풀 수 있으면 된다!

<While 문>

for가 잘 쓰여져 있으면, 그걸 while로 바꿀 수도 있다!

실습 6, 7 할 수 있어야함!

<오늘의 코드>

"""import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0 :
    print("앞면입니다.")
else :
    print("뒷면입니다.")
print("게임이 종료되었습니다.")"""

"""start = int(input("시작값을 입력하세요 : "))
end = int(input("끝값을 입력하세요 : "))
up = int(input("증가값을 입력하세요 : "))

hap = 0

for i in range(start, end, up) :
    hap = hap + i

print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" %(start, end, up, hap))"""


"""
#구구단!
for i in range(2,  10, 1) :
    for k in range(1, 10, 1) :
        print(i,"X",k ,"=", i*k)
    print()"""

"""
%구구단 가로방향
for i in range(1, 10) :
    for k in range(2, 10) :
        print("%d X %d = %2d" %(k, i, k*i), end = " ")
    print()"""
