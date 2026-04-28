def calcula_pontos_regra_simples(dados):
    resultado = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for numero in dados:
        if numero in resultado:
            resultado[numero] += numero
    return resultado