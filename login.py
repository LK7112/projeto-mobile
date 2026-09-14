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