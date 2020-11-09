sexo = input("Informe o seu sexo (M para masculino ou F para feminino: ")
altura = float(input("Informe a sua altura em metros: "))
if (sexo != "M") and (sexo != "F"):
  print("Sexo inválido, tente novamente, M para masculino ou F para feminino")
if sexo == "M":
  pesoideal = (72.7 * altura) - 58
else:
  pesoideal = (62.1 * altura) - 44.7
print("O seu peso ideal é:", pesoideal, "quilos")
