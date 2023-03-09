import random
from words import words

#print(words) --Gets every word in the word list

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(str.ascii_uppercase)
    used_letters = set() # what the user guessed

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
 
    elif user_letter in used_letters:
        print('You already used this letter.')
    else:
        print('Invalid character. Please try again.')



hangman()

