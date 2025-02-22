#Word Game is a knock-off version of a popular online word-guessing game.
#Name: Jacob Oetken
#Date: 2/22/2025
#Assignment: LAB 5

#PLEASE SEE BELOW THE MAIN CODE. NOTICED SOMETHING INTERESTING!

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    result = ""
    for i in range(len(myGuess)):
        if inSpot(myGuess[i], word, i):
            result += myGuess[i].upper()
        elif inWord(myGuess[i], word):
            result += myGuess[i].lower()
        else:
            result += "#"
    return result

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    theWord = random.choice(wordList).strip()
    
    #User should get 6 guesses to guess
    attempts = 6

    print("Guess the 5-letter word!")

    while attempts > 0:
        #Ask user for their guess
        while True:
            myGuess = input("Enter your guess: ").strip().lower()
            # Check if the guess is a 5-letter word
            if len(myGuess) == 5:
                break
            print("Please enter a 5-letter word.")

        #Give feedback using on their word
        feedback = rateGuess(myGuess, theWord)
        print("Feedback:", feedback)

        if myGuess == theWord:
            print("Congratulations! You've guessed the word correctly.")
            break

        attempts -= 1
        print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was: {theWord}")

if __name__ == '__main__':
    main()

#above is the original code that i wrote, however when i had my wife play it i noticed that the code would say something like #AlaE where its     "#" unknown/wrong letter | A | L wrong spot | A wrong spot | E     if the word was SCALE. 
#meaning if i had a correct letter, but in the wrong spot, and the correct letter in the right spot, it was still telling me that there was another of that letter. (if that makes sense)
#i sent what i had off to my buddy who is *only slightly* (or a lot) smarter than me with programming, and what is below is what he sent me back and what we came up with, which doesnt have that problem, but isnt my work and i am not 100% sure what/how he did it.
#is there a way for you to kind of describe what he did in more detail? maybe zoom or something?!

# import random

# def inWord(letter, word):
#     """Returns boolean if letter is anywhere in the given word"""
#     return letter in word

# def inSpot(letter, word, spot):
#     """Returns boolean response if letter is in the given spot in the word."""
#     return word[spot] == letter

# def rateGuess(myGuess, word):
#     """Rates your guess and returns a word with the following features.
#     - Capital letter if the letter is in the right spot
#     - Lower case letter if the letter is in the word but in the wrong spot
#     - * if the letter is not in the word at all"""
#     result = ["*"] * len(myGuess)
#     word_list = list(word)

#     # First pass: mark correct letters in the correct spot
#     for i in range(len(myGuess)):
#         if inSpot(myGuess[i], word, i):
#             result[i] = myGuess[i].upper()
#             word_list[i] = None  # Mark this letter as used

#     # Second pass: mark correct letters in the wrong spot
#     for i in range(len(myGuess)):
#         if result[i] == "*" and myGuess[i] in word_list:
#             result[i] = myGuess[i].lower()
#             word_list[word_list.index(myGuess[i])] = None  # Mark this letter as used

#     return "".join(result)

# def main():
#     #Pick a random word from the list of all words
#     wordFile = open("words.txt", 'r')
#     content = wordFile.read()
#     wordList = content.split("\n")
#     theWord = random.choice(wordList).strip()
    
#     #User should get 6 guesses to guess
#     attempts = 6

#     print("Guess the 5-letter word!")

#     while attempts > 0:
#         #Ask user for their guess
#         while True:
#             myGuess = input("Enter your guess: ").strip().lower()
#             # Check if the guess is a 5-letter word
#             if len(myGuess) == 5:
#                 break
#             print("Please enter a 5-letter word.")

#         #Give feedback using on their word
#         feedback = rateGuess(myGuess, theWord)
#         print("Feedback:", feedback)

#         if myGuess == theWord:
#             print("Congratulations! You've guessed the word correctly.")
#             break

#         attempts -= 1
#         print(f"You have {attempts} attempts left.")

#     if attempts == 0:
#         print(f"Sorry, you've run out of attempts. The word was: {theWord}")

# if __name__ == '__main__':
#     main()
