#Questão 4

def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

#Questão 5

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    else:
        return "Acima do peso"

#Questão 6

def adicionar_imposto(preco):
    imposto = preco * 0.15
    preco_final = preco + imposto
    return preco_final

print("\n1. Verificação de idade:")
print(f"20 anos: {verificar_idade(20)}")
print(f"15 anos: {verificar_idade(15)}")

print("\n2. Cálculo de IMC:")
peso = 70
altura = 1.75
imc = calcular_imc(peso, altura)
print(f"Peso: {peso}kg, Altura: {altura}m")
print(f"IMC: {imc:.2f} - {classificar_imc(imc)}")

print("\n3. Cálculo com imposto:")
preco = 100.00
preco_final = adicionar_imposto(preco)
print(f"Preço original: R$ {preco:.2f}")
print(f"Preço com imposto: R$ {preco_final:.2f}")

#Try... except
#Questão 1

try:
    numero1 = float(input("Digite o primeiro número (dividendo): "))
    numero2 = float(input("Digite o segundo número (divisor): "))
    
    resultado = numero1 / numero2
    print(f"Resultado da divisão: {resultado:.2f}")
    
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")

#Questão 2

try:
    numero = float(input("Digite um número: "))
    print(f"Você digitou o número: {numero}")
    
except ValueError:
    print("Erro: Você deve digitar um número válido!")

#Questão 3
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado:.2f}")
    
except ValueError:
    print("Erro: Você deve digitar números válidos!")
    
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

#Questão 4
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero!"