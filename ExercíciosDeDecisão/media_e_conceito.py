nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))

media = (nota_1 + nota_2) / 2
print(f'Primeira nota: {nota_1:.1f}')
print(f'Segunda nota: {nota_2:.1f}')
if 9 <= media <= 10:
    print(f'Média: {media:.1f}') 
    print('Conceito A')
    print('APROVADO')
elif 7.5 <= media < 9:
    print(f'Média: {media:.1f}') 
    print('Conceito B')
    print('APROVADO')
elif 6.0 <= media < 7.5:
    print(f'Média: {media:.1f}') 
    print('Conceito C')
    print('APROVADO')
elif 4.0 <= media < 6.0:
    print(f'Média: {media:.1f}') 
    print('Conceito D')
    print('REPROVADO')
elif 0 <= media < 4.0:
    print(f'Média: {media:.1f}') 
    print('Conceito E')
    print('REPROVADO')
