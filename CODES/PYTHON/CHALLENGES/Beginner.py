# Calculadora simples: faça +, -, *, / com validação de entrada.

def Sum(a, b):
    return a + b

def Minus(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Division(a, b):
    if b == 0:
        return None
    else:
        return a / b

Choose = input("Choose A Operation *, /, +, - ")
Numb1 = float(input("Choose Number 1 "))
Numb2 = float(input("Choose Number 2 "))

if Choose == '+':
    print(Sum(Numb1, Numb2))
elif Choose == '-':
    print(Minus(Numb1, Numb2))
elif Choose == '*':
    print(Multiply(Numb1, Numb2))
elif Choose == '/':
    print(Division(Numb1, Numb2))

# Jogo de adivinhar número: o programa escolhe um número e dá dicas de “maior” ou “menor”.



# Tabuada interativa: gere a tabuada de qualquer número e permita repetir.
# Contador de vogais e consoantes: receba uma frase e mostre as quantidades.
# Verificador de palíndromo: descubra se uma palavra/frase é igual ao contrário.
# Conversor de temperatura: Celsius, Fahrenheit e Kelvin.
# Iniciante-Intermediário