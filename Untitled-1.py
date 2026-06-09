import random

num = random.randint(1,1000)
#print(num)
tries=0
while True:
    guess = int(input("guess a number between 1 and 1000 :-"))
    tries+=1
    if guess == num:
        print("you have won the game!")
        break
    elif num>guess:
        print("Too Low, plese give a higher number")
    elif num<guess:
        print("Too high, plese give a lower number")
    else:
        print("give a whole number between 1 and 1000")

print (tries)
