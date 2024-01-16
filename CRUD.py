lis = ["Hasan", "AI-Quest", "Django", "23"]

while True:
    user = int(input("What do you want:\nChose a number: 1.Read, 2.Add, 3.Delete, 4.Update, 5.Quite: "))
    if user == 1:
        print(f"You Chose: 1 {lis}")
        break
    elif user == 2:
        print("You Chose: 2 ",lis.append(input("Add value: ")))
        print("After add new item: ",lis)
        break
    elif user == 3:
        print(lis)
        rm = str(input("What you want to temove: "))
        print("You Chose: 3 ",lis.remove(rm))
        print(f"After delete {rm}: ",lis)
        break
    elif user == 4:
        print(lis)
    
        rmv = str(input("What you want update: "))
        uv = str(input("Input new item: "))
        if rmv in lis:
            l = lis.index(rmv)
            lis[l] = uv
            print(f"After update {rmv} value, Result: {lis}")
        break
    elif user == 5:
        print("You Chose 5 Break")
        break