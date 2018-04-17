"""
A general rule for hangman
1. Make a word bank - 10 items --check
2. Pick an item from the list --check
3. Hide the word (use *) --check
4. Reveal the letters already guessed --check
5. Create the win condition --#NOPE
"""

import string
import random
print(string.ascii_lowercase)
word_bank = ["netflix", "chill", "popcorn", "soda", "games", "phone", "television", "playstation", "potato", "boss"]
guess_left = 10
random_word = random.choice(word_bank)
letter_selected = []
# print(random_word)
correct = list(random_word)

guess = ""
while guess != "Quite":

    output = []
    for letter in random_word:
        if letter in letter_selected:
            output.append(letter)
        else:
            output.append("*")
    print(" ".join(list(output)))
    if guess not in random_word:
        guess_left -= 1
        print(guess_left)
    if output == correct:
        print("You win!!!!")
        exit(0)
    if guess_left == 0:
        print("HA! You lose!")

    guess = input("Guess a letter:")
    letter_selected.append(guess)
    print("These are your letter %s" % letter_selected)

else:print(guess_left)

lower = guess.lower()

