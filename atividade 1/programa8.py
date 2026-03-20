nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

if idade > 120 ou idade > 0:
    print("Idade inválida! por favor, digite um valor menor ou igual a 120")
else:

    dias_de_vida = idade * 365
    print(f"Olá {nome}, você já viveu cerca de: {dias_de_vida}")