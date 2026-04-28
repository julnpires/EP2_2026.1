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