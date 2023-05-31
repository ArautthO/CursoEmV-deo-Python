def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mERRO! Entrada de dados interronpida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mERRO! Usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n


#Programa Principal
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {n1} eo número {n2}.')