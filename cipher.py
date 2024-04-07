def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine the base of the alphabet (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Apply the Caesar cipher shift
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Prompt the user for a plain text sentence
sentence = input("Please enter a sentence: ")

# Encrypt the sentence using Caesar cipher with a shift of 5
encrypted_sentence = caesar_cipher(sentence, 5)

# Print the encrypted sentence
print("The encrypted sentence is:", encrypted_sentence)
