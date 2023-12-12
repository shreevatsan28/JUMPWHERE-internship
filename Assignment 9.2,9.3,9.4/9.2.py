# Create a text file with words
with open("words.txt", "w") as file:
    words = ["Hands", "Legs", "India", "Crow", "Rain"]
    file.write("\n".join(words))

import random

def read_words_from_file(filename):
    # Read words from the file and store them in a list
    with open(filename, "r") as file:
        words = file.read().splitlines()
    return words

def choose_random_word(words):
    
    return random.choice(words)

def play_hangman(word):
   
    guessed_letters = set()
    max_attempts = 6
    attempts = 0
    word_to_guess = list(word.upper())
    current_display = ["_" if letter.isalpha() else letter for letter in word]
    
    print("Welcome to Hangman!")
    
    while attempts < max_attempts:
        print(" ".join(current_display))
        guess = input("Guess your letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    current_display[i] = guess
        else:
            attempts += 1
            print("Incorrect!")
            print(f"You have {max_attempts - attempts} chances left to guess.")
        
        if "_" not in current_display:
            print("Congratulations! You've guessed the word:", word)
            break
    
    if "_" in current_display:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    while True:
        words = read_words_from_file("words.txt")
        random_word = choose_random_word(words)
        play_hangman(random_word)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
