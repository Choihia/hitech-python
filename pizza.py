#%%
print("파자가게에 어서오세요")
pizza_size = input("원하시는 사이즈를 선택 하세요 L M S").upper()

bill = 0

if pizza_size in ['L', 'M', 'S']:
    Pepperoni = input("페퍼로니 추가 하시겠습니까? (숫자입력 추가 안할시 0)").upper()
    Cheese = input("치즈를 추가 하시겠습니까? (숫자입력 추가 안할시 0)").upper()
    if pizza_size == 'L':
        bill = 30000        
        print("L사이즈는 30,000원 입니다.")
        if Pepperoni == '0' and Cheese == '0':
            print(f'총 {bill}입니다.')
        else:
            bill = bill + (int(Pepperoni)*2000) +(int(Cheese)*3000)
            print(f'페퍼로니추가 {Pepperoni}번, 치즈추가 {Cheese}번 추가하셨습니다')
            print(f'총 {bill}입니다.')                
    elif pizza_size == 'M':
        bill = 20000
        print("M사이즈는 20,000원 입니다")
        if Pepperoni == '0' and Cheese == '0':
            print(f'총 {bill}입니다.')
        else:
            bill = bill + (int(Pepperoni)*2000) +(int(Cheese)*3000)
            print(f'페퍼로니추가 {Pepperoni}번, 치즈추가 {Cheese}번 추가하셨습니다')
            print(f'총 {bill}입니다.')
    elif pizza_size == 'S':
        bill = 15000
        print("S사이즈는 15,000원 입니다")
        if Pepperoni == '0' and Cheese == '0':
            print(f'총 {bill}입니다.')
        else:
            bill = bill + (int(Pepperoni)*2000) +(int(Cheese)*3000)
            print(f'페퍼로니추가 {Pepperoni}번, 치즈추가 {Cheese}번 추가하셨습니다')
            print(f'총 {bill}입니다.')        
elif pizza_size not in ['L', 'M', 'S']:
    print("잘못된 사이즈입니다")