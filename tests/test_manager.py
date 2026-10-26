import unittest
from gerenciador import main


class ManagerTests(unittest.TestCase):
    def run_session(self, values):
        answers = iter(values)
        output = []
        def read(prompt):
            try:
                return next(answers)
            except StopIteration:
                raise EOFError
        main(read, output.append)
        return '\n'.join(output)

    def test_invalid_menu_does_not_crash(self):
        self.assertIn('Escolha uma opção', self.run_session(['abc', '4']))

    def test_empty_removal_does_not_ask_for_index(self):
        self.assertIn('Ainda não há tarefas para remover.', self.run_session(['3', '4']))

    def test_invalid_indices_do_not_remove_a_task(self):
        out = self.run_session(['1', 'Estudar', '3', '0', '3', '99', '3', 'texto', '2', '4'])
        self.assertEqual(out.count('Número fora da lista.'), 2)
        self.assertIn('Informe um número válido.', out)
        self.assertIn('1. Estudar', out)

    def test_add_and_remove(self):
        out = self.run_session(['1', 'Estudar', '3', '1', '2', '4'])
        self.assertIn('Tarefa removida: Estudar', out)
        self.assertIn('Ainda não há tarefas.', out)

    def test_blank_task_is_rejected(self):
        self.assertIn('A tarefa não pode ficar vazia.', self.run_session(['1', ' ', '4']))

    def test_end_of_input_exits(self):
        self.assertIn('Até mais!', self.run_session([]))


if __name__ == '__main__':
    unittest.main()
