
def main():
    code = ['20', '2E', '2C', '21', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4A',
            '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54', '55', '56', '57', '58',
            '59', '5A', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6A', '6B', '6C',
            '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A']
    alphabet = [' ', '.', ',', '!', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
                'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    hex_code = []
    phrase = input('please input a phrase to be translated')
    for letter in phrase:
        index_value = alphabet.index(letter)
        hex_code.append(code[index_value])
        '''
        hex_code += code[index_value]
        for character in range(0, len(alphabet)):
            if letter.upper() == alphabet[character]:
                printout.append(code[character])
                hex_code += code[character]
        '''
    print(hex_code)

    hex_file = open('hex_file.txt', 'w')
    for line in hex_code:
        hex_file.write(str(line) + '\n')
    hex_file.close()


main()
