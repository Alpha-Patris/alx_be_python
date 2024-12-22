import random

def play_game():
    # Generate a secret number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Get user's guess
    guess = int(input("Guess a number between 1 and 10: "))
    
    # Match case to compare the user's guess with the secret number
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

# Main loop to allow replaying the game
while True:
    play_game()
    
    # Offer to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing! Goodbye!")
        break
        