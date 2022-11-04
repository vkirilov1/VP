num_system = input('Type the number system you want to convert the number to: ')
a = int(input('Input your number: '))

if num_system == '2':
    binary_num = str('')
    while a > 0:
        if a % 2 == 1:
            binary_num += '1'
        elif a % 2 == 0:
            binary_num += '0'
        a = a // 2

    binary_num += '0'
    binary_num = binary_num[::-1]
    print(binary_num)

elif num_system == '16':
    hex_num = str('')
    while a > 0:
        b = a % 16
        if b == 10:
            hex_num += 'A'
        elif b == 11:
            hex_num += 'B'
        elif b == 12:
            hex_num += 'C'
        elif b == 13:
            hex_num += 'D'
        elif b == 14:
            hex_num += 'E'
        elif b == 15:
            hex_num += 'F'
        else:
            hex_num += str(b)
        a = a // 16
    hex_num = hex_num[::-1]
    print(hex_num)

else:
    print('The program is still being developed, please choose between 2(binary) and 16(hex) number system!')