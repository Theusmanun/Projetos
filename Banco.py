while True:
    valorcasa = float(input("Quanto custa a casa que voce deseja comprar?"))
    salario = float(input("Quanto é o seu salario?"))
    paganos = int(input("Em quantos anos voce deseja pagar a casa?"))
    prestacaomensal = valorcasa/(paganos * 12)
    salariotrinta = salario * 0.3
    
    if prestacaomensal < salariotrinta:
        print (" Não é possivel realizar o emprestimo!")
    else:
        print ("O emprestimo foi encaminhado!")
    continuar = str(input("Quer realizar uma nova simulação? (Sim/Não)"))
    if continuar == "Sim":
        continue
    elif continuar == "Não":
        print ("Programa encerrado!")
        break



    
