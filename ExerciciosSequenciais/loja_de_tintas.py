area = float(input('Digite o valor em metros quadrados a área a ser pintada: '))
tinta = area / 3
lata = tinta / 18
preco = lata * 80
print(f'Serão necessárias para pintar essa área, {lata:.1f} latas de tinta')
print(f'O preço total a pagar é R${preco:.2f}')
