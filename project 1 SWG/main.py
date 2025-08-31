import random
'''
1 for snake
-1 for water
0 for gun
'''
comp = random.choice([-1,0,1])
youStr = input("Enter your Choise (S, W, G): ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
you = youDict[youStr]

print(f"You chose {reverseDict[you]} and computer chose {reverseDict[comp]} so:")

if(comp==you):
    print("Its a draw")
    
else:
    if(comp==1 and you==-1):
        print("you lost!")
    elif(comp==1 and you==0):
        print("you lost!")
    elif(comp== -1 and you== 1):
        print("you won!")
    elif(comp== -1 and you== 0):
        print("you lost!")
    elif(comp== 0 and you== 1):
        print("you lost!")
    elif(comp== 0 and you== -1):
        print("you win!")
    else:
        print("Something went wrong")