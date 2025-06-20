# app.py

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

# Adiciona um novo comentário para simular uma mudança na feature/adicionar-autenticacao
# Este é um placeholder para a lógica de autenticação
def autenticar_usuario(usuario, senha):
    """
    Função simples para simular a autenticação de um usuário.
    Retorna True para credenciais válidas, False caso contrário.
    """
    if usuario == "admin" and senha == "senha123":
        return True
    return False

if __name__ == "__main__":
    print(saudacao_sistema())
    
    minhas_tarefas = []
    print(adicionar_tarefa(minhas_tarefas, "Planejar rotas de entrega"))
    print(adicionar_tarefa(minhas_tarefas, "Contactar fornecedores de embalagens"))
    
    print("\nMinhas Tarefas:")
    print(listar_tarefas(minhas_tarefas))

    print("\n--- Testando autenticação ---")
    if autenticar_usuario("admin", "senha123"):
        print("Autenticação bem-sucedida para 'admin'.")
    else:
        print("Falha na autenticação para 'admin'.")

    if autenticar_usuario("usuario", "senhaerrada"):
        print("Autenticação bem-sucedida para 'usuario'.")
    else:
        print("Falha na autenticação para 'usuario'.")