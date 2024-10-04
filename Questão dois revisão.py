while True:
    valortotal = float(input("Quanto foi o valor total da compra?"))
    if valortotal > 100:
        valordesconto = valortotal * 0.9
        print("O valor da sua compra após o desconto ficou: R$", valordesconto)
    else:
        print ("A sua compra não recebeu nenhum desconto!")
        valordesconto == valortotal

    continuar = str(input("Deseja continuar utilizando o programa? (Sim/Não)"))
    if continuar == "Não":
            print("A sua compra deu: R$", valordesconto)
            break
            
    else:
         continue

    



