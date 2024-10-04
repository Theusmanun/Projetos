print ("A - Digite A para cadastrar um novo cliente: ")
print ("B - Digite B para mostrar todos os clientes: ")
print ("C - Digite C para buscar um novo cliente: ")
print ("D - Digie D para atualizar o cadastro de cliente: ")
print ("E - Digite E para excluir um cliente: ")

opcao = str(input("Digite uma Opção"))

match (opcao):
    case 'A' : 
        print("Abrindo o cadastrador de cliente!")
    case 'B' : 
        print("Buscando todos os clientes!")
    case 'C' : 
        print ("Buscando o cliente desejado!")
    case 'D' : 
        print ("Abrindo o atualizador de cadastro!")
    case 'E' : 
        print ("Abrindo a lixeira de clientes!")
    