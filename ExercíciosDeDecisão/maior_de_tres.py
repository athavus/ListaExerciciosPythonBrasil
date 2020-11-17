numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

maior = numero_1

if numero_2 > maior:
    maior = numero_2
if numero_3 > maior:
    maior = numero_3
print(f'O maior dos três números é {maior}')
