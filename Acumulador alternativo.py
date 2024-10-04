acumulador = 0
while True:
    num = int(input("Informe um numero (0 - sair)"))

    if num < 0:
        print("Numero irregular!")
        continue 
    elif num == 0:
        print("Encerrando!")
        break
    acumulador=acumulador+num
print ("A soma dos numeros informador pelo usuario foi: ", acumulador)



