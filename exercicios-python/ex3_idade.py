idade = int(input("Qual a sua idade?"))
cidade = input("Qual a sua cidade?")
if idade >= 60:
    print(f"Você é idoso e mora na cidade de {cidade}")
elif idade >= 18:
    print(f"Você é adulto e mora na cidade de {cidade}")
else:
    print(f"Você é menor de idade e mora na cidade de {cidade}.")


