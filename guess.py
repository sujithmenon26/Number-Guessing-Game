guess_number = 7
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    number = int(input("enter number \n"))
    guess_count += 1
    if number == guess_number:
        print("you won!")
        break
    elif number > 8:
        print("number is smaller")
    elif number < 6:
        print("number is greater")

else:
    print("max attempts you lose ")