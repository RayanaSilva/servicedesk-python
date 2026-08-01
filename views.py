import tkinter as tk
from tkinter import messagebox, ttk
import database as db


class AbaCliente(ttk.Frame):
    def __init__(self, parent, on_cadastrar_callback):
        super().__init__(parent)
        self.on_cadastrar_callback = on_cadastrar_callback

        frame = ttk.LabelFrame(self, text=" Dados do Cliente ", padding=15)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nome = ttk.Entry(frame, width=40)
        self.entry_nome.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="E-mail:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_email = ttk.Entry(frame, width=40)
        self.entry_email.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Telefone:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_telefone = ttk.Entry(frame, width=40)
        self.entry_telefone.grid(row=2, column=1, pady=5)

        btn_salvar = ttk.Button(frame, text="Cadastrar Cliente", command=self.salvar)
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=15)

    def salvar(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()

        if not nome:
            messagebox.showwarning("Atenção", "O campo Nome é obrigatório!")
            return

        db.salvar_cliente_db(nome, email, telefone)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)

        self.on_cadastrar_callback()


class AbaFuncionario(ttk.Frame):
    def __init__(self, parent, on_cadastrar_callback):
        super().__init__(parent)
        self.on_cadastrar_callback = on_cadastrar_callback

        frame = ttk.LabelFrame(self, text=" Dados do Funcionário ", padding=15)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nome = ttk.Entry(frame, width=40)
        self.entry_nome.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Equipe:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_equipe = ttk.Entry(frame, width=40)
        self.entry_equipe.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Cargo:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_cargo = ttk.Entry(frame, width=40)
        self.entry_cargo.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="E-mail:").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_email = ttk.Entry(frame, width=40)
        self.entry_email.grid(row=3, column=1, pady=5)

        btn_salvar = ttk.Button(frame, text="Cadastrar Funcionário", command=self.salvar)
        btn_salvar.grid(row=4, column=0, columnspan=2, pady=15)

    def salvar(self):
        nome = self.entry_nome.get().strip()
        equipe = self.entry_equipe.get().strip()
        cargo = self.entry_cargo.get().strip()
        email = self.entry_email.get().strip()

        if not nome:
            messagebox.showwarning("Atenção", "O campo Nome é obrigatório!")
            return

        db.salvar_funcionario_db(nome, equipe, cargo, email)
        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")

        self.entry_nome.delete(0, tk.END)
        self.entry_equipe.delete(0, tk.END)
        self.entry_cargo.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

        self.on_cadastrar_callback()


class AbaChamado(ttk.Frame):
    def __init__(self, parent, on_chamado_criado_callback=None):
        super().__init__(parent)
        self.on_chamado_criado_callback = on_chamado_criado_callback

        frame = ttk.LabelFrame(self, text=" Detalhes do Chamado ", padding=15)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(frame, text="Cliente:").grid(row=0, column=0, sticky="w", pady=5)
        self.cb_cliente = ttk.Combobox(frame, width=37, state="readonly")
        self.cb_cliente.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Atribuir a (Técnico):").grid(row=1, column=0, sticky="w", pady=5)
        self.cb_funcionario = ttk.Combobox(frame, width=37, state="readonly")
        self.cb_funcionario.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Categoria:").grid(row=2, column=0, sticky="w", pady=5)
        self.cb_categoria = ttk.Combobox(
            frame, width=37, state="readonly",
            values=["Hardware", "Software", "Rede", "Sistemas", "Acessos", "Impressora", "Outros"]
        )
        self.cb_categoria.grid(row=2, column=1, pady=5)
        self.cb_categoria.current(0)

        ttk.Label(frame, text="Aplicação:").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_aplicacao = ttk.Entry(frame, width=40)
        self.entry_aplicacao.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Prioridade:").grid(row=4, column=0, sticky="w", pady=5)
        self.cb_prioridade = ttk.Combobox(
            frame, width=37, state="readonly",
            values=["Baixa", "Média", "Alta", "Crítica"]
        )
        self.cb_prioridade.grid(row=4, column=1, pady=5)
        self.cb_prioridade.current(1)

        ttk.Label(frame, text="Descrição:").grid(row=5, column=0, sticky="nw", pady=5)
        self.txt_desc = tk.Text(frame, width=30, height=4)
        self.txt_desc.grid(row=5, column=1, pady=5)

        ttk.Label(frame, text="SLA (em horas):").grid(row=6, column=0, sticky="w", pady=5)
        self.entry_sla = ttk.Entry(frame, width=40)
        self.entry_sla.insert(0, "24")
        self.entry_sla.grid(row=6, column=1, pady=5)

        btn_salvar = ttk.Button(frame, text="Abrir Chamado", command=self.salvar)
        btn_salvar.grid(row=7, column=0, columnspan=2, pady=15)

        self.atualizar_comboboxes()

    def atualizar_comboboxes(self):
        clientes = db.listar_clientes_db()
        self.cb_cliente["values"] = [f"{c[0]} - {c[1]}" for c in clientes]

        funcionarios = db.listar_funcionarios_db()
        self.cb_funcionario["values"] = [f"{f[0]} - {f[1]}" for f in funcionarios]

    def salvar(self):
        cli_sel = self.cb_cliente.get()
        func_sel = self.cb_funcionario.get()
        categoria = self.cb_categoria.get()
        aplicacao = self.entry_aplicacao.get().strip()
        prioridade = self.cb_prioridade.get()
        descricao = self.txt_desc.get("1.0", tk.END).strip()
        sla_str = self.entry_sla.get().strip()

        if not cli_sel or not aplicacao:
            messagebox.showwarning("Atenção", "Selecione um Cliente e preencha a Aplicação!")
            return

        try:
            sla_horas = int(sla_str) if sla_str else 24
        except ValueError:
            messagebox.showwarning("Atenção", "O campo SLA precisa ser um número inteiro de horas!")
            return

        cliente_id = int(cli_sel.split(" - ")[0])
        funcionario_id = int(func_sel.split(" - ")[0]) if func_sel else None

        db.salvar_chamado_db(cliente_id, funcionario_id, categoria, aplicacao, prioridade, descricao, sla_horas)
        messagebox.showinfo("Sucesso", "Chamado aberto com sucesso!")

        self.entry_aplicacao.delete(0, tk.END)
        self.txt_desc.delete("1.0", tk.END)
        self.entry_sla.delete(0, tk.END)
        self.entry_sla.insert(0, "24")

        if self.on_chamado_criado_callback:
            self.on_chamado_criado_callback()


class AbaGestaoChamados(ttk.Frame):
    """Nova aba para inclusão de anotações e encerramento dos chamados em aberto."""
    def __init__(self, parent):
        super().__init__(parent)

        # Divisão superior (Tabela) e inferior (Ações)
        frame_tabela = ttk.LabelFrame(self, text=" Chamados em Aberto ", padding=10)
        frame_tabela.pack(fill="both", expand=True, padx=10, pady=5)

        columns = ("id", "cliente", "categoria", "aplicacao", "prioridade", "status")
        self.tree = ttk.Treeview(frame_tabela, columns=columns, show="headings", height=6)
        
        self.tree.heading("id", text="ID")
        self.tree.column("id", width=40, anchor="center")
        self.tree.heading("cliente", text="Cliente")
        self.tree.column("cliente", width=120)
        self.tree.heading("categoria", text="Categoria")
        self.tree.column("categoria", width=100)
        self.tree.heading("aplicacao", text="Aplicação")
        self.tree.column("aplicacao", width=110)
        self.tree.heading("prioridade", text="Prioridade")
        self.tree.column("prioridade", width=80, anchor="center")
        self.tree.heading("status", text="Status")
        self.tree.column("status", width=90, anchor="center")

        scrollbar = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Painel inferior para interações
        frame_acoes = ttk.LabelFrame(self, text=" Registrar Ação / Anotação ", padding=10)
        frame_acoes.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_acoes, text="Anotação / Solução:").grid(row=0, column=0, sticky="nw", pady=5)
        self.txt_anotacao = tk.Text(frame_acoes, width=50, height=4)
        self.txt_anotacao.grid(row=0, column=1, pady=5, padx=5)

        btn_frame = ttk.Frame(frame_acoes)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=10)

        btn_anotar = ttk.Button(btn_frame, text="Adicionar Anotação", command=self.adicionar_anotacao)
        btn_anotar.pack(side="left", padx=5)

        btn_encerrar = ttk.Button(btn_frame, text="Encerrar Chamado", command=self.encerrar_chamado)
        btn_encerrar.pack(side="left", padx=5)

        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for chamado in db.listar_chamados_abertos_db():
            self.tree.insert("", tk.END, values=chamado)

    def _obter_chamado_selecionado(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione um chamado na tabela para prosseguir.")
            return None
        return self.tree.item(selected[0])["values"][0]

    def adicionar_anotacao(self):
        chamado_id = self._obter_chamado_selecionado()
        if not chamado_id:
            return

        anotacao = self.txt_anotacao.get("1.0", tk.END).strip()
        if not anotacao:
            messagebox.showwarning("Atenção", "Escreva uma anotação antes de salvar!")
            return

        db.adicionar_anotacao_db(chamado_id, anotacao)
        messagebox.showinfo("Sucesso", f"Anotação registrada para o chamado #{chamado_id}!")
        self.txt_anotacao.delete("1.0", tk.END)
        self.atualizar_lista()

    def encerrar_chamado(self):
        chamado_id = self._obter_chamado_selecionado()
        if not chamado_id:
            return

        solucao = self.txt_anotacao.get("1.0", tk.END).strip()
        if not solucao:
            messagebox.showwarning("Atenção", "Informe a solução final no campo de texto para encerrar!")
            return

        if messagebox.askyesno("Confirmação", f"Deseja encerrar definitivamente o chamado #{chamado_id}?"):
            db.encerrar_chamado_db(chamado_id, solucao)
            messagebox.showinfo("Sucesso", f"Chamado #{chamado_id} encerrado!")
            self.txt_anotacao.delete("1.0", tk.END)
            self.atualizar_lista()