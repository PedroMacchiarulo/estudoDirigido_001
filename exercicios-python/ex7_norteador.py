print("Selecione a forma de pagamento:")
print("1 - Dinheiro")
print("2 - Pix")
print("3 - Cartão")
print("4 - Outro")

opcao = input("Digite o número da opção: ")
valor = float(input("Digite o valor da compra: "))

if opcao == "1":  # Dinheiro
    valor_pago = float(input("Digite o valor entregue: "))
    if valor_pago == valor:
        print("Pagamento aceito em dinheiro (valor exato).")
    else:
        print("Só é aceito dinheiro com valor exato.")

elif opcao == "2":  # Pix
    print("Pagamento aceito via Pix, qualquer valor.")

elif opcao == "3":  # Cartão
    if valor >= 20:
        print("Pagamento aceito no cartão.")
    else:
        print("No cartão só é permitido para compras acima de R$20.")

elif opcao == "4":  # Outro
    print("Forma de pagamento não aceita.")

else:
    print("Opção inválida.")
