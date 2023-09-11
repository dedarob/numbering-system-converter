print('-=-'*20)
print('Conversor de bases')
print('-=-'*20)
numero = int(input('Digite um número: '))
base = int(input('Qual será a conversão?\n1 para binário\n2 para hexadecimal\n3 para octal\nDigite Aqui: '))
originalNum = numero
if base == 1:
    listaBina = []
    while numero != 1:
        resultBina = numero % 2
        numero = numero // 2
        listaBina.append(resultBina)
        if numero == 1:
            listaBina.append(1)
    listaBina.reverse()
    listaBina = ''.join(map(str, listaBina))
    print('O número {} em binário é: {}'.format(originalNum, listaBina))
elif base == 2:
    listaHexa = []
    if numero <=15:
        listaHexa.append(numero)
    else:
        while numero >= 16:
            resultHexa = numero % 16
            numero = numero // 16
            listaHexa.append(resultHexa)
            if numero < 16:
                listaHexa.append(numero)
    listaHexa.reverse()
    stringHexa = [str(x) for x in listaHexa]
    stringHexa = ''.join(stringHexa)
    print('O número {} em Hexadecimal é : {}'.format(originalNum, stringHexa))
elif base ==3:
    listaOct = []
    if numero <=7:
        listaOct.append(numero)
    else:
        while numero >= 8:
            resultOct = numero % 8
            numero = numero // 8
            listaOct.append(resultOct)
            if numero < 8:
                listaOct.append(numero)
    listaOct.reverse()
    stringOct = [str(x) for x in listaOct]
    stringOct = ''.join(stringOct)
    print ('O número {} em Octal é : {}'.format(originalNum, stringOct))