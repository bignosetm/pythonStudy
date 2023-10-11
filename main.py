'''
python
#변수선언
변수 선언 할때는 타입 설정 안해 됨.
출력은 그냥 print
문자열 여러 문단 할려면 """  """

#캐스팅(형변환)
서로 다른 타입을 출력 할려면 타입을 동일하게 맞춰줘야함 이걸 캐스팅(형변환)이라고 한다.
x=3;
y="3"
print(x+y); --> 에러
print(str(x)+y)--> 정수를 str를 써서 문자열로 만들어줌
또는 print(x+int(y)) string타입인 y를 정수형으로 만들어줌

#조건문
if 조건식 :
    실행문

#함수 def
def 함수명(매개변수):
    실행문

#반복문
#for
for i(변수) in range(반복횟수):
    실행문

#while
i = 0
while i<3:
    실행문
    i +=1

###for문과 while문의 차이는 while은 반복횟수를 지정할 수 있음###

#리스트(List)
우리가 흔히쓰는 배열임.
x = [1, 2, 3, 4]
len(x) --> 리스트 길이 구하기

x = [4, 3, 2, 1]
y = sorted(x)---->[1, 2, 3, 4] 리스트가 정열됨.

y = sum(x)--->10 배열이 숫자로 구성되어 있으면 모두 합함.
#반복문과 리스트 조합해서 쓰기
for n in x:
    print(n)
---> 4 3 2 1이 출력

#리스트에서 위치 찾기
x = [4, 3, 2, 1]
y = [1, "hello", "there"]
x.index(3)--> 1 그냥 값의 위치값만 찾아줌 3번째 요소의 값이 1이 아니라 리스트에 있는 3의
                위치가 1번째 인덱스라는 뜻
y.index("hello")-->1 hello의 값의 위치가 1번째 인덱스라는 뜻

#값이 있는지 알기
print("hello" in y) --->true
print("bye" in y) --- false

#튜플(Tuple)
x = (1, 2, 3) 
y = ('a', 'b', 'c')
x.index(2) --> 1 리스트의 값의 위치 구하기랑 동일

---->리스트라 튜플 차이 리스트는 sorted를 이용해서 정렬을 하던가 아니면 값을 추가할 수 있지만
    튜플은 한번 값을 저장하면 따로 수정이나 내용 변환이 불가능함
    리스트는 리스트내에 있는 함수를 사용할 수 있지만 튜플은 불가능

#딕션너리(dict())
---> key와 value로 구성
x = dict()--->{}
y = {} --->{}
x = {
    key: value, ---->key 와 value로 구성
    key: value, ---->key는 불변하는 값이여야함.
    "name": "Tm",
    "age": 12,
호출할때
x.[key] ---> value
x.["name"] ----> "Tm"
}
print(x.keys()) ---> 딕션너리의 모든 key를 보여줌
print(x.values()) ---> 딕션너리의 모든 value값을 보여줌

x[key] = value 새로운 key 추가 and value 수정

#리스트와 딕션너리를 이용한 혼합 문제
fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d = {}
for f in fruit: #fruit리스트를 한번씩 돔
    if f in d: #딕션너리 d안의 변수 f의 키가 있으면 value에 +1
        d[f] += 1
    else: #딕션너리 d안의 변수 f의 키가 없으면 f를 키로 해서 value 값을 1로 설정
        d[f] = 1
print(d)

#class와 object
class는 함수와 변수들의 합
class Person:
    def __init__(self, name): --> 여기서 __init__는 초기화를 위한 함수,
        self.name = name     오브젝트 생성(인스턴스 생성)과 관련하여 데이터 초기를 실시하는함수
                             아마 첫 매개변수 선언을 할때 쓰면 되는것 같다. "self.매개변수"를 해야
                             클래스 내에서 사용 가능한듯 하다.
                             #여기서 name은 
        
    def say_hello(self, to_name): ---> 여기서 self는 인스턴스 자신을 가르키고 있다. 약간 무적 변수?
        print("안녕" + to_name + "나는"  + self.name)

p = Person(n) -->n에는 매개변수 name의 값이 들어 간다.
p.say_hello() ---> "안녕 나는 워니" 가 출력
!!여기서!!
jenny = Person("제니")
jenny.say_hello()---> "안녕 나는 제니" 라고 출력하고 싶으면
jenny.say_hello("미지") --> "안녕 미지(to_name) 나는 제니(self.name)" 함수의 매개변수도 사용함

#상속
class Police(Person): -->Person클래스에 있는 함수나 다 쓸수 있음-->상속
    def arrest(self, to_arrest):
        print("넌 체포됐다, "+to_arrest)


#클래스 예들
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕 " + to_name+" 나는 "+ self.name+ " 나이는 "+str(self.age))

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다, "+to_arrest)

class Programmer(Person):
    def program(self, to_programmer):
        print("프래그래머: "+ to_programmer)

wonie = Person("워니", 20)
jenny = Police("제니", 21)
michael = Programmer("마이클", 22)

wonie.say_hello("지욱")
jenny.say_hello("해유")
jenny.arrest("지우")
michael.program("오토")


from animal import dog # animal이라는 패키지에서 dog 모듈을 가져옴
from animal import cat

from animal import * #animal 패키지가 갖고 있는 모듈을 다 불러와

#d = dog.Dog() #dog라는 모듈안에서 Dog라는 클래스를 가져옴
#d.hi() #클래스 안에있는 hi라는 함수 사용

d = Dog()#바로 클래스를 가져와서 사용가능
c = Cat()

d.hi()
c.hi()

'''
