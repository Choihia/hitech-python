#%%
Dan_Start = 2
Dan_Finish = 9
Step_Start = 1
Step_Finish = 9

for dan in range (Dan_Start,Dan_Finish+1,1):
    for step in range (Step_Start,Step_Finish+1,1):
        answer = dan*step
        print (f"{dan}*{step}={answer}")
    print ("---"*10)


# %% 구구단 가로형태로 출력(1) 
#2*1=2	2*2=4	2*3=6 ... 2*7=14	2*8=16	2*9=18
Dan_Start = 2
Dan_Finish = 9
Step_Start = 1
Step_Finish = 9

for dan in range (Dan_Start,Dan_Finish+1,1):
    for step in range (Step_Start,Step_Finish+1,1):
         answer = dan*step
         msg = f"{dan}*{step}={answer}"
         print (msg,end='\t')
    print('\n')


#%%
#2*1=2	2*2=4	2*3=6...2*7=14	2*8=16	2*9=18
Dan_Start = 2
Dan_Finish = 9
Step_Start = 1
Step_Finish = 9

for dan in range (Dan_Start,Dan_Finish+1,1):
    msg=''
    for step in range (Step_Start,Step_Finish+1,1):
        answer = dan*step
        msg += f"{dan}*{step}={answer}\t"        
    print(msg)


# %%구구단 가로형태로 출력(2)
 #2*1=2	3*1=3...7*1=7	8*1=8	9*1=9
Dan_Start = 2
Dan_Finish = 9
Step_Start = 1
Step_Finish = 9

for step in range (Step_Start,Step_Finish+1,1):
    for dan in range (Dan_Start,Dan_Finish+1,1):
        answer = dan*step
        msg = f"{dan}*{step}={answer}"
        print (msg,end='\t')
    print('\n')


#%%
#2*1=2	3*1=3...7*1=7	8*1=8	9*1=9
Dan_Start = 2
Dan_Finish = 9
Step_Start = 1
Step_Finish = 9
line=''

for step in range (Step_Start,Step_Finish+1,1):    
    msg=''
    for dan in range (Dan_Start,Dan_Finish+1,1):
        answer = dan*step
        msg += f"{dan}*{step}={answer}"
        msg += '\t'
    line += msg+'\n'        


print(line)


# %% 조건문 구구단
    #2단시작 6단끝 5스텝시작 8스텝끝
Dan_Start = 2
Dan_Finish = 6
Step_Start = 5
Step_Finish = 8
line=''

for step in range (Step_Start,Step_Finish+1,1):    
    msg=''
    for dan in range (Dan_Start,Dan_Finish+1,1):
        answer = dan*step
        msg += f"{dan}*{step}={answer}"
        msg += '\t'
    line += msg+'\n'
    
    

print(line)



# %% 조건문 구구단
    #2단시작 6단끝 5스텝시작 8스텝끝
Dan_Start = 2
Dan_Finish = 9
Step_Start = 1
Step_Finish = 9
line=''


for step in range (Step_Start,Step_Finish+1,1):    
    msg=''
    for dan in range (Dan_Start,Dan_Finish+1,1):
        if 5<=step<=8 and dan<7:
            answer = dan*step
            msg += f'{dan} * {step} = {answer}'
            msg += '\t'        
    line += msg+'\n'

print(line)  
# %%
star = '*'
for i in range (1, 6, 1):
    print (star)    
    star += '*'
# %%
star = '*'
sp = ' '

for y in range (5,0,-1):
    msg_sp=f' '*(y-1)
    msg_star=f'*'*6
    print(msg_sp+msg_star)
# %%
for i in range(1,5+1,1):
    print(i, '*'*i)

digits_max = 5
for i in range(digits_max,0,-1):
    msg_empty = f' '*(i-1)
    msg_star = f'*'*(digits_max-i+1)
    print(i, msg_empty+msg_star)