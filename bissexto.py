def coletar_ano():
    ano = int(input("Digite um ano de seu interesse: "))
    return ano

def bissexto(n1):
    calculo_bissexto1 = n1 % 4
    calculo_bissexto2 = n1 % 100
    calculo_bissexto3 = n1 % 400
    caminho1 = bool(calculo_bissexto1 == 0 and calculo_bissexto2 != 0)
    caminho2 = bool(calculo_bissexto3 == 0)
    print("O ano ", end="")
    if caminho1 == True or caminho2 == True:
        print("é bissexto.")
    else:
        print("não é bissexto.")



ano_usuario = coletar_ano()
e_bissexto_usuario = bissexto(ano_usuario)