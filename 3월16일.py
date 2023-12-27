"""first = int(input("첫번째 정수를 입력하세요 :"))
second = int(input("두번째 정수를 입력하세요 :"))
print(first,"+",second,"=",first+second)
print(first,"-",second,"=",first-second)
print(first,"*",second,"=",first*second)
print(first,"/",second,"=",first+second)"""

"""americano = 2000
cafelatte = 3000
kapuchino = 3500
amrsell = int(input("아메리카노 판매 개수 :"))
cafsell = int(input("카페라떼 판매 개수 :"))
kapsell = int(input("카푸치노 판매 개수 :"))
print("총 매출은",americano*amrsell+cafelatte*cafsell+kapuchino*kapsell,"입니다.")"""

#%표시할 때 문자열 오류 나는 거 질문 : 쉼표
#>=와 =>가 차이가 있나? :문법적오류
#;가 무슨 의미였지? : 여러 문장 한 라인으로 쓸떄 쓰는 기호

"""a = 10
a+=5;print(a)"""

"""a,b=100,200
print(a==b,a!=b,a>b,a<b,a>=b,a<=b)"""

"""a=99
print((a>100)and(a<200))
print((a>100)or(a<200))
print(not(a==100))"""
#print 써 주어야 작동하는 거겠지?

exmoney = int(input("교환할 금액을 입력하세요 : "))
print("500원 짜리", int(exmoney//500),"개")
a=exmoney%500
print("100원 짜리", int(a//100),"개")
b=a%100
print("50원 짜리", int(b//50),"개")
c=b%50
print("10원 짜리", int(c//10),"개")
print("나머지",int(c%10),"원")


<오늘의 메모장>
a="명작"
b="이야기"
print(a+" "+b)

14p(중요) 복합연산자 어떻게 쓰는지 뜻이뭔지 꼭 알기
a를 선언해야됨!

== : 앞에와 뒤가 같니?라고 물어보는 관계연산자
!= : 앞에와 뒤에가 같지 않니?라고 물어보는 관계 연산자
=과 ==의 차이 앍기!
= : 오른쪽에 있는 걸 왼쪽에 대입해줘~ 라는 뜻
>=인데 =>라고 쓰는 거 주의하기.

and : 다~ 참이어야만 참 (and 여러개 쓸 수 있음)
or : 하나가 참이면 참
not : 반대로 만들어 주는 것

스포 : if는 이 조건이 참일 때만 동작하는 애
