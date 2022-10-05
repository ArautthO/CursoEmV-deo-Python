frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
print(frase)
"""inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]"""
print(junto, inverso)
if junto == inverso:
        print('Essa Frase é Palídromo!')
else:
        print('Essa Frase não é palíndromo!')
