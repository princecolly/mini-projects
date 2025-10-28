# Py Hangman

import random
import json

## Definitions
# Our Dictionary
with open("words_dictionary.json", "r") as dictionary_file:
    dictionary = json.load(dictionary_file)

words = tuple([w for w in dictionary.keys() if w.isalpha() and len(w) > 2])

toxic_lines = [
    "Do you even *know* the alphabet?",
    "This is why the rope is the hero of this story.",
    "My disappointment is a national resource.",
    "You type like you fail forward.",
    "Even the wrong letters are embarrassed to be guessed by you."
]

puppy_lines = [
    "Oops… That letter tried its best 😔",
    "It’s okay… mistakes make us beautiful 🥺",
    "I believe you! Please believe in me too!",
    "If I swing… tell my family… I love them 🐾",
    "You're doing great!… I think… 😣"
]

auntie_lines = [
    "This intelligence… you bought on credit?",
    "Is this how you guessed your KCPE answers? Shame!",
    "Letters are many. You choose nonsense.",
    "Even that boda boda guy knows the word already.",
    "You will guess right next time… if God helps you."
]

villain_lines = [
    "One more mistake… and I rise again.",
    "The rope only delays my vengeance.",
    "I am taking notes on who to haunt first.",
    "Keep guessing wrong. My power grows.",
    "When the last limb drops… you drop next."
]

personalities = {
    "1": puppy_lines,
    "2": auntie_lines,
    "3": villain_lines,
    "4": toxic_lines
}

hangman_art = {
    0: (
        "+---+-  ",
        "|   |   ",
        "|       ",
        "|       ",
        "|       ",
        "|       ",
        "========"
    ),
    1: (
        "+---+-  ",
        "|   |   ",
        "|   O   ",
        "|       ",
        "|       ",
        "|       ",
        "========"
    ),
    2: (
        "+---+-  ",
        "|   |   ",
        "|   O   ",
        "|   |   ",
        "|       ",
        "|       ",
        "========"
    ),
    3: (
        "+---+-  ",
        "|   |   ",
        "|   O   ",
        "|  /|   ",
        "|       ",
        "|       ",
        "========"
    ),
    4: (
        "+---+-  ",
        "|   |   ",
        "|   O   ",
        "|  /|\\ ",
        "|       ",
        "|       ",
        "========"
    ),
    5: (
        "+---+-  ",
        "|   |   ",
        "|   O   ",
        "|  /|\\ ",
        "|  /    ",
        "|       ",
        "========"
    ),
    6: (
        "+---+-  ",
        "|   |   ",
        "|   O   ",
        "|  /|\\ ",
        "|  / \\ ",
        "|       ",
        "========"
    )

}

def display_hangman(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def choose_personality():
    while True:
        print("Choose personality: 1 / 2 / 3 / 4")
        p = input("->: ")
        if p in personalities:
            return p
        print("Invalid choise, my friend.")

def play_game(selected_personality, scoreboard):
    max_mistakes = len(hangman_art) - 1
    answer = random.choice(words)
    
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        display_hangman(wrong_guesses)
        display_hint(hint)
        print(f"\nMistakes: {wrong_guesses}/{max_mistakes}")
        print(f"Guessed: {', '.join(sorted(guessed_letters))}\n")

        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"\n{guess} is already guessed\n")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, ch in enumerate(answer):
                if ch == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            if wrong_guesses < max_mistakes:
                print(random.choice(personalities[selected_personality]))

        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("\nYOU WIN! 🎉\n")
            scoreboard["Wins"] += 1
            break

        if wrong_guesses >= max_mistakes:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("GAME OVER 💔")
            scoreboard["Losses"] += 1
            break

def main():
    scoreboard = {"Wins": 0, "Losses": 0}

    print("\n******          🚨 Welcome to HANGMAN 2.0 🚨          ******")
    print("Multiverse of Sarcasm, Trauma, and Questionable Life Choices")
    print("*************************************************************\n")

    while True:
        selected_personality = choose_personality()
        play_game(selected_personality,scoreboard)

        print(f"\nScoreboard ➜ Wins: {scoreboard['Wins']} | Losses: {scoreboard['Losses']}")

        if not input("\nWant another round? (y/n): ").lower() == 'y'.lower():
            print("\nThanks for playing! 👋")
            print(f"\nFinal Score ➜ Wins: {scoreboard['Wins']} | Losses: {scoreboard['Losses']}")
            break

if __name__ == '__main__':
    main()
