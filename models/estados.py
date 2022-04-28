from models import transicoes


class Estados():
    def __init__(self, transicoes = [], is_terminal = False):
        self.transicoes = transicoes
        self.is_terminal = is_terminal

    def add_transicao(self, transicao):
        setattr(self, 'transicoes', self.transicoes + [transicao])

    def print_info(self):
        print(self.transicoes.__dict__)
