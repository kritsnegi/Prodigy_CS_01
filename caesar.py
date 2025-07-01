# Caesar Cypher Encryption & Decryption Implementation

def caesar_encryption(message , shift):
    result = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26 
                elif shifted < ord('A'):
                    shifted += 26  
                result += chr(shifted)
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
                result += chr(shifted)
        else:
            result += char
    return result

def caesar_decryptin(cipher , shift):
    return caesar_encryption(cipher, -shift)


def main():
    message = input("Enter the message you want to Encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted = caesar_encryption(message , shift)
    cipher = encrypted
    decrypted = caesar_decryptin(cipher , shift)
    print("Encrypted message: ", encrypted)
    print("Decrypted message: ", decrypted)
    

if __name__ == "__main__":
    main()
