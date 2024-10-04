acumulador = 0
num = int(input("Informe um numero (0 - Sair)"))

while num != 0:
    if num < 0:
        print ("Erro - 00 insira um numero positivo")
    else:
        acumulador=acumulador + num
    num = int(input("Informe um numero (0 - Sair)"))
print ("A soma deu: ", acumulador)