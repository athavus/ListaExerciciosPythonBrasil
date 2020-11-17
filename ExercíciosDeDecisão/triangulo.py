x = float(input("Digite o valor da medida do primeiro lado: "))
y = float(input("Digite o valor da medida do segundo lado: "))
z = float(input("Digite o valor da medida do terceiro lado: "))
if (x > (y + z)) or (z > (x + y)) or (y > (x + z)):
    print("Estes lados não podem formar um triângulo")
else:
    print("Estes lados podem formar um triângulo")
    if (x == y) and (x == z):
        print("Este é um triângulo equilátero!")
    elif (x != y) and (x != z) and (y != z):
        print("Este é um triângulo escaleno!")	
    else:
        print("Este é um triângulo isósceles!")