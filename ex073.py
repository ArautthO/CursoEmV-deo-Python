brasileiro = ('Grêmio', 'Coringa', 'Palmeiras', 'Sampa', 'Framerda', 'Fruminense', 'Bostafogo', 'Vasco', 'Chapecoense', 'inter', 'Bahia', 'Santos', 'Atlético', 'Crisciuma', 'Vitoria', 'Jacaré', 'Juventude', 'Cruzeiro', 'Zéquinha', 'Coritiba')
print(len(brasileiro))
print(brasileiro[:5])
print(brasileiro[-4:])
print(sorted(brasileiro))
print('A chapecoense está na posição {}ª do Campeonato!'.format(brasileiro.index('Chapecoense')+1))
for cont in range(len(brasileiro)):
    print(f'{brasileiro[cont]} na {cont+1} colocação')