import random

def get_computer_choice():
    choices = ['water', 'snake', 'gun']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("______Welcome to Water, Snake, Gun Game______")
    
    rounds = int(input("Enter the number of rounds you want to play: "))
    user_score = 0
    computer_score = 0
    
    for _ in range(rounds):
        print("\nMake your choice: ")
        print("1 for Water")
        print("2 for Snake")
        print("3 for Gun")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user_choice = 'water'
        elif choice == 2:
            user_choice = 'snake'
        elif choice == 3:
            user_choice = 'gun'
        else:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
    
    print("\nGame Over")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("Computer is the overall winner. Better luck next time!")
    else:
        print("The game ended in a tie.")

while True:
    play_game()
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay != 'yes':
        print("Thank you for playing! Goodbye!")
        break

