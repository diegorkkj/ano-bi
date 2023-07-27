x = "n"

while x !="y":

    if 2 > 1:
        print("Bem vindo ao ano_by.py o melhor")
        print("o melhor algoritimo que ta tendo.")

    x = int(input("Informe o ano: "))

    sobra = x % 4

    if sobra == 0:
        print(f"{x} é by.")

    else:
        print(f"{x} não é by.")

    x = input("Deseja sair? \n y = SIM \n n = NÃO \n")
    if x == "Y" or x == "sim":
        x = "y"
    elif x == "N" or x == "não":
        x = "n"
