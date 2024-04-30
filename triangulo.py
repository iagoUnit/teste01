
def verificarNum(entrada):
    entrada = str(entrada)
    while entrada.replace('.', '').isnumeric() == False or entrada.count('.') > 1:
        print('Entrada inválida, digite somente números.')
        entrada = input('Digite uma entrada válida: ')
    return entrada

lado_01 = input('Digite o comprimento do lado 1 do triangulo: ').strip()

lado_01 = verificarNum(lado_01)

lado_02 = input('Digite o comprimento do lado 2 do triangulo: ').strip()

lado_02 = verificarNum(lado_02)

lado_03 = input('Digiete o comprimento do lado 3 do triangulo: ').strip()

lado_03 = verificarNum(lado_03)

lado_01, lado_02, lado_03 = float(lado_01), float(lado_02), float(lado_03)

if lado_01 < lado_02 + lado_03 and lado_02 < lado_01 + lado_03 and lado_03 < lado_01 + lado_02:
    print('É Triangulo', end=' ')

    if lado_01 == lado_03 == lado_02:
        print('Equilátero.')
    elif lado_01 == lado_02 or lado_02 == lado_03 or lado_01 == lado_03:
        print('Isósceles.')
    else:
        print('Escaleno.')
