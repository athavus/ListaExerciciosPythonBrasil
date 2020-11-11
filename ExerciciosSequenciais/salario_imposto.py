valor = int(input('Digite quanto você ganha por hora: '))
hora = int(input('Digite quantas horas por mês você trabalha: '))
salario = valor * hora
ir = salario * 0.11
inss = salario * 0.08
sind = salario * 0.05
descontos = sind + ir + inss
salario_liquido = salario - descontos
print(f'O salário bruto é R${salario:.2f}')
print(f'O valor a ser pago no INSS foi R${inss:.2f}')
print(f'O valor a ser pago no sindicato foi R${sind:.2f}')
print(f'O salário líquido é R${salario_liquido:.2f}')
print(f'Os descontos do salário bruto foram R${descontos} e o salário líquido foi R${salario_liquido}')
