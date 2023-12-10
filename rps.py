import json
import random

def load_language(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_user_choice(language_data):
    user_choice = input(language_data["choose"]).lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print(language_data["invalid_choice"])
        user_choice = input(language_data["choose"]).lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice, language_data):
    if user_choice == computer_choice:
        return language_data["tie"], 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return language_data["you_win"], 1
    else:
        return language_data["computer_wins"], -1

def play_game(rounds, language_data):
    player_score = 0
    computer_score = 0

    for _ in range(rounds):
        user_choice = get_user_choice(language_data)
        computer_choice = get_computer_choice()

        print(f"\nYou chose {get_emoji(user_choice)} {user_choice}")
        print(f"Computer chose {get_emoji(computer_choice)} {computer_choice}")

        result, score = determine_winner(user_choice, computer_choice, language_data)
        print(result)

        player_score += score

    print(language_data["game_over"].format(
        player_score=player_score,
        computer_score=computer_score,
        rock_emoji=get_emoji('rock'),
        scissors_emoji=get_emoji('scissors')
    ))

def get_emoji(choice):
    emojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }
    return emojis.get(choice, '')

# Get the language choice from the user
language = input("🌐 Choose a language (en/cz): ").lower()

if language not in ['en', 'cz']:
    print("❌ Invalid language choice. Defaulting to English.")
    language = 'en'

# Load language data
language_data = load_language(f'lang/{language}.json')

# Get the number of rounds from the player
num_rounds = int(input(language_data["rounds_prompt"]))
play_game(num_rounds, language_data)
