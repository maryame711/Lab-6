github = ""

def encode(password):
    encode_list = []
    for digit in password:
        encode_list.append(int(digit))

    for i in range(0,len(encode_list)):
        modify_l = encode_list[i] + 3
        if modify_l >= 10:
            modify_l = modify_l - 10

        encode_list[i] = modify_l

    for j in range(0, len(encode_list)):
        encode_list[j] = str(encode_list[j])


    enc = "".join(encode_list)
    global github
    github = enc
    print("Your password has been encoded and stored!")
    return github

def menu():
    print("Menu", "\n------------- \n1. Encode \n2. Decode"
        "\n3. Quit")

def decode(password):
    decode_list =[]
    for digit in password:
        decode_list.append(int(digit))

    ranng = len(decode_list)

    for i in range(0,ranng):
        modify_l = decode_list[i] - 3
        if modify_l < 0:
            modify_l = decode_list[i] - 3 + 10

        decode_list[i] = modify_l

    for j in range(0,ranng):
        decode_list[j] = str(decode_list[j])

    decoded_pass = "".join(decode_list)
    print("The encoded password is",password, "and the original password is", decoded_pass)

def main():
    menu()
    menu_option = int(input("Please enter an option: "))

    while menu_option != 3:
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            menu()
            menu_option = int(input("Please enter an option: "))
        elif menu_option == 2:
            decode(github)
            menu()
            menu_option = int(input("Please enter an option: "))

if __name__ == '__main__':
    main()