for i in range(3):
    idade = int(input(f"\nQual a idade da {i+1} pessoa? "))
    if idade >= 18:
        print("Você pode entrar na festa!")
    elif idade >= 16:
        print("Você não pode entrar na festa!")
    else:
        print("Entrada Negada!")