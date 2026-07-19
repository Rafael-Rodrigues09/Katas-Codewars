def create_phone_number(n):
    if len(n) != 10:
        return 'Type a number with 10 digits'
    numbers_str = ''.join(map(str, n))
    return f'({numbers_str[0:3]}) {numbers_str[3:6]}-{numbers_str[6:11]}'

#Try with some number, type a number with 10 digits
while True:
    try:
        number_input = input('Type some number: ')
        print(create_phone_number(list(map(int, number_input))))
        break
    except ValueError:
        print('Type valid numbers(integers)')
        