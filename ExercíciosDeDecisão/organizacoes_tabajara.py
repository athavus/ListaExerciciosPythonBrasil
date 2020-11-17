salario = float(input('Digite o seu salário: '))

if salario <= 280:
    salario_novo = salario + (salario * 0.20)
    per = 20
elif 280 < salario <= 700:
    salario_novo = salario + (salario * 0.15)
    per = 15
elif 700 < salario <= 1500:
    salario_novo = salario + (salario * 0.10)
    per = 10
elif salario > 1500:
    salario_novo = salario + (salario * 0.05)
    per = 5

print(f'O salário antes do reajuste era R${salario:.2f}')
print(f'O percentual de aumento aplicado foi {per}%')
print(f'O valor do aumento foi R${(salario * (per / 100)):.2f}')
print(f'O novo salário, após o aumento é R${salario_novo:.2f}')
