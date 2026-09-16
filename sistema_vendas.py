frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
sucos = frutas
valores = [8]
while True:
    if input_frutas := input("Digite o nome de uma fruta: ").lower() in frutas:
        print("Temos esse suco!")
        print(f"O valor do suco de 400ml é R${valores[0]:.2f}!!")
    else:
        print("Não temos esse suco!")
        break