def collatz(number):
    if number % 2 == 0:
        print(str(number) + ' // 2 = ' + str(number // 2))
    else:
        print('3 * ' + str(number) + ' + 1 = ' + str((3*number)+1))

try:
    number = int(input())
    collatz(number)
except ValueError:
    print('enter an integer number, float not allowed')