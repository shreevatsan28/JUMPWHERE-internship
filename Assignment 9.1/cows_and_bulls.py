import random

def generate_secret_number():
  secret_number = ""
  while len(secret_number) < 4:
    digit = random.randint(0, 9)
    if str(digit) not in secret_number:
      secret_number += str(digit)
  return secret_number

def get_cows_and_bulls(secret_number, guess):
  cows = 0
  bulls = 0
  for i in range(len(secret_number)):
    if secret_number[i] == guess[i]:
      bulls += 1
    elif secret_number[i] in guess:
      cows += 1
  return cows, bulls

def play_game():
  secret_number = generate_secret_number()

  num_guesses = 0

  while True:
    guess = input("Enter a number: ")

    if len(guess) != 4 or not guess.isdigit():
      print("Invalid guess. Please enter a 4-digit number.")
      continue

    cows, bulls = get_cows_and_bulls(secret_number, guess)

    print(f"{cows} cows, {bulls} bulls")

    if cows == 4 and bulls == 4:
      print("Congratulations! You guessed the correct number!")
      break

    num_guesses += 1

  print(f"You made {num_guesses} guesses.")

if __name__ == "__main__":
  play_game()
