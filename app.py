# app.py

def saudacao_sistema():
    """Retorna uma saudação simples para o sistema de gerenciamento de tarefas."""
    return "Bem-vindo ao Sistema de Gerenciamento de Tarefas para Logística!"

def adicionar_tarefa(lista_tarefas, tarefa):
    """Adiciona uma nova tarefa à lista."""
    lista_tarefas.append(tarefa)
    return f"Tarefa '{tarefa}' adicionada."

def listar_tarefas(lista_tarefas):
    """Lista todas as tarefas."""
    if not lista_tarefas:
        return "Nenhuma tarefa cadastrada."
    return "\n".join([f"- {t}" for t in lista_tarefas])

if __name__ == "__main__":
    print(saudacao_sistema())
    
    minhas_tarefas = []
    adicionar_tarefa(minhas_tarefas, "Planejar rotas de entrega")
    adicionar_tarefa(minhas_tarefas, "Contactar fornecedores de embalagens")
    
    print("\nMinhas Tarefas:")
    print(listar_tarefas(minhas_tarefas))