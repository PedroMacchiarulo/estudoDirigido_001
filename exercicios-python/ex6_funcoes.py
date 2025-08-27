def saudacao(nome):
    return f"Olá, {nome}!"

usuario = input("Digite seu nome: ")
print(saudacao(usuario))

def idade_100(idade):
    anos = 100 - idade
    return f"Faltam {anos} anos para você completar 100 anos"

idade = int(input("Digite sua idade: "))
print(idade_100(idade))
