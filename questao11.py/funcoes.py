def calcula_pontos_quina(dados):
    contagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in dados:
        contagem[dado] += 1

    for qtd in contagem.values():
        if qtd >= 5:
            return 50
    return 0

def calcula_pontos_full_house (dados):
    trinca = False
    dupla = False
    for face in range(1, 7):
        if dados.count(face) == 3:
            trinca = True
        if dados.count(face) == 2:
            dupla = True
    if trinca and dupla:
        soma = 0
        for dado in dados:
            soma += dado
        return soma
    return 0

def calcula_pontos_quadra(lista):
    for dado in lista:
        contador = 0
        for numero in lista:
            if numero == dado:
                contador += 1
        if contador >= 4:
            soma = 0
            for numero in lista:
                soma += numero
            return soma
    return 0

def calcula_pontos_soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

def calcula_pontos_sequencia_alta (dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 30
    if 2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 30
    return 0

def calcula_pontos_sequencia_baixa(lista):
    for numero in lista:
        if numero + 1 in lista and numero + 2 in lista and numero + 3 in lista:
            return 15
    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }