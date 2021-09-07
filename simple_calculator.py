# Practice

numb_1 = float(input('Input your first number ! '))
operator = input('Insert +, -, *, / ')
numb_2 = float(input('Input your second number ! '))
if operator=='+':
    print(f'Hasilnya adalah {numb_1 + numb_2}')
elif operator=='-':
    print(f'Hasilnya adalah {numb_1 - numb_2}')
elif operator =='*' or 'x':
    print(f'Hasilnya adalah {numb_1 * numb_2}')
elif operator=='/':
    print(f'Hasilnya adalah {numb_1 / numb_2}')
print('Thank you')



