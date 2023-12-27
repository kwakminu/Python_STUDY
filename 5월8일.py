9p,10p 꼭 실습해보기!

12p. 중괄호고 : 이보이지 않아? ->세트

16p. 인덱스와 값을 동시에 보여주는 함수

20p. 문자열도 인덱스, 슬라이싱 이용해서 뽑아올 수 있음

오늘의 코드

"""sd = {x: x**2 for x in (2,4,6)}
print(sd)"""

"""korean_foods = ['김치', '비빔밥', '떡볶이']
korean_foods_enum = enumerate(korean_foods)
print(type(korean_foods_enum))
print(korean_foods_enum)

for index, food in korean_foods_enum :
    print(index, food)

for index, food in enumerate(korean_foods) :
    print(index, food)"""

"""evens = [x*2 for x in range(10)]
print(evens)

A = [1,2,3]
B = [2,3,4]
pairs = [(a,b) for a in A for b in B if a!=b]
print(pairs)

triple_dic = {x : x**3 for x in (2,3,4)}
print(triple_dic)

triple_dic = {}
for x in (2,3,4) :
    triple_dic[x] = x**3
print(triple_dic)"""

"""
s = []
print("지금부터 달리기 시합을 시작하겠습니다.")
print()
n = int(input("달리기 선수가 몇 명인가요? "))
print()
for k in range (n) :
    s.append(input("지금 들어온 선수 이름을 입력하세요 : "))
    print()
print("달리기 시합 결과!!")
print()
for index, name in enumerate(s) :
    print("%d 등 %s" %(index+1, name))
print()
print("수고 많았습니다, 여러분!!")"""

"""a_list = [44, 66, 34, 24, 144, 98, 568, 234, 345]
A_list = [x for x in a_list if x%12==0]
print(A_list)"""

"""b_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
B_list = [int(x) for x in b_list if x>0]
print(B_list)"""

"""ss = "파이썬짱!"

sslen = len(ss)
for i in range(0, sslen) :
    print(ss[i]+'$', end = '')"""

"""ss = '파이썬은완전재미있어요'

sslen = len(ss)
for i in range(0, sslen) :
    if i%2 == 0 :
        print(ss[i], end='')
    else :
        print('#',end='')"""

outStr = ""
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for i in range(0, count) :
    outStr += inStr[count - (i +1) ]

print("내용을 거꾸로 출력 --> %s" %outStr)
#그냥 인덱스로 심플하게 할 수도 있다~ (::-1)
