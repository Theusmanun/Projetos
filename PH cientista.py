while True:
    ph = int(input("Qual o PH da amostra? (-1 para encerrar o programa)"))

    if ph >= 0 and ph < 7:
        print ("A sua substancia é acida!")
    elif ph > 7:
        print ("A sua substancia é básica!")
    elif ph == 7:
        print ("A sua substancia é neutra")
    elif ph == -1:
        print ("Programa encerrado!")
        break

