arquivo = float(input('Digite o tamanho do arquivo para download em MB: '))
link = float(input('Digite a velocidade do link da internet em Mbps: '))
tempo = (arquivo / link) / 60
print(f'O tempo em minutos para se gastar no download é {tempo:.2f} minutos')
