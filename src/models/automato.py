from models.estados import Estados
from models.transicoes import Transicoes


class Automato():
    def __init__(self, qtd_estados, alfabeto_terminal, vetor_transicoes, estados_iniciais, estados_de_aceitação):
        self.estados = [Estados() for i in range(qtd_estados)]
        self.alfabeto_terminal = alfabeto_terminal
        self.estados_iniciais = [self.estados[i] for i in estados_iniciais]

        for i in estados_de_aceitação:
            self.estados[int(i)].is_terminal = True

        for i in vetor_transicoes:
            source, value, dest = i.split()

            dest = self.estados[int(dest)]
            transicao = Transicoes(dest, value)
            self.estados[int(source)].add_transicao(transicao)

    def processa_cadeia(self, cadeia):
        for estado in self.estados_iniciais:
            if self.processa_cadeia_recur(cadeia, estado):
                return True
        return False

    def processa_cadeia_recur(self, cadeia, estado):
        if len(cadeia) == 0 and estado.is_terminal:
            return True
        elif len(cadeia) > 0:
            for transicao in estado.transicoes:
                if transicao.valor == cadeia[0] and self.processa_cadeia_recur(cadeia[1:], transicao.destino):
                    return True
        return False
