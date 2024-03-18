#%%
import os

for i in range(1,9+1,1):
    for j in range(1,9+1,1):
        answer = i*j
        print(f'{i} * {j} = {answer}')
        j+=1
    print('---'*10)        
    i+=1

# %%
