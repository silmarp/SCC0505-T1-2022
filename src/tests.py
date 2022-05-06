import unittest
from models.automato import Automato


class Test_automato(unittest.TestCase):

    def setUp(self):
        self.automato_deterministico = Automato(3, ["a", "b"], ["0 a 1", "0 b 2", "1 b 1", "1 a 2", "2 a 2", "2 b 1"], [0], [2])

        self.automato_nao_deterministico = Automato(4, ["a", "b"], ["0 a 1", "0 a 2", "2 a 3", "1 b 3"], [0], [3])

    def test_deterministico(self):
        cadeias = (
            ["aaaaaba", True],
            ["aabaabbac", False],  # caracter fora do alfabeto terminal
            ["", False],  # cadeia vazia
            ["baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", True],
            ["aab", False])

        for test in cadeias:
            with self.subTest():
                self.assertEqual(self.automato_deterministico.processa_cadeia(test[0]), test[1])

    def test_nao_deterministico(self):
        cadeias = (
            ["ab", True],
            ["aa", True],
            ["c", False],  # caracter fora do alfabeto terminal
            ["", False],  # cadeia vazia
            ["aaa", False],
            ["b", False],
            ["bb", False],
            ["aab", False])

        for test in cadeias:
            with self.subTest():
                self.assertEqual(self.automato_nao_deterministico.processa_cadeia(test[0]), test[1])


if __name__ == '__main__':
    unittest.main()
