def maior_10(number):
    if number < 10:
        print(f'O número {number} é menor que 10.')


def resto(number):
    if number % 2 == 0:
        print(f'O número {number} é par.')


def oito_dezesseis(number):
    if number >= 8 and number <= 16:
        print(f'O número {number} está entre 8 e 16.')


def cinquenta_oitenta(number):
    if number == 51 or number == 80:
        print(f'O número {number} é 51 ou 80.')


number = int(input('Digite um número: '))

maior_10(number)
resto(number)
oito_dezesseis(number)
cinquenta_oitenta(number)