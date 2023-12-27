함수 내부에 선언된 변수는 함수 안에서만 생존할 수 있는 변수

<오늘의 코드>

"""def func1() :
    global a
    a = 10
    print("func1()에서 a값 %d" %a)
   
def func2() :
    print("func2()에서 a값 %d" %a)

a = 20
print(a)

func1()
func2()
print(a)"""

""""
def func(a) :
    hap = 0
    for k in a :
        hap = hap + int(k)
    print(hap)

a = input("정수를 입력하세요")
func(a)"""

"""
def func1() :
    result = 100
    return result

def func2() :
    print("반환값이 없는 함수 실행")

hap = 0

hap = func1()
print("func1()에서 돌려준 값 ==> %d" %hap)
func2()"""

"""
def multi(v1, v2) :
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

myList = []
hap , sub = 0, 0

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
print("multi()에서 돌려준 값 ==> %d, %d" %(hap, sub))"""
