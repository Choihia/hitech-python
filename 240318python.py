#%%
print('hello world')

# %%
a = 'a'
print(a, type(a))
a = 'asdf'
print(a, type(a))
a = 1
print(a, type(a))
a = 1.1
print(a, type(a))

# %%

a = 1
b = 2
c = a + b

print(f'{a}+{b} = {c}')

a = 200
b = 1000
c = a + b

print(f'{a}+{b} = {c}')

# %%

a = [1,2,3,4,5]
print(a,type(a))

a = (1,2,3,4,5)
print(a,type(a))

a = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(a,type(a))

# %%
import os

print('this is calculation program')

a = input('in a : ')
a = int(a)
print(a,type(a))

op = input('in op(+, -, *, /, //, **) : ')

b = input('in b : ')
b = int(b)
print(b,type(b))


if (op == '+'):
    c = a+b
elif (op == '-'):
    c = a-b
elif (op == '*'):
    c = a*b
elif (op == '/'):
    c = a/b
elif (op == '//'):
    c = a//b
elif (op == '**'):
    c = a**b
else:
    print('만족하는 op가 없습니다.')

print(c, type(c))
print(f'{a} {op} {b} = {c}')



# %%
#구구단
import os

for i in range(0,9+1,1):
    print(i)

for i in[1,2,3]:
    print(i)
for i in (1,2,3):
    print(i)



# %%
print('---'*10)
a1 = "10"*10
print(a1)

a2 = ''
for i in range(1,10+1,1):
    print(i)
    a2 +='10'
print(a2)
print(a1 == a2)
print('---'*10)
# %%
