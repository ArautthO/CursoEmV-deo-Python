print('Para o cálculo do seu IMC, digite suas medidas: ')
alt = float(input('Digite qual a sua Altura: '))
peso = float(input('Digite qual o seu peso: '))
imc = peso/(alt*alt)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do seu peso ideal!'.format(imc))
elif imc < 25:
    print('Parabéns! seu IMC é {:.2f} e você está em seu peso ideal!'.format(imc))
elif imc < 30:
    print('Cuidado! Seu IMC é {:.2f} e você está com sobrepeso!'.format(imc))
elif imc < 40:
    print('Alerta! Seu IMC é {:.2f} e você está com obesidade!'.format(imc))
else:
    print('Perigo! Seu IMC é {:.2f} e você está com obesidade mórbida!'.format(imc))