github = ""

def encode(password):
    encode_list = []
    for digit in password:
        encode_list.append(int(digit))

    for i in range(0,len(encode_list)):
        encode_list[i] = encode_list[i] + 3

    for j in range(0, len(encode_list)):
        encode_list[i] = str(encode_list[i])
    enc = "".join(encode_list)
    global github
    github = enc
    print("Your password has been encoded and stored!")
