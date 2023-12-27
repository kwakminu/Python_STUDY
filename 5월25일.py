<오늘 부분 시험문제 많이 낸다는 소문이>
35p. (중요) 정의하는 데와 호출하는 데의 파라미터가 딱딱 맞아야지 오류가 안난다!
39p. country = 로 콕 찝어서 지정했기 때문에 국적에 들어감!
40p. 몇개를 주든 하나의 튜플로 취급해서 받는다!
42p. 묶어서 줄 때와 안묶어서 주는 게 차이가 있다!

43p. 이 페이지는 시험에 안나온다. cf)일반적으로.. 이 부분만 봐도 된다!

44p. (중요!! 외우기!)
       규칙 1. 매개변수로 넘겨줄 때는 : 대신 = 을 쓴다!
       규칙 2. 키에는 문자열이 들어가도 따옴표를 쓰지 않는다!
       cf. 키에서는 따옴표 안써도 값은 문자열 따옴표 써야함!

46p. 함수의 구조 잘 이해하기! 정의부가 있고 호출부가 있는데, 호출부를 부르면 동작을 해~
      정의부는 조금 이따가 부를 테니까 넘어가야지~ 이런 느낌
      어디로 가는 지만 잘 찾으면 된다!
      아랫부분 설명 : infunc는 outfunc안에 들어가야지만 있는 함수이기 때문에 오류가 남!
4. 함수의 응용 파트는 어렵게 꼬아내지 않고, PPT에 있는 것들 그대로 내거나 안내거나 하기 때문에, 이거 이상을 해야지 라고 생각하지 않아도 된다!

<오늘의 코드>
"""def para_func(v1,v2,v3=0) :
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" %hap)
hap = para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" %hap)"""

"""def fo(name, birth, major = 'cs', country = 'KOR') :
    print("이름 :", name, ", 생년월일 :", birth, ', 전공 :', major, ',국적 :', country)

fo('곽민우', '20020808')
fo('곽민우', '20020808', 'Software')
fo('곽민우', '20020808', 'Software', 'Korea')
fo('곽민우', '20020808', country = 'KOREA')"""

def para_func(*para) :
    result = 0
    for num in para :
        result = result + num

    return result

"""hap = 0

hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" %hap)
hap = para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" %hap)

hap = para_func(10,20,30,40,50,60,70,80,90,100)
print(hap)"""

"""
def print_language(*languages) :
    for lang in languages :
        print(lang)

print_language("Python", "Java", "Ruby")

def print_language_tuple(languages_tuple) :
    for lang in languages_tuple :
        print(lang)

print_language_tuple(('Python', 'Java', 'Ruby'))"""

"""
def concat(sep, *args) :
    return sep.join(args)

print(concat("/", "a", "b", "c"))
print(concat("/", "a", "b", "c", "d"))"""

"""def dic_func(**para) :
    for k in para.keys() :
        print("%s --> %d명입니다." %(k,para[k]))"""

def outFunc(v1,v2) :
    def inFunc(num1, num2) :
        return num1 + num2
    return inFunc(v1, v2)
print(outFunc(10, 20))

def hap(num1, num2) :
    res = num1 + num2
    return res
print(hap(10,20))

hap2 = lambda num1, num2 : num1+num2
print(hap2(10,20))

hap3 = lambda num1 = 10, num2 = 20 : num1 + num2
print(hap3())
print(hap3(100, 200))
