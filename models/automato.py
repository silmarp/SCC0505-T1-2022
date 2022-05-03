from models.estados import Estados
from models.transicoes import Transicoes


class Automato():
    def __init__(self, qtd_estados, alfabeto_terminal, vetor_transicoes, estados_iniciais, estados_de_aceitação):
        self.estados = [Estados() for i in range(qtd_estados)]
        self.alfabeto_terminal = alfabeto_terminal
        self.estados_iniciais = estados_iniciais

        for i in estados_de_aceitação:
            self.estados[int(i)].is_terminal = True

        for i in vetor_transicoes:
            source, value, dest = i.split()

            dest = self.estados[int(dest)]
            transicao = Transicoes(dest, value)
            self.estados[int(source)].add_transicao(transicao)

#    def processa_cadeia(self, cadeia):
