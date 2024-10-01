print("Calculadora IMC")

peso= float(input("Digite seu peso \n"))
altura = float(input("Digite sua altura em metros\n"))

imc= peso/(altura**2)

if(imc>18.5): print("Abaixo do peso")
elif(25<=imc<24.9): print("Peso normal")
elif(25<=imc <29.9): print("Sobrepeso")
else: print("Obesidade")
