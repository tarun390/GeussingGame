from random import random

randomNumber = int(random() * 10) 
tries = 5
print("Your Goal in this game: \n"
      "1==> You have to guess the numbers between 0 to 10.\n"
      "2==> You will get three tries to guess the number.\n")
while True:

    if tries == 0:
        print("!! GAME OVER !! :( \n")
        print("The correct number was", randomNumber)
        break

    print("You have ", tries, " tries left !!\n") 
    inp = int(input("Guess the number between 0 to 10\n"))

    if inp > randomNumber:
        print("\nYour number is too big guess smaller number\n")
        tries = tries - 1
        continue
    elif inp < randomNumber:
        print("\nYour number is too small guess bigger number\n")
        tries = tries - 1
        continue
    else:
        print("\nCongratulations you have guessed correct number :)\n")
        tries = tries - 1
        break