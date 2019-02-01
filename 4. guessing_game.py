print("Guess the word")
print("The animal having strips of black and white, much more look like a deer")
ans = "Zebra"
guess_counter = 1
guess = ""
out_of_guess = False

while guess != ans and not(out_of_guess):
    if guess_counter <=3 :
        print("%d guesses left" %(4 - guess_counter))
        guess = input("Enter your guesses: ")
    else:
        out_of_guess = True

    guess_counter += 1

if out_of_guess:
    print("you lose !")
else:
    print("you won !")
