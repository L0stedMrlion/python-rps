import json
import random

def load_language(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

language = input("Choose a language (en/cz): ").lower()

if language not in ['en', 'cz']:
    print("Invalid language choice. Defaulting to English.")
    language = 'en'

language_data = load_language(f'lang/{language}.json')

def get_user_choice():
    user_choice = input(language_data["choose"]).lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print(language_data["invalid_choice"])
        user_choice = input(language_data["choose"]).lower()
    return user_choice

num_rounds = int(input(language_data["rounds_prompt"]))
play_game(num_rounds)
