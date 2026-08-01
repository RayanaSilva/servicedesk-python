import tkinter as tk
from tkinter import ttk

import database as db
from views import AbaChamado, AbaCliente, AbaFuncionario, AbaGestaoChamados


class ServiceDeskApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sistema de Service Desk")
        self.geometry("750x620")

        # Inicializa o banco de dados e cria as tabelas no Oracle se necessário
        db.init_db()

        # Criar gerenciador de abas (Notebook)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Instanciar a aba de Gestão primeiro para vinculá-la à atualização
        self.tab_gestao = AbaGestaoChamados(self.notebook)

        # Instanciar a aba de Abertura de Chamados
        self.tab_chamado = AbaChamado(
            self.notebook, 
            on_chamado_criado_callback=self.tab_gestao.atualizar_lista
        )

        # Instanciar as abas de Cadastros
        self.tab_cliente = AbaCliente(
            self.notebook, self.tab_chamado.atualizar_comboboxes
        )
        self.tab_funcionario = AbaFuncionario(
            self.notebook, self.tab_chamado.atualizar_comboboxes
        )

        # Adicionar abas ao notebook
        self.notebook.add(self.tab_gestao, text="Gestão de Chamados")
        self.notebook.add(self.tab_chamado, text="Abertura de Chamado")
        self.notebook.add(self.tab_cliente, text="Cadastro de Cliente")
        self.notebook.add(self.tab_funcionario, text="Cadastro de Funcionário")


if __name__ == "__main__":
    app = ServiceDeskApp()
    app.mainloop()