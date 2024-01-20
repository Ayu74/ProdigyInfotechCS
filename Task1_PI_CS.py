def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift * (1 if encrypt else -1)) % 26 + base)
        else:
            result += char
    return result

def main():
    message = input("Enter the message: ")
    shift_value = int(input("Enter the shift value: "))
    
    encrypted_message = caesar_cipher(message, shift_value)
    print(f"\nEncrypted message: {encrypted_message}")
    
    decrypted_message = caesar_cipher(encrypted_message, shift_value, encrypt=False)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
