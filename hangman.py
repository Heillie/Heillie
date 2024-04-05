#heilliesantana
import random

def choose_word():
    word_bank = ["apple", "banana", "orange", "computer", "elephant", "giraffe", "hangman", "python", "jazz", "kangaroo", "zebra", "xylophone", "umbrella", "telephone", "watermelon", "strawberry", "quarantine", "happiness", "chocolate", "sunshine"]
    return random.choice(word_bank)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def draw_man(lives):
    stages = [
        '''
        -----
        |   |
        |   O
        |  /|\\
        |  / \\
        |
        -
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |  /
        |
        -
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |
        |
        -
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |
        |
        -
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |
        |
        -
        ''',
        '''
        -----
        |   |
        |   O
        |  /|
        |
        |
        -
        ''',
        '''
        -----
        |   |
        |   O
        |
        |
        |
        -
        ''',
        '''
        -----
        |   |
        |
        |
        |
        |
        -
        '''
    ]
    return stages[lives]

def hangman_game():
    word = choose_word()
    guessed_letters = []
    lives = 7
    win = False

    print("Welcome to Hangman!")
    print(draw_man(lives))
    print("Guess the word:")
    print(display_word(word, guessed_letters))

    while lives > 0:
        guess = input("Enter a letter or type 'exit' to quit: ").lower()

        if guess == 'exit':
            print("Thanks for playing!")
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            lives -= 1
            print("Wrong guess!")
            print(f"Remaining lives: {lives}")
            print(draw_man(lives))

        word_display = display_word(word, guessed_letters)
        print(word_display)

        if '_' not in word_display:
            win = True
            break

    if win:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, the word was '{word}'. Better luck next time!")

if __name__ == "__main__":
    hangman_game()
