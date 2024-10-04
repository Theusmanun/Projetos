def menu():
    print ("Codigo 1 - Bateria")
    print ("Codigo 2 - Pneu")
    print ("Codigo 3 - Filtro de oleo")
    print ("Codigo 4 - Pastilha de freio")
    print ("Codigo 5 - Opção invalida")
    opcao = int(input("Qual o codigo do produto?"))
    quantidade = int(input("Quantas peças voce quer?"))
    match (opcao):
        case 1: 
            print("O preço final deu: ", 200 * quantidade)
        case 2: 
            print("O valor final deu: ", 350 * quantidade)
        case 3:
            print("O valor final deu: ", 50 * quantidade)
        case 4:
            print("O valor final deu: ", 100 * quantidade)
        case 5:
            menu () 
opcao = int(input("Qual o codigo do produto?"))
quantidade = int(input("Quantas peças voce quer?"))
menu()
match (opcao):
    case 1: 
        print("O preço final deu: ", 200 * quantidade)
    case 2: 
        print("O valor final deu: ", 350 * quantidade)
    case 3:
        print("O valor final deu: ", 50 * quantidade)
    case 4:
        print("O valor final deu: ", 100 * quantidade)
    case 5: 
            menu( )