#CalebNoss.
def encode():
    try:
        decoded_password = input("Please enter your password to encode: ")
        encoded_password = ""
        if len(decoded_password) == 8:
            for decoded_character in range(len(decoded_password)):
                encoded_character = (int(decoded_password[decoded_character]) + 3)
                if len(str(encoded_character)) == 2:
                    encoded_character = encoded_character - 10
                encoded_password += str(encoded_character)
            print("Your password has been encoded and stored!\n")
            return encoded_password
    finally:
        a=1


if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = input("Please enter an option: ")
        if choice == "1":
            encoded_password = encode()
        elif choice == "2":
            print(encoded_password)