from models.estados import Estados
from models.transicoes import Transicoes

file_path = input()

with open(file_path, 'r') as file:

    qtd_estados = int(file.readline())

    estados_list = [Estados() for i in range(qtd_estados)]

    terminais_list = file.readline().strip().split(' ')[1::]

    estados_aceitacao = file.readline().strip().split(' ')[1::]

    for estado in estados_aceitacao:
        estados_list[int(estado)].is_terminal = True

    qtd_transicao = int(file.readline().strip())

    for i in range(qtd_transicao):
        inicio, valor, fim = file.readline().strip().split(' ')

        transicao = Transicoes(destino=int(fim), valor=valor)

        estados_list[int(inicio)].add_transicao(transicao)

    qtd_cadeias = int(file.readline())

    cadeias = [file.readline().strip() for i in range(qtd_cadeias)]
