from funcoes import *
import random

cartela = {
    'regra_simples': {
        1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)
for rodada in range(12):
    dados = []
    for i in range(5):
        dados.append(random.randint(1, 6))
    guardados = []
    finalizado = False
    rerrolagens = 0
    while finalizado == False:
        print("Dados rolados:", dados)
        print("Dados guardados:", guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()
        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados):
                valor = dados[indice]
                guardados.append(valor)
                nova_lista = []
                for i in range(len(dados)):
                    if i != indice:
                        nova_lista.append(dados[i])
                dados = nova_lista

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(guardados):
                valor = guardados[indice]
                dados.append(valor)
                nova_lista = []
                for i in range(len(guardados)):
                    if i != indice:
                        nova_lista.append(guardados[i])
                guardados = nova_lista

        elif opcao == "3":
            if rerrolagens < 2:
                dados = []
                quantidade = 5 - len(guardados)
                for i in range(quantidade):
                    dados.append(random.randint(1, 6))
                rerrolagens = rerrolagens + 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            categoria = None
            while categoria is None:
                print("Digite a combinação desejada:")
                entrada = input()
                if entrada in ['1','2','3','4','5','6']:
                    chave = int(entrada)
                    if cartela['regra_simples'][chave] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + guardados, entrada, cartela)
                        finalizado = True
                        categoria = entrada
                elif entrada in cartela['regra_avancada']:
                    if cartela['regra_avancada'][entrada] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + guardados, entrada, cartela)
                        finalizado = True
                        categoria = entrada
        else:
            print("Combinação inválida. Tente novamente.")

pontuacao_total = 0
for valor in cartela['regra_simples'].values():
    if valor != -1:
        pontuacao_total += valor
for valor in cartela['regra_avancada'].values():
    if valor != -1:
        pontuacao_total += valor

soma_simples = 0
for valor in cartela['regra_simples'].values():
    if valor != -1:
        soma_simples += valor
if soma_simples >= 63:
    pontuacao_total += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total}")