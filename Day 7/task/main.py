import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
lives = 6

# Create a list of underscores for the hidden word
display = ["_"] * len(chosen_word)
correct_letters = []

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue

    # Check if guess is correct
    if guess in chosen_word:
        correct_letters.append(guess)
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

    print("Word to guess: " + " ".join(display))
    print(stages[lives])  # Show the Hangman stages

    # Win condition
    if "_" not in display:
        game_over = True
        print("🎉 You win! 🎉")

    # Lose condition
    if lives == 0:
        game_over = True
        print(f"💀 IT WAS '{chosen_word}'. YOU LOSE. 💀")
