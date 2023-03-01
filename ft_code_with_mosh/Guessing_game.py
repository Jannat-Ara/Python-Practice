secret_numer= int(input("Enter the number:"))
Guess_count = 0
Guess_limit = 3
while Guess_count < Guess_limit:
    Guess = int(input('Guess:'))
    Guess_count = Guess_count +1
    if Guess == secret_numer:
        print("The number you have guessed is correct!")
        break
else:
    print("Sorry, Try again!")