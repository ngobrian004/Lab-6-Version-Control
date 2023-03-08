# Brian Ngo

def encode(password):
    conversion_table = {"0": "3", "1": "4", "2": "5", "3": "6", "4": "7", "5": "8", "6": "9", "7": "0", "8": "1", "9": "2",}
    new_password = ""
    for i in password:
        new_password += conversion_table[i]
    return new_password

def decode(password):
    conversion_table = {'3': '0', '4': '1', '5': '2', '6': '3', '7': '4', '8': '5', '9': '6', '0': '7', '1': '8', '2': '9'}
    original_password = ''
    for i in password:
        original_password += conversion_table[i]
    return original_password

if __name__ == "__main__":
    loop = True
    while loop:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode(original_password)
            print("Your password has been encoded and stored!")
            print()
        if option == 2:
            original_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            print()
        if option == 3:
            exit()
