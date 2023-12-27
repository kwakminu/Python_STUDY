10장 함수
프로그래밍에서의 함수 : 인수가 있을 수도 있고 없을 수도 있음. 반환값이 있을 수도 있고 없을 수도 있음.
def -> 함수를 선언할게!
def 함수의이름(인수 <- 있을 수도 있고 없을 수도 있음) :
16p 변수명은 꼭 똑같을 필요 없다. 주는 걸 받는 것이라고 생각!
지금은 어떻게 만들어지는지만 알면된다. 언제 만

def 함수의이름(괄호안에 있는 스타일로 짜면 호출할 때도 있어야 하고, 없는 스타일로 짜면 호출할 때도 없어야 함. )
18p. return이 있는지 없는지에 따라 달라짐. return이 없으면 11줄에서 빈손으로 와서 오류가 난다. 빈손으로 갔는데, 그걸 hap에다 넣을 수 없으니까!

함수는 호출하는 애, 정의하는 애가 짝이 딱딱 맞아야한다!!!

<오늘의 코드>

"""def plus(v1, v2) :
    result = 0
    result = v1 + v2
    return result

hap = 0

hap = plus(100, 200)
print("100과 200의 plus() 함수 결과는 %d" %hap)"""

"""
def happyBirthday(name) :
    print("생일을 축하합니다!")
    print("%s 님의 생일을 축하합니다!" %name)

def f(x) :
    for i in range(1,10) :
        print("%d * %d = %d" %(x, i, x*i))

x = int(input("정수를 입력하세요 : "))
f(x)"""

"""
def calc(v1, op, v2) :
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    elif op == '**' :
        result = v1 ** v2
   

    return result

res = 0
var1 , var2, oper = 0, 0, ""

var1 = int(input("첫 번째 수를 입력하세요 : "))
oper = input("계산을 입력하세요(+, -, *, /, **) : ")
var2 = int(input("두 번째 수를 입력하세요 : "))

if oper == "/" and  var2 == 0 : :
    print("0으로는 나누면 안됩니다.ㅠㅠ")
else :
    res = calc(var1, oper, var2)
    print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res) )"""
