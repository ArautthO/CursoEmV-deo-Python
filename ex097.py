def escreva(txt):
    tam = len(txt)+4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# Programa principal
txt = str(input('Digite uma frase: '))
escreva(txt)
