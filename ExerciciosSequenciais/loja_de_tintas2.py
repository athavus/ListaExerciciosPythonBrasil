area = float(input('Digite o valor em metros quadrados a área a ser pintada: '))
tinta = area / 6
lata = tinta / 18
galao = tinta / 3.6
preco_galao = galao * 25
preco_lata = lata * 80
print(f'Serão necessárias para pintar essa área em latas de tinta {lata:.1f} latas')
print(f'Serão necessárias para pintar essa área em galões de tinta {galao:.1f} galões')
print(f'O preço total a pagar em latas é R${preco_lata:.2f}')
print(f'O preço total a pagar em galões de tinta é R${preco_galao:.2f}')
