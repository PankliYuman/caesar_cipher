eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Welcome to Caesar Cipher Program")
text = input("Enter your text")
new_text = ""
while True:
    try:
        number_of_position = int(input("Specify how many positions each letter should shift to the right (e.g., 5) or"
                                       " to the left (e.g., -2) in the Caesar cipher."))
        break
    except ValueError:
        print("Please enter a number")

for i in range(len(text)):
    if text[i] in eng_lower_alphabet:
        new_text += eng_lower_alphabet[eng_lower_alphabet.find(text[i]) + number_of_position]
        continue
    elif text[i] in eng_upper_alphabet:
        new_text += eng_upper_alphabet[eng_upper_alphabet.find(text[i]) + number_of_position]
        continue
    else:
        new_text += text[i]

print(new_text)
