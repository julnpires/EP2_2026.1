def calcula_pontos_quina(dados):
    contagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in dados:
        contagem[dado] += 1

    for qtd in contagem.values():
        if qtd >= 5:
            return 50
    return 0