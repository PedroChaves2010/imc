import os
os.system("cls")

print("Seja Bem-vindo a calculadora de imc")

nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 25:
    print("Você está com sobrepreso")
    print(imc)
elif imc < 30:
    print("Você está com obesidade grau I")
    print(imc)
elif imc < 35:
    print ("Você está com obesidade grau II")
    print(imc)
elif imc < 40:
    print("Você está com obesidade morbida")
    print(imc)
else:
    print("Você está saudavel")
    print(imc)
