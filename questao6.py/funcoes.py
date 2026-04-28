def calcula_pontos_sequencia_baixa(lista):
    for numero in lista:
        if numero + 1 in lista and numero + 2 in lista and numero + 3 in lista:
            return 15
    return 0