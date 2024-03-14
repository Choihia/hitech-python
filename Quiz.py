#3-1
print("Hello world")
print("Hello  world")
print("Hello"+"world")
print("hello"+" "+"world")

#3-2
# print("오늘은 파이썬 챌린지 3일차 입니다)
# print('디버깅 "+" 연습중입니다')
#  print('내일은("금요일" + "입니다)')
# print(("그래서 챌린지가 없습니다"))
#디버깅
print("오늘은 파이썬 챌린지 3일차 입니다")
print('디버깅 ' + '연습중입니다')
print('내일은 금요일' + '입니다')
print("그래서 챌린지가 없습니다")

#3-3
p = input("당신의 이름은 무엇입니까? : ")
print(p)

p = input("당신은 이름이 무엇입니까? : ")
print("나는" + " " + p + " " + "입니다")

#3-4
p = input("당신의 이름은 무엇입니까? : ")
print(len(p))

#3-5
name = input("당신의 이름은? : ")
length = len(name)
print(length)

#3-6
a = input("a : ")
b = input("b : ")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)

# #3-7 퀴즈 : 올바른 파이썬 코드는 무엇일까요?
# ㄱ. var a = 12
# ㄴ. a = 12
# ㄷ. a:12
# ㄹ. 12 = a
# 정답 : ㄴ

# 3일차 종합 챌린지 퀴즈 : 내가 좋아하는 영화를 입력하고, 영화의 주인공을 입력해서
# 내가 좋아하는 영화는 000이고, 주인공은 000다를 출력하세요.
movie = input("좋아하는 영화는? : ")
character = input("영화의 주인공은? : ")

print("좋아하는" +" "+ "영화는" + " " + movie + "이고" + ", " + "주인공은" + " " + character+"(이)다")