import random

no01 = input('Digite um nome: ')
no02 = input('Digite um nome: ')
no03 = input('Digite um nome: ')
no04 = input('Digite um nome: ')
no05 = input('Digite um nome: ')
lista = [no01, no02, no03, no04, no05]
random.shuffle(lista)
print(lista)