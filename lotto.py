#%%
import random

print("로또번호 랜덤 생성")
lotto = []


for i in range (1,7,1):
    random_number = random.randint(1,45)
    lotto.append(random_number)

print(lotto)
# %%
