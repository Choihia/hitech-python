#print(len("hello"))
#print(len("12345"))
#%%
print("hello"[1])
#%%
num_char=(input("당신의 이름 : "))
print(type(num_char))
# %%
num_char=len(input("당신의 이름 : "))
new_num_char=str(num_char)
print("당신의 이름은 " + new_num_char + "character.")
# %%
a=input("두자리 숫자 : ")

a1=int (a[0])
a2=int (a[1])

print(a1+a2)
# %%
height= input("당신의 키(m) : ")
weight= input("당신의 몸무게(kg) : ")

bmi= int(weight)/float(height)**2

bmi_int=int(bmi)

print(height)
print(weight)
print(f"bmi지수 : {bmi_int}")
# %%
age = input("당신의 나이 : ")

age_int = int(age)

years = 90-age_int
months = age_int*12
weeks = age_int*52
days = age_int*365

print(months)

message = f"당신의 90살까지 년수는 {years}년, 월수는 {months}월, 주수는{weeks}주, 일수는 {days}일 남았습니다."
print(message)
# %%
#팁 계산기
#총 얼마?
#팁은 몇%
#팁을 포함 얼마
#몇명이 지불?
#1인당 지불금액

print("팁 계산기")

order = float(input("음식 가격 : "))
tip_per = int(input("팁은 몇 퍼센트? : "))
people = int(input("몇명인가요? : "))

tip = order*(tip_per/100)
total = order+tip
one_people = total/people

final= round(one_people,2)

print(f"팁 포함 한명당 {final}$")
# %%
print("롤러코스터 매표기")
height = int(input("키를 입력하세요 : "))

if height > 120:
    age = int(input("나이를 입력하세요 : "))
    if age<12:
        print("무료입니다.")
    elif age <= 18:
        print("7000원 입니다.")
    else :
        print("12,000원 입니다.")
else:
    print("이용하실 수 없습니다.")

# %%
