elem = int(input('Digite quantos elementos quer ver: '))
cont = 0
num1 = 1
num2 = 0
num3 = 0
while cont < elem:
    print(num1+num3, end='-> ')
    num2 = num1
    num1 = num3
    num3 = num1 + num2
    cont +=1
