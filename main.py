import customtkinter as ctk
import database as db
from views import (
    AbaChamado,
    AbaCliente,
    AbaFuncionario,
    AbaGestaoChamados,
    AbaChamadosEncerrados
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class ServiceDeskApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Sistema de Service Desk")
        self.geometry("980x700")

        # Inicializa o banco de dados e cria as tabelas no Oracle se necessário
        db.init_db()

        # Criar gerenciador de abas (Notebook)
        self.notebook = ctk.CTkTabview(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Adicionar abas ao notebook
        self.notebook.add("Gestão de Chamados")
        self.notebook.add("Abertura de Chamado")
        self.notebook.add("Cadastro de Cliente")
        self.notebook.add("Cadastro de Funcionário")
        self.notebook.add("Chamados Encerrados")
        # Instanciar views dentro das abas
        self.tab_gestao = AbaGestaoChamados(self.notebook.tab("Gestão de Chamados"))
        self.tab_chamado = AbaChamado(
            self.notebook.tab("Abertura de Chamado"),
            on_chamado_criado_callback=self.tab_gestao.atualizar_lista
        )
        self.tab_cliente = AbaCliente(
            self.notebook.tab("Cadastro de Cliente"),
            self.tab_chamado.atualizar_comboboxes
        )
        self.tab_funcionario = AbaFuncionario(
            self.notebook.tab("Cadastro de Funcionário"),
            self.tab_chamado.atualizar_comboboxes
        )
        self.tab_chamados_encerrados = AbaChamadosEncerrados(self.notebook.tab("Chamados Encerrados"))
        # Empacotar cada aba
        self.tab_gestao    .pack(expand=True, fill="both")
        self.tab_chamado   .pack(expand=True, fill="both")
        self.tab_cliente   .pack(expand=True, fill="both")
        self.tab_funcionario.pack(expand=True, fill="both")
        self.tab_chamados_encerrados.pack(expand=True, fill="both")


if __name__ == "__main__":
    app = ServiceDeskApp()
    app.mainloop()