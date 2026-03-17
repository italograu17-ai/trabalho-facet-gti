# solicita os dados 
nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))

print(f"Olá, {nome_usuario}! Seja bem-vindo ao nosso programa.")
anos_faltantes = 100 - idade_usuario

if anos_faltantes > 0:
    print(f"Faltam apenas {anos_faltantes} anos para voce completar um século de vida!")
elif anos_faltantes == 0:
    print("Parabens! Voce já completou 100 anos hoje")
else:
    print(f"Incrivel voce já passou dos 100 anos há {abs(anos_faltantes)} anos.")