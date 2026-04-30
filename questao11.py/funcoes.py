from funcoes import calcula_pontos_quina, calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_sem_combinacao, calcula_pontos_sequencia_alta, calcula_pontos_sequencia_baixa
def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_sem_combinacao(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }