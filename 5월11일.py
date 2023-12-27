함수와 메소드의 차이!
함수 -> 혼자 단독으로 사용 가능

27p. 중요!! 사용되는 데가 무궁무진함.
굳이굳이 오른쪽으로 자르고 싶으면 rsplit()!
split은 자르고, join은 붙이는 것!


14~17분 다시 듣기 (실습4, 제대로 못들음)

오프셋 리턴 -> 인덱스를 리턴하는구나 라고 생각해도 됨!

<오늘의 코드>

"""ss = input("날짜(연/월/일) 입력 ==> ")

ssList = ss.split('/')

print("입력한 날짜의 10년 후 ==> ", end = "")
print(str(int(ssList[0])+10)+"년", end = "")
print(ssList[1] + "월" , end = "")
print(ssList[2] + "일", end = "")"""

"""
lylics = 'Half of my hear is in Havana'
lylicsList = []
for i in lylics.split() :
    lylicsList.append((i, i.upper()))
print(lylicsList)

lylics = 'Half of my hear is in Havana'
lylicsList = [(i, i.upper()) for i in lylics.split()]
print(lylicsList)"""

"""k = input("주민등록번호를 입력하세요 : ")
print(k[8])

if k.startswith("1",7) or k.startswith("3", 7) :
    print("남성입니다.")
else :
    print("여성입니다.")
#인덱스 세는 거 0부터인 거 진짜 명심하자!!!"""
