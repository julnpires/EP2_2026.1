def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    dados_no_estoque.pop(dado_para_remover)
    return [dados_rolados, dados_no_estoque]