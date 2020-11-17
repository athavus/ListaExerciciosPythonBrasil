numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

maior = numero_1
menor = numero_1

if maior < numero_2:
    maior = numero_2
if menor > numero_2:
    menor = numero_2
if maior < numero_3:
    maior = numero_3
if menor > numero_3:
    menor = numero_3

print(f'O maior número digitado foi {maior} e o menor foi {menor}')
