19p color의 length를 구하는 건지 colors의 length를 구하는 건지 잘
확인하기!

20p ( i+1)+"번쨰 숫자 :"는 숫자 + 문자이기 때문에 할 수 없음
그래서 str을 붙였다!

19, 20p 복습하기!

(sum() ->리스트에 있는 거 다 합하기
min() ->리스트에 있는 최솟값
max() -> 리스트에 있는 최댓값
-> 시험범위는 아니지만 실제 적용할 때 많이 쓴다!)

while 들어가기 전에 꼭 초기값주기!
그리고 끝값 +1 쓰거나 작거나 같을때로 쓰기!
while 나오기 직전에 증감값!

for문이 익숙하면 for문으로 우선 짜고, 그걸 바탕으로 while로 바꾸자!
그게 더 편할 수 있다.

리스트의 값 변경? -> 변수 값 바꾸는 거랑 똑같다!

24p 데이터 하나 자리에 두개 넣으려면 슬라이싱으로 넣어줘야한다!

(중요!) append는 뒤에 들어가! (들어갈 때 뒤로 들어간다!)

cards.insert(1, 9) : 1번째 인덱스에 9라는 값을 삽입해줘~ -> 9가 첫번째 인덱스가 됨!
cards.remove(5) 5라는 값을 지워줘~
cards.pop(3) 3번째 인덱스에 있는 값을 지워줘~

<오늘의 코드>
"""colors = ['black', 'blue', 'yellow', 'red']

for i in colors :
    print(i, len(i))"""

"""aa = []
for i in range(0,10) :
    aa.append(0)
hap = 0

i = 0
while i < 10 :
    aa[i] = int(input(str(i+1)+"번째 숫자 : "))
    i = i + 1

hap = sum(aa)

print("합계 ==> %d" %hap)"""

"""list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for i in list1 :
    for k in list2 :
        print("%d * %d= %d" %(i, k, i*k))"""

"""list1 = list(range(2,10))
list2 = list(range(1,10))

for i in list1 :
    for k in list2 :
        print("%d * %d= %d" %(i, k, i*k))"""

a=[]
print("한번에 하나씩 총 3개 좋아하는 과일을 입력하세요.\n")

for i in range (1, 4) :
    a.append(input("%d: 좋아하는 과일을 입력하세요: " %i))

print("\n당신이 좋아하는 과일은",a,"입니다")
