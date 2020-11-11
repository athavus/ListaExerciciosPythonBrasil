n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
if n1 > n2:
    print(f'O maior valor entre {n1} e {n2} é {n1}!')
elif n2 > n1:
    print(f'O maior valor entre {n1} e {n2} é {n2}!')
else:
    print(f'{n1} e {n2} são valores iguais!')
