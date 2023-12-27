시험공부할 때 리스트먼저 거꾸로 하는게 좋다.
시험 문제를 뒤쪽에 더 많이 낸다! (비중을 더 크게 낸다)
리스트가 제일 시험문제 낼 게 많다!

46p 데이터 내용만 넘어가는 게 아니라 데이터 주소값을 넘겨줌!
한쪽에서 변경해준 게 다른 쪽에서도 영향을 준다.;

47p. 따로 하고 싶으면 이렇게 하기! (기억!) or copy해도된다!

48p. 인덱스는 0부터 시작된다는 거 항상 유념하기!

51p. 2차원리스트 풀 때 메트릭스 그려서 해도 된다!

52p같은 어려운 문제는 안낸다! (할수있으면 하고 못하면 재껴도 된다!)
but 리스트 연습 코드에 있는 "좋아하는 색 리스트" 정도는 할 수 있어야함!

오늘의 코드

"""list1= []
list2 = []
value = 0
for i in range (0, 4) :
    for k in range (0,5) :
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []

for i in range(0,4) :
    for k in range (0,5) :
        print("%3d" %list2[i][k], end = " ")
    print(" ")"""

"""c = []

for k in range (0,3) :
    put = input("좋아하는 색을 입력하세요: ")
    c.append(put)
check = 0

while check != "0" :
    check = input("색을 하나 입력하세요(0을 입력하면 종료합니다): ")
    if check in c :
        print("%s은(는) 당신이 좋아하는 색입니다." %check)
    else :
        print("%s은(는) 당신이 좋아하는 색이 아닙니다." %check)"""
