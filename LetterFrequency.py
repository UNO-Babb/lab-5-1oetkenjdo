#LetterFrequency.py
#Name: Jacob Oetken
#Date: 2/22/2025
#Assignment: LAB 5

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #loop through each letter in message
    for letter in message:
        if (alpha.find(letter) >= 0): #letter is letter
            spot = alpha.find(letter)
            freq[spot] = freq[spot] + 1 #frequency of letter go up 1 if exists
        else: #letter is not letter
            pass

    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    output = ""
    for i in range(26):
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main():
    msg = input("Enter a message: ")
    countLetters(msg)



if __name__ == '__main__':
  main()
