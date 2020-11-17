hora = int(input('Quantas horas você trabalha por mês: '))
valor_hora = float(input('Quanto você ganha por hora: '))

salario_bruto = valor_hora * hora

if salario_bruto <= 900:
    per = 0
    imposto_renda = salario_bruto * 0.00
elif 900 < salario_bruto <= 1500:
    per = 5
    imposto_renda = salario_bruto * 0.05
elif 1500 < salario_bruto <= 2500:
    per = 10
    imposto_renda = salario_bruto * 0.10
elif salario_bruto > 2500:
    per = 20
    imposto_renda = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
total_descontos = imposto_renda + inss
salario_liquido = salario_bruto - total_descontos

print(f'Salário Bruto: ({valor_hora} * {hora})                  : R$ {salario_bruto:.2f}')
print(f'(-) IR ({per}%)                                 : R$ {imposto_renda:.2f}')
print(f'(-) INSS ( 10%)                             : R$ {inss:.2f}')
print(f'FGTS (11%)                                  : R$ {fgts:.2f}')
print(f'Total de descontos                          : R$ {total_descontos:.2f}')
print(f'Salário Liquido                             : R$ {salario_liquido:.2f}')
