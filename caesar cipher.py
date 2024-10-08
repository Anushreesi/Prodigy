def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:  # decrypt
                shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def main():
    while True:
        print("\nCaesar Cipher Encryption/Decryption")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '3':
            print("Thank you for using the Caesar Cipher program. Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (1-25): "))
        
        if shift < 1 or shift > 25:
            print("Invalid shift value. Please enter a number between 1 and 25.")
            continue
        
        if choice == '1':
            result = caesar_cipher(message, shift, 'encrypt')
            print(f"Encrypted message: {result}")
        else:
            result = caesar_cipher(message, shift, 'decrypt')
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
