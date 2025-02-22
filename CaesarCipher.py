#CeasarCipher.py
#Name: Jacob Oetken
#Date: 2/22/2025
#Assignment: LAB 5

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #letter is letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: #letter is not letter
            secret = secret + letter

    return secret

def decode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    decoded_message = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #letter is letter
            spot = (alpha.find(letter) - key) % 26
            decoded_message = decoded_message + alpha[spot]
        else: #letter is not letter
            decoded_message = decoded_message + letter

    return decoded_message




def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    secret = encode(message, key)
    print("Encrypted:", secret)
    
    decode_response = input("Do you want to decode the message? (Y/N): ").strip().lower() 
    if decode_response == 'y':
        plaintext = decode(secret, key)
        print("Decrypted:", plaintext)
    else:
        print("Decoding skipped.")

if __name__ == '__main__':
    main()
