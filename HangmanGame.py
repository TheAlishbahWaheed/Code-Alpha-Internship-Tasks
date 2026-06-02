import random
words = ["python", "computer", "hangman", "program", "gaming"]
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
hidden_word = ["_"] * len(word)
print("Welcome to Hangman Game!")
while incorrect_guesses < max_guesses and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1
if "_" not in hidden_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)