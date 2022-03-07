
def main():
    code = ['41', '42', '43', '44', '45', '46', '47', '48', '49', '4A', '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A']
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    hex_code = ''
    printout = []
    phrase = input('please input a phrase to be translated')
    for letter in phrase:
        for character in range(0, len(alphabet)):
            if letter.upper() == alphabet[character]:
                printout.append(code[character])
                hex_code += code[character]
    print(hex_code)
    print(printout)

    hex_file = open('hex_file.txt', 'w')
    for line in printout:
        lineout = line, "\n"
        hex_file.writelines(lineout)
    hex_file.close()


main()
