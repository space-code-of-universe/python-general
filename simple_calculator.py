# Practice

numb_1 = float(input('Input your first number ! '))
operator = input('Insert +, -, *, / ')
numb_2 = float(input('Input your second number ! '))
if operator=='+':
    result = numb_1 + numb_2
    print(f'The result is {result}')

elif operator=='-':
    result = numb_1 - numb_2
    print(f'The result is {result}')

elif operator =='*' or 'x':
    result = numb_1 * numb_2
    print(f'The result is {result}')

elif operator=='/':
    result = numb_1 / numb_2
    print(f'The result is {result}')

else:
    print('Please input the correct number')

print('Thank you')





