from models.automato import Automato

# É usado array para o codigo ser usado em outras situações
# Para esse projeto há apenas um estado inicial que é o 0
ESTADO_INICIAL = [0]


def main():
    file_path = input()

    with open(file_path, 'r') as file:
        qtd_estados = int(file.readline())
        terminais_list = file.readline().strip().split(' ')[1::]
        estados_aceitacao = file.readline().strip().split(' ')[1::]
        qtd_transicao = int(file.readline().strip())

        vetor_transicoes = [file.readline().strip() for i in range(qtd_transicao)]

        my_automato = Automato(qtd_estados, terminais_list, vetor_transicoes, ESTADO_INICIAL, estados_aceitacao)

        qtd_cadeias = int(file.readline())

        for i in range(qtd_cadeias):
            cadeia = file.readline().strip()
            if my_automato.processa_cadeia(cadeia):
                print("aceita")
            else:
                print("rejeitada")


if __name__ == "__main__":
    main()
