35p s.strip()은 좌우 양쪽 공백 삭제 (가운데에 있는 공백에 적용되는 게 아니다!)
36p ss.strip('<>') 은 좌우의 <와 > 모두 제거된다!
37p 조건문에서 not과 or는 쓸 때 항상 조심하기!
39p 끊어놓고 하면 된다!

42p 가볍게 보기!
43p 중요하게 보기!

46p replace() 메서드 활용 꼭 안해도 됨!

<오늘의 코드>

"""ss = input("입력 문자열 ==> ")
print("출력 문자열 ==> ", end = "")

if ss.startswith('(') == False :
    print("(", end = '' )

print (ss, end = '')

if ss.endswith(')') == False :
    print(")", end = '')"""
"""
inStr = "   한글 Python 프로그래밍   "
outStr = ""

for i in range(0, len(inStr)) :
    if inStr[i] != ' ' :
        outStr = outStr + inStr[i]

print("원래 문자열 ==>" + "[" + inStr + "]")
print("공백 삭제 문자열 ==> " + "[" + outStr + "]")"""

"""
inStr = "<<<파<<이>>썬>>>"
outStr = ""

for i in range(0,len(inStr)) :
    if inStr[i] != "<" and  inStr[i] != ">" :
        outStr += inStr[i]ㅁ
       
print("원래 문자열 ==>" + "[" + inStr + "]")
print("공백 삭제 문자열 ==> " + "[" + outStr + "]")"""

"""ss = input("입력 문자열 ==> ")

print("출력 문자열 ==> ", end = "")
print(ss.replace('o', '$'))"""

"""
ss = input("입력 문자열 ==> ")

print("출력 문자열 ==> ", end = '')

for i in range (0, len(ss)) :
    if ss[i] != 'o' :
        print(ss[i], end = '')
    else :
        print('$', end = '')"""

"""a = input("문자열 입력 : ")

if a.isdigit() :
    print("숫자입니다.")
elif a.isalpha() :
    print("글자입니다.")
elif a.isalnum() :
    print("글자+숫자입니다.")
else :
    print("모르겠습니다.")"""
