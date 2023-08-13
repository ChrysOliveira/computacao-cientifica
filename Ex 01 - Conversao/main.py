print("Escolha uma opcao:")
print("1 - Pe para metros")
print("2 - Pe para jardas")
print("3 - Metros para Jardas")
print("4 - Metros para Pe")
print("5 - Jardas para Pe")
print("6 - Jardas para Metro")

escolha = int(input())

valor = int(input("Digite o valor\n"))

match escolha:
    case 1:
        valor = valor * 0.3048
    case 2:
        valor = valor / 3
    case 3:
        valor = valor / 0.9144
    case 4:
        valor = valor * 3.281
    case 5:
        valor = valor * 3
    case 6:
        valor = valor * 0.9144
    case _:
        print("Escolha um valor valido")

print("O resultado eh: " + str(valor))