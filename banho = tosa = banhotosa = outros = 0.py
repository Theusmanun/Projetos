banho = tosa = banhotosa = outros = 0
def menu ():
    print ("1 - Banho")
    print ("2 - Tosa")
    print ("3 - Banho e tosa")
    print ("4 - Outros")
    global op
    op = int(input("Informe a opção desejada!"))
   
for i in range (5):
    menu()
    match (op):
        case 1:
            banho+=1
        case 2:
            tosa+=1
        case 3:
            banhotosa+=1
        case 4:
            outros+=1
print ("Quantidade: ")
print ("Banho: ", banho)
print ("Tosa: ", tosa)
print ("Banho e tosa: ", banhotosa)
print ("Outros: ", outros)

