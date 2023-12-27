리스트 조작 함수 부분을 외워서 시험 내지는 않는다!
리스트 함수를 여러개 적용하고 어떻게 결과가 바뀌었는지를 문제로 낸다.
함수 이름 (append, pop..)을 외우는 게 아니다. 그걸 내지 않고 어떻게 동작하나?만 알 수 있으면된다.
pop만 쓰면 뒤에 있는 게 사라짐
sort는 내용 자체를 바꾸는 것. sorted 얘는 내용을 보여주기만 하는 것.
sorted된 내용을 다시 쓰고 싶으면 새로운 리스트를 대입하기!

37p for 변수 in range 쓸 때 변수 명 맞추는 거 중요하다!

---

38p 실습 6 여기에는 안써있지만 코드 짤 때는 문자열로 짜야한다!

(기억!) 38p. for 변수 in 리스트를 쓸 수도 있지!
리스트에서 왼쪽에서 하나씩 뽑아오는거야~

40p에서 for i in range(0,100) :
      bb.append(aa[99-i]
를 더 간단히 바꾸는 방법 있다! (사진찍어놓음)

멤버연산자 : 그안에 있니?
10 in a_list : a_list 리스트 안에 10 있니?
50 not in a_list : a_list 리스트 안에 50 없니?

43p 55가 없어도 에러 안나고 쓸 수 있다!

45p 다음 시간에 실습 8 답 보기!

문제 풀 때 조건 맞게만 하면 된다!

<오늘의 코드>

"""klist = []
for i in range (0, 3) :
    klist.append(0)
hap = 0

for i in range (0,3) :
    klist[i] = int(input(str(i+1)+"번째 숫자 :"))

for p in range (0,3) :
    hap = hap + klist[p]

print("합계 ==> %d" %hap)"""

빵 = ["플랫","위트","허니오트","화이트"]
고기 = ["미트볼","소시지","닭가슴살"]
야채 = ["양상추","토마토","오이"]
소스=["마요네즈","케찹","칠리"]
"""
for i in range (0,4) :
    for k in range (0,3) :
        for o in range (0,3) :
            for p in range (0,3) :
                print("%s+%s+%s+%s" %(빵[i],고기[k],야채[o],소스[p]))
#이건 혼자 그냥 해본 거! 신경쓰지 말자 """

"""
aa = []
bb = []
value = 0

for i in range (0, 100) :
    aa.append(value)
    value += 2

bb = aa.copy()
bb.reverse()

print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." %(bb[0], bb[99]))
"""

nations = ["K", "C", "R", "M"]
nations.append("N")

print(nations)

if "J" in nations :
    print("Japan 는(은) 국가목록에 있습니다.")
else :
    print("Japan 는(은) 국가목록에 없습니다.")

if "R" in nations :
    print("Russia 는(은) 국가목록에 있습니다.")
else :
    print("Russia 는(은) 국가목록에 없습니다.")
