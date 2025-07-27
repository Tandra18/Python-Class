import random


def guessing_game():
    print("Guess any number from 1 to 10\n"
          "You have 5 attempts!")
    secret_number = random.randint(1,11)
    attempts = 5

    while True:
        try:
            guess_num = int(input("Enter your guess : "))

            if not 0 < guess_num < 11:
                print("\nGuess number must be between 1 to 10\n")
                continue

            elif attempts == 1:
                print("💀Game Over! Too much attempts! ")
                break

            elif guess_num > secret_number:
                attempts -= 1
                print(f"\nGuess number is higher than the secret number!\n"
                      f"You have {attempts} attempts left!")

            elif guess_num < secret_number:
                attempts -= 1
                print(f"\nGuess number is lower than the secret number!\n"
                      f"You have {attempts} attempts left!")

            else:
                print(f"🎉You are correct! Your attempts are {attempts} times!")
                break

        except ValueError:
            print("🚫Please only enter a number!")


guessing_game()
