# tests/test_app.pi
import unittest
# Importe também a nova função autenticar_usuario do app.py
from app import saudacao_sistema, adicionar_tarefa, listar_tarefas, autenticar_usuario 

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
        
    def test_autenticar_usuario_sucesso(self):
        """Verifica a autenticação com credenciais corretas."""
        self.assertTrue(autenticar_usuario("admin", "senha123"))

    def test_autenticar_usuario_falha(self):
        """Verifica a autenticação com credenciais incorretas."""
        self.assertFalse(autenticar_usuario("admin", "senhaerrada"))
        self.assertFalse(autenticar_usuario("outro_usuario", "senha123"))
        self.assertFalse(autenticar_usuario("outro_usuario", "senhaerrada"))


if __name__ == '__main__':
    unittest.main()