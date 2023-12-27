if 문 쓸 때 들여쓰기 어디에 걸려있는지 확인하는 거 매우 중요하다!

if elif 구문 쓸 때 중요한 것 : 제일 조그만 걸 먼저 빼기! 조금씩 조금씩 꺼내야
아닌 애들 중에서 그걸 찾고 아닌 애들 중에서 그걸 찾고.. 하는 게 좋다!

"""n = int(input("숫자를 입력하세요: "))

if n>0 :
    print("양수입니다.")
elif n==0 :
    print("0입니다.")
else :
    print("음수입니다.")"""

"""#실습 5
print("##철수와 영이의 가위, 바위, 보 게임")
cs = input("철수는 무엇을 낼까요? ")
ye = input("영이는 무엇을 낼까요? ")

if cs == "가위" :
    if ye == "가위" :
        print("무승부입니다.")
    elif ye == "바위" :
        print("영이가 이겼습니다.")
    elif ye == "보" :
        print("철수가 이겼습니다.")
    else :
        print("영이의 값입력 오류=>", ye)
elif cs == "바위" :
    if ye == "가위" :
        print("철수가 이겼습니다.")
    elif ye == "바위" :
        print("무승부입니다.")
    elif ye == "보" :
        print("영이가 이겼습니다.")
    else :
        print("영이의 값입력 오류=>", ye)
elif cs == "보" :
    if ye == "가위" :
        print("영이가 이겼습니다.")
    elif ye == "바위" :
        print("철수가 이겼습니다.")
    elif ye == "보" :
        print("무승부 입니다.")
    else :
        print("영이의 값입력 오류=>", ye)
else :
    print("철수의 값입력 오류=>", cs)"""

"""flag = (input("마음에 드는 옷이 있나요? (예/아니요) : "))

if flag == "예" :
    print ("축하합니다!")
    cloth = int(input("가격이 얼마인가요?"))
    if cloth <= 100000 :
               print("구매합니다.")
    else :
        print("구매하지 않습니다.")
               
elif flag == "아니요" :
    print ("아쉽군요!")
else :
    print("예 또는 아니요를 입력하세요!")"""
   


"""g = int(input("점수를 입력하세요 : "))

if g>=90 :
        print("A\n학점입니다. ^^")
elif g>=80 :
    print("B/n학점입니다. ^^")"""

"""#실습 5
print("##철수와 영이의 가위, 바위, 보 게임")
cs = input("철수는 무엇을 낼까요? ")
ye = input("영이는 무엇을 낼까요? ")

if cs == "가위" :
    if ye == "가위" :
        print("무승부입니다.")
    elif ye == "바위" :
        print("영이가 이겼습니다.")
    elif ye == "보" :
        print("철수가 이겼습니다.")
    else :
        print("영이의 값입력 오류=>", ye)
elif cs == "바위" :
    if ye == "가위" :
        print("철수가 이겼습니다.")
    elif ye == "바위" :
        print("무승부입니다.")
    elif ye == "보" :
        print("영이가 이겼습니다.")
    else :
        print("영이의 값입력 오류=>", ye)
elif cs == "보" :
    if ye == "가위" :
        print("영이가 이겼습니다.")
    elif ye == "바위" :
        print("철수가 이겼습니다.")
    elif ye == "보" :
        print("무승부 입니다.")
    else :
        print("영이의 값입력 오류=>", ye)
else :
    print("철수의 값입력 오류=>", cs)""

"""wt = int(input("수박의 무게를 입력하세요: "))

if wt >= 10 :
         print("1등급입니다.")
elif wt >= 7 :
         print("2등급입니다.")
elif wt >= 4 :
         print("3등급입니다.")
else :
    print("4등급입니다.")"""

gd = input("성별을 입력하세요. (남/여)")

if gd == "남" :
    arm = int(input("팔굽혀펴기를 몇회하셨나요?"))

    if arm >=10 :
        print("합격(Pass)입니다.")
    else :
        print("불합격(Fail)입니다.")
elif gd == "여" :
    arm = int(input("팔굽혀펴기를 몇회하셨나요?"))

    if arm >= 5 :
        print("합격(Pass)입니다.")
    else :
        print("불합격(Fail)입니다.")
else :
    print( "남/여를 입력하세요.")
