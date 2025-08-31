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
    
if(comp-you== -1 or comp-you== 2):
    print("you lost!")
    
else:
    print("you won!")