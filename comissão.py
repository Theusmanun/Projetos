vendastotais = float(input("Qual o valor de vendas realizadas por você?"))
salariofixo = float(input("Qual o seu salario fixo?"))
comissaofixa = float(input("Qual a sua comissão?"))

comissaofinal = comissaofixa / 100

print ("Seu salario é de: ", (vendastotais * comissaofinal) + salariofixo)