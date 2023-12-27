2주차 실습, 연습 코드들

hello="안녕하세요"
print(hello)
university="숭실대학교"
grade="1"
department="사회복지학부"
print("저는", university, department, grade, "학년 입니다.")
name = input("이름을 입력하세요.")
print(name ,"님 환영합니다")
gender = input("성별을 입력하세요.")
schoolnumber = input("학번을 입력하세요.")
print(name, "님의 성별은", gender)
print(name, "님의 학번은", schoolnumber, "입니다")

print("반갑습니다. 계좌 이체를 위한 정보를 입력하세요.")
exportnumber=input("1) 출금 계좌 번호 :")
inportbank=input("2) 입급 은행 :")
inportnumber=input("3) 입금 계좌 번호 :")
getperson=input("4) 수취인 :")
getmoney=input("5) 이체금액 :")
print()
print("입력하신 정보는 아래와 같습니다.")
print("===============================")
print("-출금 계좌 번호 :",exportnumber)
print("-입금 은행 :", inportbank)
print("-입금 계좌 번호 :", inportnumber)
print("-수취인 :", getperson)
print("-이체 금액 :", getmoney)
print("===============================")


print("택배 배송을 위한 정보를 입력하세요.")
exnumber=input("1) 받는 분 이름 :")
inpbank=input("2) 받는 분 연락처 :")
innumber=input("3)받는 분 주소 :")
getpe=input("4) 배송 메세지 :")
print()
print("아래 정보로 배송하겠습니다.")
print("===============================")
print("-받는 분 이름 :",exnumber)
print("-받는 분 연락처 :", inpbank)
print("-받는 분 주소 :", innumber)
print("-배송 메세지 :", getpe)
print("===============================")

잔머리를 써서 일을 적게 하는 방법을 생각하자!

----------

3장 문자열

파이썬에서는 작은따옴표, 큰따옴표 둘다 똑같이 인식함
앞에 있으면 뒤에도 있어야 함! (ex : '안녕 x)
오른쪽에 있는 변수는 선언 된 적이 있어야함
따옴표를 안쓰면 변수로 인식

n 줄에 거친 문자열을 출력하거나, 어떤 변수에 할당할 때
하나짜리 따옴표가 아니라, n번의 따옴표를 서야됨.
(6P)

7p 더하기와 곱하기라는 연산자는 문자열에서도 쓸 수 있다!
+를 쓸 수도 있고 ,을 쓸 수도 있다. (두개가 완전히 똑같지는 않다. 스페이스 붙느냐 안붙느냐의 차이)
플러스는 딱 붙고 ,는 한번 띄어짐.
빈 문자열도 문자열이다!
8p 띄어쓰기 없으면 틀린다. 빈문자열도 문자열이니까 조심하기!!! (중요)
따옴표사이에 있는 모든 에를 문자열 취급!
9p len함수 : 세주는 함수

Q 코드편집기에서는 왜 len 앞에 print 써야하지? :당연히 써야함. Shell이니까 괜찮았던것!

print("실패하는 것보다"
"도전하지 않는 것을"
"두려워하지마라.")

text='쉽고 재미있는 파이선 프로그래밍'
print(len(text))
name=input('이름을 입력하세요: ')
welcome=name,'님, 반갑습니다'
print(welcome)


중간고사를 볼 때 틀린부분을 고치라는 문제도 나오기 떄문에 틀린 걸 해서 틀려보기

10p 문자열 메소드는 주로 다루지 않고 아주 기본적인 것만 소개
함수와 메소드는 유사한 아이인데 함수는 독자적으로 메소드는 기대서 쓰는 것 (아직 이해 안되는 게 정상!, 배우다 보면 메소드 이해 될 것)
이렇게 많구나~ 아~ 하고 지나가면 됨.

12p 문자열 형식화
%s 문자열
%d 정수
%f 부동소수점 실수
(중요!) "내 이름은 %s입니다." %"홍길동" -> 사이에 쉼표가 없다는 거 구분
shell이니까 프린트가 없는 거 구분하기.
13p 괄호 쓰면 순서대로 들어감

print("%d 곱하기 %d은 %d이다"%(2,3,6))
print("%s의 %s 과목 점수는 %d점이다"%("철수","수학",100))

number1=int(input("첫 번째 값을 입력하시오:")) -> input은 답을 쓰면 무조건 str으로 받기 때문에 int로 바꿔줘야함!
number2=int(input("두 번쨰 값을 입력하시오:"))
print("입력된 두가지 값은 %d와 %d입니다."%(number1, number2))
