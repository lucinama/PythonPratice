def contador_notas(multiplo, numero):
    if(numero % multiplo == 0):
        notas = numero / multiplo
        return notas
    else:
        return -1


entrada = int(input())
resultado = contador_notas(100, entrada)
if (resultado != -1):
    print("{} nota(s) de R$ {}".format(resultado, 100))