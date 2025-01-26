import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    """
    Generate a random password.

    :param length: Length of the password
    :param use_uppercase: Include uppercase letters
    :param use_numbers: Include numbers
    :param use_special: Include special characters
    :return: Randomly generated password
    """
    characters = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("No character sets selected for password generation.")

    # Generate a password by randomly sampling characters
    password = ''.join(random.choices(characters, k=length))
    return password

def encrypt_message(message, shift):
    """
    Encrypt a message using a Caesar cipher.

    :param message: The message to encrypt
    :param shift: The number of positions to shift each character
    :return: Encrypted message
    """
    encrypted = ''
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def decrypt_message(encrypted_message, shift):
    """
    Decrypt a message encrypted using a Caesar cipher.

    :param encrypted_message: The encrypted message
    :param shift: The number of positions the characters were shifted
    :return: Decrypted message
    """
    return encrypt_message(encrypted_message, -shift)

# User Interaction
def main():
    print("Welcome to the Password Generator and Encryption Tool!")

    try:
        # Password Generator
        print("\nPassword Generator")
        length = int(input("Enter the desired password length (e.g., 12): "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"\nYour generated password is: {password}")

        # Encryption/Decryption Tool
        print("\nEncryption/Decryption Tool")
        message = input("Enter a message to encrypt: ")
        shift = int(input("Enter the shift value (e.g., 3): "))

        encrypted_message = encrypt_message(message, shift)
        print(f"Encrypted message: {encrypted_message}")

        decrypted_message = decrypt_message(encrypted_message, shift)
        print(f"Decrypted message: {decrypted_message}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
