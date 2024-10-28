def caesar_cipher(plain_text):
    shift = 5
    encrypted_text = ""

    for char in plain_text:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Keep non-alphabet characters unchanged

    return encrypted_text

if __name__ == "__main__":
    plain_text = input("Enter text to encrypt: ")
    # Call the function to get the encrypted text
    encrypted = caesar_cipher(plain_text)  # Ensure you assign the output here
    print(encrypted)  # Print only the encrypted text



