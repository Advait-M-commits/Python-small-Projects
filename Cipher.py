print('''
__        __   _                            _____     
\ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ |
  \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/

  ____ ___ ____  _   _ _____ ____
 / ___|_ _|  _ \| | | | ____|  _ \|
| |    | || |_) | |_| |  _| | |_) |
| |___ | ||  __/|  _  | |___|  _ <
 \____|___|_|   |_| |_|_____|_| \_|

 ''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(og_txt, shift_amount):
    cipher_txt = ""
    for letter in og_txt:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_txt += alphabet[shifted_position]
        else:
            cipher_txt += letter
    print(f"The encoded text is: {cipher_txt}")

def decrypt(og_txt, shift_amount):
    cipher_txt = ""
    for letter in og_txt:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            cipher_txt += alphabet[shifted_position]
        else:
            cipher_txt += letter   
    print(f"The decoded text is: {cipher_txt}")

user_input = "yes"

while user_input == "yes":
    direction = input("Enter 'encode' to encrypt or 'decode' to decrypt: ")
    text = input("Enter the text:\n").lower()
    shift = int(input("Enter the shift number:\n"))

    if direction == 'encode':
        encrypt(og_txt=text, shift_amount=shift)
    elif direction == 'decode':
        decrypt(og_txt=text, shift_amount=shift)
    else:
        print("Enter a valid operation!")

    user_input = input("Do you want to continue? 'Yes' or 'No'? ").lower()

print("Thank You, see you later")

