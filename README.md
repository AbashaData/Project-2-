# Simple Encryption/Decryption Tool

This project provides a simple command-line application to encrypt and decrypt messages using the Caesar cipher method. It's a beginner-friendly tool designed to help users understand the basics of encryption and decryption techniques.

## Features
1. **Encrypt Messages**:
   - Input any text to encrypt.
   - Use a user-defined shift value to encode the message.
   - Supports both uppercase and lowercase letters while keeping non-alphabet characters unchanged.

2. **Decrypt Messages**:
   - Input the encrypted message and shift value to restore the original text.

3. **User-Friendly Interface**:
   - Simple prompts for input.
   - Clear and intuitive output.

## Requirements
- Python 3.x

## How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd project-directory
   ```
3. Run the program:
   ```bash
   python encryption_tool.py
   ```

## Usage
1. The program will prompt you to input a message to encrypt.
2. Enter a shift value (integer).
3. View the encrypted message.
4. Decrypt the encrypted message by re-entering the shift value.

### Example Interaction
```bash
Welcome to the Simple Encryption/Decryption Tool!

Enter a message to encrypt: Hello World
Enter the shift value (e.g., 3): 5
Encrypted message: Mjqqt Btwqi

Decrypted message: Hello World
```

## How It Works
- The Caesar cipher shifts each letter in the input message by the specified number of positions in the alphabet.
- Non-alphabet characters (e.g., spaces, numbers, punctuation) remain unchanged.

## Limitations
- Only supports English alphabetic characters.
- Fixed shift value for encryption and decryption.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests with enhancements or bug fixes.

## Contact
If you have questions or suggestions, feel free to open an issue or contact the maintainer.
