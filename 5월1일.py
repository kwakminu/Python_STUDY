딕셔너리의 특징 : 딕셔너리에 들어가는 키값은 유일해야돼~
(유일하게 구분되는 애를 키를 쓰고 혹시 동일한 값이 나올 수 있어! 싶은 건 값으로 주기!)
26p. 두개 다 값을 뽑을 수 있다! (똑같다)


20분 ~ 32분 다시 듣기 (못들음)
28p. keys, values (s가 붙어있어야 되는 거 확인!)
29p. 딕셔너리는 키를 이용해서 데이터에 접근할 수 있고, 데이터를 갱신할 수 있고, 있는지 없는지 찾아볼 수 있다.

a = []
b = list()
a, b 같은 거!
c = ()
d = tuple()
c, d 같은 거!
e = {}
-> 딕셔너리이다!



30p. 숫자도 %s로 찍을 순 있다. (왜 %s인데 9가 찍히는지에 대한 대답)
30p. 여기서 for k in singer.keys() 안하고 for k in singer해도 딕셔너리에서 키가 중요하니까 키가 뽑혀서 결과가 똑같음!


31p. itemgetter(1)이면 키가 아니라 값으로 정렬 (하지만 시험에서 이런 건 안나온다!)

<오늘의 코드>

"""import operator

D = {}

D = {'T' : '토', 'E' : '에', 'H' : '헨', 'G' : '고', 'J' : '제'}
L = sorted(D.items(), key = operator.itemgetter(1))

print(L)"""

#key = operator.itemgetter(1)는 end = " " 같은거

D ={'one' : '하나', 'two' : '둘', 'three' : '셋', 'four' : '넷'}

k = input("단어를 입력하세요 . ")
if k in D :
    print(D[k])
else :
    print("없는 단어입니다.")
