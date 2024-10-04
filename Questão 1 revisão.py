contador = maisfilhos = menosfilhos = 0
def pergunta ():
    global filhos
    filhos = int(input("Quantos filhos voce tem?"))

for contador in range (10):
    pergunta()
    if filhos <= 2:
        menosfilhos +=1
    else:
        maisfilhos +=1

print (maisfilhos ,"mulheres tem mais de dois filhos")
print (menosfilhos," mulheres tem dois ou menos de dois filhos")
    

    