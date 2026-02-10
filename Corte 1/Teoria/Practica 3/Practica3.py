while True:

    a = input("Por favor ingrese un valor: ")

    aInt = int(a)

    mod = aInt%2

    if(mod == 0):
        print("a es un PAR")
    else:
        print("a NO es PAR, es IMPAR")

    continuar = input("¿Desea seguir? (S/N)")
    if continuar.lower() != "S":
            print("Gracias.")
            break
