"""Booleanos, representam valores de verdadeiro ou falso, True ou False
int, numeros inteiros 1 2 3 4...
float, numeros quebrados 1.5 2.5 3.5...
string, textos 'oshdahesfhbsh'..."""

idade = int(input("Diga sua idade:"))
print(f"Você tem {idade} anos")
while idade < 0:
    print(f"Idade inválida, digite novamente!")
    idade = int(input("Diga sua idade:"))
if idade >=18:
    print(f"Você é maior de idade!")
else:
    print(f"Você é menor de idade!")
