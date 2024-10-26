def caesar_cipher(text, shift=5):
    encrypted_text = ""

    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift within uppercase letters (A-Z)
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift within lowercase letters (a-z)
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Leave special characters unchanged
            encrypted_text += char

    return encrypted_text

# Get user input
plain_text = input("Enter a sentence to encrypt: ")

# Encrypt the input text and print the result
encrypted_text = caesar_cipher(plain_text)
print("Encrypted text:", encrypted_text)

