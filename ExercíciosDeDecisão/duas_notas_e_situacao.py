nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))

media = (nota_1 + nota_2) / 2

if media == 10:
    print('Aprovado com Distinção')
elif media < 7:
    print('Reprovado')
elif media >= 7:
    print('Aprovado')
