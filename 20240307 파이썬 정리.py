#사칙연산
a = 7
b = 3
c = a + b
print(c)

d = a - b
print(d)

e = a * b
print(e)

f = a / b
print(f)   #나누기

g = a % b #나머지값 
print(g)

h = a // b #소숫점 버리기
print(h)

#비교 연산자

if a == 7:
    print("7이 맞음")

if a != 7:
    print("7이 아님")

if a < 8:
    print("8 미만")

if a > 6:
    print("6 초과")

if a <= 7:
    print("7보다 작거나 같음")

if a >= 6:
    print("6보다 크거나 같음")

#할당 연산자
a = 7
a *= 10 # a * 10을 a로 변경
print(a)

a = 7
a += 10 # a+10을 a값 변경
print(a)

a = 7
a -= 10 # a - 10을 a로 변경
print(a)

a = 7
a /= 10 # a / 10을 a로 변경
print(a)

a = 7
a %= 10 #a / 10의 나머지를 a로 변경
print (a)

a = 7
a //= 10 # a /10의 나머지를 버린 값을 a로 변경
print (a)

# 논리 연산자
x = True
y = False  
if x and y:
    print("Yes")
else:
    print("No")
# and는 두 값이 전부 True 일 경우 yes 한쪽만 True일 경우 no 

if x or y:
    print("Yes")
else:
    print("No")
# or은 두 값 중 하나라도 True면 yes

a = 7
if not a <=8:
    print("not 연산 결과 : True")
else:
    print("not 연산 결과 : False")
# not 연산자는 결과를 반대로 나오게 한다. 7은 8보다 작거나 같아서 True지만 not 연산자가 적용되어 False값이 나오게 된다.

#멤버쉽 연산자

z = [1,2,3,4,5]
q = 3 in z #True
print(q)

q = 3 not in z #False
print(q)

# in은 z그룹에 3이 있다면 True를 출력함 없다면 False를 출력함 
# not in은 z 그룹에 3이 있다면 False 없다면 True 6을 넣을경우 6은 z 그룹에 없으므로 True가 나오게 된다.

#Identity연산자
r = "ABC"
u = r
print(r is u)
#r이랑 u가 동일하므로 True
print(r is not u)
#r이랑 u가 동일하므로 False 만약 동일하지 않다면 True