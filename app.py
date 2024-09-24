# Entrada de dados do usuário
print(f"Programa que calcula o seu Índice de massa corporal IMC.")
peso = float(input("Informe seu peso(kg): ").replace(",",".")) #replace troca o a vírugla por ponto se for digitado'''
altura = float(input("Informe sua altura(m): ").replace(",","."))

# calcula IMC
imc = peso / (altura **2)

# Valor IMC
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print(f"Abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print(f"Peso normal.")
elif 25 <= imc < 29.9:
    print(f"Sobre peso.")
elif 30 <= imc < 34.9:
    print(f"Obesidade Grau 1.")
elif 35 <= imc < 39.9:
    print(f"Obesidade grau 2.")
else:
    print("Obesidade grau 3.")

