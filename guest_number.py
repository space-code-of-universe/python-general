trying = 0
secret_number = 7
limit = 3

while trying < limit:
    guest_number = input('Input number (1-9) ')
    guest_number = int(guest_number)

    if guest_number == secret_number:
        print('Congratulation, you are right')
        break
    trying += 1