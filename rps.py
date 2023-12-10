import random

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! 😐", 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win! 🎉", 1
    else:
        return "Computer wins! 😔", -1

def play_game(rounds):
    player_score = 0
    computer_score = 0

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice} {get_emoji(user_choice)}")
        print(f"Computer chose {computer_choice} {get_emoji(computer_choice)}")

        result, score = determine_winner(user_choice, computer_choice)
        print(result)

        player_score += score

    print(f"\n ⌛ Game over! Your score: {player_score} {get_emoji('rock')}, Computer score: {computer_score} {get_emoji('scissors')}")

def get_emoji(choice):
    emojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }
    return emojis.get(choice, '')

num_rounds = int(input("🔢 Enter the number of rounds you want to play: "))
play_game(num_rounds)
