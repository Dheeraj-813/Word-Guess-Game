import random
word = ['apple','oracle','amazon','microsoft','orange','cat','dog']

# Choose the random word from the list.

guessed_word = random.choice(word)
print(guessed_word)

# For guessing the word we required the hint.

hint = guessed_word[0] + guessed_word[1]
print(hint)

# Take the letter from user and store it.

store_g_l = []

# Game provide us 6 attempt.

try_p = 6

# User input

a = input('Enter your Name :- ')
print('Welcome to the Guess word Game ', a)
print('We are going to give you 6 attempts to guess the word')

# 1st attempt

for guess in range(try_p):
    while True:
        letter = input("Guess a letter:- ")
        if len(letter) == 1:
            break
        else:
            print("Oops! Please guess the letter again")

if letter in guessed_word:
    print("Correct")
    store_g_l.append(letter)
else:
    print("Nop, letter is wrong")

if guess == 3:
    print()
    clue_request = input("Would you like clue for another word?")
    if clue_request.startswith('y'):
        print()
        print('Clue of the first and last letter of the word is :- ', hint)
    else:
        print("Your doing great job!")

print()
print('''Now let's see what have you guessed so for. you have guessed :- ''', len(store_g_l),'letters correctly')
print('These letters are:- ', store_g_l)

word_guess = input('Guess the whole word :- ')
if word_guess == guessed_word:
    print("Congrats! you are correct.")
else:
    print('Sorry! The answer was ', guessed_word)

print()
input('Please press enter to leave the game.')
