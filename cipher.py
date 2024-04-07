def caesar_cipher(text, shift):
    alphabet = {'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm',
                'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u',
                'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c',
                'y': 'd', 'z': 'e'}

    encrypted_text = ""
    for char in text:
        encrypted_text += alphabet.get(char, char)
    return encrypted_text

text = "python is fun!"
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Original:", text)
print("Encrypted:", encrypted_text)
