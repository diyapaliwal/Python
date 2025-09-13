''' We are going to write a program that generates a random number and asks the user to guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
Hint: Use the random module. '''
import random
randomNo = random.randrange(1,101)
count = -1
userNo = None
while(userNo != randomNo):
    userNo = int(input("Guess a number between 1 to 100: "))
    count+=1
    if (userNo < randomNo):
        print("Higher number please!")
    
    elif(userNo > randomNo):
        print("Lower number please!")
    
    else:
        print("Yay! You guessed it right!")

print(f"you gussed it correct after {count} wrong tries.")