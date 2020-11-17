horario = str(input('Digite [M- Matutino, V- Vespertino, N- Noturno] ')).upper()

if horario == 'M':
    print('Bom Dia!')
elif horario == 'V':
    print('Boa Tarde!')
elif horario == 'N':
    print('Boa Noite!')
elif horario not in 'NVM':
    print('Valor Inválido!')
