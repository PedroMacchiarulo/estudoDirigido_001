senha_correta = "python123"
tentativas = 0
limite = 3

while tentativas < limite:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado.")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta. Tentativa {tentativas} de {limite}.")
if tentativas == limite:
    print("Número máximo de tentativas atingida. Acesso negado.")       

