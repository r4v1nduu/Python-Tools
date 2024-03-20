def encrypt(plaintext, key):
    ciphertext = ""

    # For loop to check characters one by one in the text
    for char in plaintext:

        # Check whether the characters are alphabetical
        if char.isalpha():

            # Identifying capital and simple letters to calculate ASCII Offset
            ascii_offset = 65 if char.isupper() else 97

            # ord - returns the Unicode code from a given character
            # chr - returns a string representing a character and a Unicode code integer
            # %26 ensures that the result wraps around within the range of the alphabet (26 characters)
            encrypted_char = chr(  (ord(char)-ascii_offset+key)%26   + ascii_offset)
            ciphertext += encrypted_char

        # If characters are not alphabetical, they remain the same
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)


choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\nEnter 1 or 2: ")

if choice == '1':
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the key: "))
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

elif choice == '2':
    ciphertext = input("Enter the ciphertext: ")
    key = int(input("Enter the key: "))
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)

else:
    print("Invalid choice.")
