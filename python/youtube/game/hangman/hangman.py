import random

hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  0 |
    |
    ===""", """
+---+
  | |
  0 |
 /| |
    ===""", """
+---+
  | |
  0 |
 /|\|
    ===""", """
+---+
  | |
  0 |
 /|\|
  |  ===""","""
 /  
""", """
+---+
  | |
  0 |
 /|\|
  |  ===""","""
 / \  
""",
]

animals = ['tiger', 'lion', 'giraffe', 'zebra', 'dolphin', 'shark', 'elephant', 'rhino']

word = random.choice(animals).lower()

guessed_correctly = []
guessed_incorrectly = []
tries = 6
hangman_count = -1

while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += '_ '
    if output == word:
        break

    print("Gues the word: ", output)
    print(tries, " chances left")

    guess = input().lower()
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already, guessed.", guess)
    elif guess in word:
        print("Congrats!!", guess)
    else:
        print("Sorry, you guessed wrong!")
        hangman_count += 1
        tries -= 1
        guessed_incorrectly.append(guess)
        print(hangman1[hangman_count])

if tries > 0:
    print("you guessed the word and you won")
else:
    print("Sorry there, you lost the game. Try again :-)")
