import random

# Lists to track attempts for statistics
user_attempts_list = []
computer_attempts_list = []

def guess(limit):
    '''User tries to guess a random number.'''
    random_number = random.randint(1, limit)
    attempts = 0
    guess_num = 0
    print(f"\nI have chosen a number between 1 and {limit}. Try to guess it!")

    while guess_num != random_number:
        try:
            guess_num = int(input("Enter your guess: "))
            if guess_num < 1 or guess_num > limit:
                print(f"Please enter a number between 1 and {limit}.")
                continue
        except ValueError:
            print("Invalid input! Enter an integer.")
            continue

        attempts += 1
        if guess_num < random_number:
            print("Too low!")
        elif guess_num > random_number:
            print("Too high!")

    print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.\n")
    user_attempts_list.append(attempts)  # Save attempts for statistics


def computer_guess(limit):
    '''Computer tries to guess the user's number using binary search.'''
    print(f"\nThink of a number between 1 and {limit}. I will try to guess it.")
    low = 1
    high = limit
    attempts = 0
    feedback = ''

    while feedback != 'c' and low <= high:
        guess_num = (low + high) // 2
        attempts += 1
        feedback = input(f"Is {guess_num} too low (l), too high (h), or correct (c)? ").lower()
        if feedback == 'l':
            low = guess_num + 1
        elif feedback == 'h':
            high = guess_num - 1
        elif feedback == 'c':
            print(f"I guessed your number {guess_num} in {attempts} attempts!\n")
            computer_attempts_list.append(attempts)  # Save attempts for statistics
        else:
            print("Invalid input! Please type 'l', 'h', or 'c'.")


def show_statistics():
    '''Show statistics for user and computer games.'''
    if user_attempts_list:
        print(f"Your fastest guess: {min(user_attempts_list)} attempts")
        print(f"Your average attempts: {sum(user_attempts_list)/len(user_attempts_list):.2f}")
    if computer_attempts_list:
        print(f"Computer's fastest guess: {min(computer_attempts_list)} attempts")
        print(f"Computer's average attempts: {sum(computer_attempts_list)/len(computer_attempts_list):.2f}")
    print()


def main_menu():
    """Main menu loop for the game."""
    while True:
        print("\n===== Number Guessing Game =====")
        print("1 --> You Guess the Number")
        print("2 --> Computer Guesses Your Number")
        print("3 --> Show Statistics")
        print("0 --> Exit")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input! Enter 0, 1, 2, or 3.")
            continue

        if option == 0:
            print("Thanks for playing! Goodbye.")
            break
        elif option not in [1, 2, 3]:
            print("Invalid option! Enter 0, 1, 2, or 3.")
            continue

        if option == 1 or option == 2:
            try:
                limit = int(input("Enter the maximum number to guess: "))
                if limit < 1:
                    print("Number must be at least 1.")
                    continue
            except ValueError:
                print("Invalid input! Enter a positive integer.")
                continue

        if option == 1:
            guess(limit)
        elif option == 2:
            computer_guess(limit)
        elif option == 3:
            show_statistics()


# Start the game
main_menu()


