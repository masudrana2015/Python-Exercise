guess_num=int(input())
actual_num=10

if guess_num < actual_num:
    print("your guess is almost there")
elif guess_num > actual_num:
    print("your guess is higher")
else:
    print("Your Guess Is Correct!")

