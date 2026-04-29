def calcula_pontos_quadra(lista):
    for dado in lista:
        contador = 0
        for numero in lista:
            if numero == dado:
                contador += 1
        if contador == 4:
            soma = 0
            for numero in lista:
                soma += numero
            return soma
    return 0