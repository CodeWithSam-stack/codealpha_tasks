import random

def play_hangman():
    words = ["python", "hangman", "programming", "developer", "codealpha"]
    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6
    
    print("=" * 50)
    print("Welcome to Hangman!")
    print("=" * 50)
    print(f"\nYou have {max_wrong} chances to guess wrong.\n")
    
    while wrong_guesses < max_wrong:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word}")
        print(f"Wrong guesses remaining: {max_wrong - wrong_guesses}")
        print(f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}\n")
        
        if display_word.replace(" ", "") == secret_word:
            print("🎉 Congratulations! You won!")
            print(f"The word was: {secret_word}")
            return
        
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.\n")
            continue
        
        if guess in guessed_letters:
            print("⚠️  You already guessed that letter.\n")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in secret_word:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.\n")
        else:
            print(f"✅ Correct! '{guess}' is in the word.\n")
    
    print("=" * 50)
    print(f"Game Over! You lost.\nThe word was: {secret_word}")
    print("=" * 50)

if __name__ == "__main__":
    play_hangman()