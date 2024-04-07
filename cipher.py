def caesar_cipher(text):
    """
    Encrypts a message using the Caesar cipher method with a right shift of 5.

    Parameters:
    - text (str): The input text to be encrypted.
    
    Returns:
    - str: The encrypted message.
    """
    result = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 5
    
    for char in text:
        if char.lower() in alphabet:
            position = alphabet.find(char.lower())
            new_position = (position + shift) % 26
            encrypted_char = alphabet[new_position]
            if char.upper() in alphabet:
                encrypted_char = encrypted_char.upper()
            
            result += encrypted_char
        else:
            result += char
    
    return result

text = input("Please enter a sentence: ")

print("The encrypted sentence is:", caesar_cipher(text))
