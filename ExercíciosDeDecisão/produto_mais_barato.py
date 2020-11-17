produto_1 = float(input('Digite o preço do primeiro produto: R$'))
produto_2 = float(input('Digite o preço do segundo produto: R$'))
produto_3 = float(input('Digite o preço do terceiro produto: R$'))

mais_barato = produto_1

if mais_barato > produto_2:
    mais_barato = produto_2
if mais_barato > produto_3:
    mais_barato = produto_3

print(f'Você deve comprar o produto com preço R${mais_barato}')
