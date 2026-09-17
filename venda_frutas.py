itens = ["ovo", 5.5, "chocolate", 7.5, "morango", 6.5]
input_fruta = input(f"Digite o nome da fruta que deseja comprar(separar por vírgula):{itens}:").strip()
total = 0
for fruta in input_fruta.split(","):
    fruta = fruta.strip()
    if fruta in itens:
        index = itens.index(fruta)
        preco = itens[index + 1]
        total += preco
        print(f"Você comprou {fruta} por R${preco:.2f}")
        for i in range(1, len(itens), 2):
         total += itens[i]
         print(f"Total da compra: R${total:.2f}")
    else:
        print(f"{fruta} não está disponível.")