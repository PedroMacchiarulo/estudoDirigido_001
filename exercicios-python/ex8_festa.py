vezes = int(input("Quantas idades deseja consultar? "))
for i in range(vezes):
    idade = int(input(f"\nQual a idade da {i+1} pessoa? "))
    
    if idade >= 18:
        print("Você pode entrar na festa!")
    elif idade >= 16:
        print("Você não pode entrar na festa!")
    else:
        print("Entrada Negada!")
    