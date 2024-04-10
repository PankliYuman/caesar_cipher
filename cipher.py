eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Welcome to Caesar Cipher Program")
text = input("Enter your text: ")
new_text = ""


def shift_char(char, shift, alphabet):
    if char in alphabet:
        new_index = (alphabet.index(char) + shift) % len(alphabet)
        return alphabet[new_index]
    return char


while True:
    try:
        number_of_position = int(input("Specify how many positions each letter should shift to the right (e.g., 5) or"
                                       " to the left (e.g., -2) in the Caesar cipher: "))
        break
    except ValueError:
        print("Please enter a valid number.")

for char in text:
    if char.islower():
        new_text += shift_char(char, number_of_position, eng_lower_alphabet)
    elif char.isupper():
        new_text += shift_char(char, number_of_position, eng_upper_alphabet)
    else:
        new_text += char

print("Ciphered text:", new_text)
