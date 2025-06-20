# tests/test_app.py
import unittest
from app import saudacao_sistema, adicionar_tarefa, listar_tarefas

class TestSistemaTarefas(unittest.TestCase):

    def test_saudacao_sistema(self):
        """Verifica se a função de saudação retorna o texto esperado."""
        self.assertEqual(saudacao_sistema(), "Bem-vindo ao Sistema de Gerenciamento de Tarefas para Logística!")

    def test_adicionar_tarefa(self):
        """Verifica se uma tarefa é adicionada corretamente."""
        lista = []
        adicionar_tarefa(lista, "Comprar suprimentos")
        self.assertIn("Comprar suprimentos", lista)
        self.assertEqual(len(lista), 1)

    def test_listar_tarefas_vazia(self):
        """Verifica a mensagem quando a lista de tarefas está vazia."""
        lista = []
        self.assertEqual(listar_tarefas(lista), "Nenhuma tarefa cadastrada.")

    def test_listar_varias_tarefas(self):
        """Verifica se várias tarefas são listadas corretamente."""
        lista = ["Tarefa A", "Tarefa B"]
        resultado = listar_tarefas(lista)
        self.assertIn("- Tarefa A", resultado)
        self.assertIn("- Tarefa B", resultado)
        self.assertNotIn("Nenhuma tarefa cadastrada", resultado)

if __name__ == '__main__':
    unittest.main()