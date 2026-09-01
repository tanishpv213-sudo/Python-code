import random
playing = True
number = str(random.randint(1, 9))

print("I will generate a number from 0 to 9. You have to guess it!")
print("This game ends when you get 1 hero!")
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game!")
        print("The number was",number)
        break
    else:
        print("Your guess is wrong! Try again! \n")