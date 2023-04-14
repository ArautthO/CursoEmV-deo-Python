num1 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num2 = int(input('Digite um número entre 0 e 20: '))
    resp = ' '
    if num2 >= 0 and num2 <= 20:
        print(f'Você Digitou {num1[num2]}!')
        while resp not in 'SsNn' :
            resp = str(input('Quer continuar? [S/N]').strip())
        if resp in 'Nn':
            break