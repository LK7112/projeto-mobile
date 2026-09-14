#usuarios corretos
usuario_correto = "Luka.Goes"
senha_correta = "Luka123"
max_tentativas = 3
tentativas = 0 
while tentativas < max_tentativas:
    usuario_input = input("Digite o nome de usuário:")
    senha_input = input("Digite sua senha:")
    if usuario_input == usuario_correto and senha_input == senha_correta:
        print("Login bem sucedido!")
        break
    else:
        tentativas += 1
        print(f"Usuário ou senha incorretos. Tentativa {tentativas} de {max_tentativas}.")
        
valor = float(input("Valor da compra: R$"))
distancia = float(input("Distância em km:"))
if valor >= 200:
        frete = 0
else:
        frete = 5 + distancia * 1.5
        print(f"Valor do frete: R${frete:.2f}")
        print(f"Valor total da compra: R${valor + frete:.2f}")