#Crie um programa que receba dois números inteiros do usuário. O programa deve calcular e exibir a soma desses números e,
#  em seguida, verificar se o resultado é par ou ímpar. Exiba uma mensagem apropriada indicando a paridade.

print("Calculadora de pares")
num1= int(input("Digite um número: \n"))
num2 = int(input("Digite o segundo número \n"))

soma= num1+num2

if soma%2 ==0:print("O resultado da soma entre ", num1, " e ", num2, " é par")
else: print("O resultado da soma é impar")

#solicite ao usuário o valor de um produto e a porcentagem de desconto a ser aplicada. 
# O programa deve calcular o valor final do produto após aplicar o desconto e exibir o valor original, o desconto aplicado e o valor final.

print ("-------------")
print("Calculando desconto")
valorInicial = float(input("Digite o valor do produto \n"))
porcentagemDesconto = float(input("Digite a porcentagem de desconto \n"))
valorDesconto = valorInicial *(porcentagemDesconto/100)
valorFinal= valorInicial - valorDesconto
print("O valor inicial era ", valorInicial, " com o desconto de ", porcentagemDesconto, "% é igual a ", valorFinal)