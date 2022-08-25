import random

from words import word_list


def get_word():
    word = random.choice(word_list)

    return word.upper()


def check(guess, word_completion, word):
    for i in range(len(word)):
        if guess[i] == word[i]:
            word_completion = word_completion.replace("_", word[i], 1)

        elif guess[i] in word[i]:
            print(guess[i], "is in the word.")

    print(word_completion)


def play(word):
    print(word[0])
    word_completion = "_" * len(word)
    tries = 6
    guessed = False
    guessed_words = []
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(len(word))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input("Guess the word: ").upper()

        if guess in guessed_words:
            print("Invalid guess")
            print("You guessed", guessed_words, "so far")

        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                print("You got it, the word is", word)
                guessed_words.append(guess)
                guessed = True

            else:
                check(guess, word_completion, word)
                guessed_words.append(guess)
                tries -= 1
                print("You have", tries, "left")

        else:
            tries -= 1
            print("You have", tries, "left")

        print(display_hangman(tries))
        print(word_completion)
        print(tries)


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]



def main():
    word = get_word()
    play(word)
    while input("Do you want to play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


main()
