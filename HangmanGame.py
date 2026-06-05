import random

# Word list with hints
words = {
    "python": "A popular programming language",
    "computer": "An electronic machine",
    "hangman": "The name of this game",
    "program": "A set of instructions for a computer",
    "gaming": "Playing video games"
}

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

def play_hangman():
    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6
    hidden_word = ["_"] * len(word)

    print("\n🎮 Welcome to Hangman!")
    print("💡 Hint:", hint)

    while incorrect_guesses < max_guesses and "_" in hidden_word:
        print(hangman_stages[incorrect_guesses])
        print("Word:", " ".join(hidden_word))
        print("Guessed Letters:", " ".join(sorted(guessed_letters)))
        print(f"Attempts Left: {max_guesses - incorrect_guesses}")

        guess = input("\nEnter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")

            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
        else:
            print("❌ Wrong Guess!")
            incorrect_guesses += 1

    # Game result
    if "_" not in hidden_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        score = (max_guesses - incorrect_guesses) * 10
        print("🏆 Score:", score)
    else:
        print(hangman_stages[max_guesses])
        print("\n💀 Game Over!")
        print("The word was:", word)

# Main Loop
while True:
    play_hangman()

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("👋 Thanks for playing!")
        break