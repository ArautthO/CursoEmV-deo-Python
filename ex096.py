def área(lar, comp):
    tot = lar * comp
    print(f'A area de um terreno {lar}m x {comp}m é de {tot}m².')

# Programa principal
l = float(input('Digite a Largura do terreno em metros: '))
c = float(input('Digite o comprimento do terreno em metros: '))
área(l, c)
