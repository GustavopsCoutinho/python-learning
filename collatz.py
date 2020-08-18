def collatz(number):
    try:
        number = int(number)
        try:
            tempor =  1 / number
            while abs(number) !=1:
                if number % 2 == 0:
                    number = number // 2
                    print(number)
                else:
                    number = 3 * number + 1
                    print(number)
        except ZeroDivisionError:
            print('O valor informado nao pode ser zero')
    except ValueError:
        print('Voce não informou um numero inteiro, tente novamente')

print('Informe um numero inteiro')
number = input()
collatz(number)