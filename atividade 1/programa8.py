nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

if idade > 120:
    prin("Idade inválida! por favor, digite um valor")
dias_de_vida = idade * 365
print("voce ja viveu: ",dias_de_vida, "de sua vida")