# (+ - * / exit)
command = ''

while command != 'exit':
    command = input('command : ')

    if command == 'exit':
        break

    if command != '+' and command != '-' and command != '*' and command != '/':
        print('command not recognized')
        continue

    a = int(input('First number : '))
    b = int(input('second number : '))

    if command == '+':
        result = a + b
    elif command == '-':
        result = a - b
    elif command == '*':
        result = a * b
    elif command == '/':
        result = a / b
    print(f'The result is {result}')

print('Thank you')
