import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ctk
import database as db

# Paleta de cores personalizada para o Treeview
_THREE_BG = "#lelele"
_THREE_FG = "#ffffff"
_THREE_HEADER_BG = "#1F6AA5"
_THREE_SEL_BG = "#2FA572"
_THREE_ROW_H = 28

def _aplicar_estilo_treeview():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background=_THREE_BG,
                    foreground=_THREE_FG,
                    fieldbackground=_THREE_BG,
                    rowheight=_THREE_ROW_H,
                    font=("Segoe UI", 10),
                    borderwidth=0,
    )
    style.configure("Treeview.Heading",
                    background=_THREE_HEADER_BG,
                    foreground=_THREE_FG,
                    font=("Segoe UI", 10, "bold"),
                    relief="flat",
    )
    style.map("Treeview",
                background=_THREE_HEADER_BG,
                foreground=_THREE_FG,
    )

def _label_titulo(parent, text):
    ctk.CTkLabel(parent, 
                 text=text, 
                 font=ctk.CTkFont(size=13, weight="bold"),
                 anchor="w").pack(fill="x",
                                  padx=15,
                                  pady=(12, 0))



class AbaCliente(ctk.CTkFrame):
    def __init__(self, parent, on_cadastrar_callback):
        super().__init__(parent, fg_color="transparent")
        self.on_cadastrar_callback = on_cadastrar_callback

        _label_titulo(self, "Dados do Cliente")

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(fill="both", expand=True, padx=15, pady=10)

        campos = [("Nome:", 0), ("E-mail:", 1), ("Telefone:", 2)]
        for texto, row in campos:
            ctk.CTkLabel(frame, text=texto, anchor="w").grid(row=row, column=0, sticky="w", padx=(15, 5), pady=8
        )

        self.entry_nome     = ctk.CTkEntry(frame, width=320, placeholder_text="Nome completo")
        self.entry_email    = ctk.CTkEntry(frame, width=320, placeholder_text="email@exemplo.com")
        self.entry_telefone = ctk.CTkEntry(frame, width=320, placeholder_text="(00) 00000-0000")

        self.entry_nome    .grid(row=0, column=1, pady=8, padx=(0, 15))
        self.entry_email   .grid(row=1, column=1, pady=8, padx=(0, 15))
        self.entry_telefone.grid(row=2, column=1, pady=8, padx=(0, 15))

        ctk.CTkButton(
            frame, text="Cadastrar Cliente", width=200, command=self.salvar
        ).grid(row=3, column=0, columnspan=2, pady=20)

    def salvar(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()

        if not nome:
            messagebox.showwarning("Atenção", "O campo Nome é obrigatório!")
            return

        db.salvar_cliente_db(nome, email, telefone)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

        self.entry_nome.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_telefone.delete(0, "end")

        self.on_cadastrar_callback()


class AbaFuncionario(ctk.CTkFrame):
    def __init__(self, parent, on_cadastrar_callback):
        super().__init__(parent, fg_color="transparent")
        self.on_cadastrar_callback = on_cadastrar_callback

        _label_titulo(self, "Dados do Funcionário")

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=15, pady=10)

        labels = ["Nome:", "Equipe:", "Cargo:", "E-mail:"]
        placeholders = ["Nome completo", "Ex: Suporte N1", "Ex: Analista", "email@empresa.com"]
        for i, (lbl, ph) in enumerate(zip(labels, placeholders)):
            ctk.CTkLabel(frame, text=lbl, anchor="w").grid(
                row=i, column=0, sticky="w", padx=(15, 5), pady=8
            )
            entry = ctk.CTkEntry(frame, width=320, placeholder_text=ph)
            entry.grid(row=i, column=1, pady=8, padx=(0, 15))
            attr = ["entry_nome", "entry_equipe", "entry_cargo", "entry_email"][i]
            setattr(self, attr, entry)

        ctk.CTkButton(
            frame, text="Cadastrar Funcionário", width=200, command=self.salvar
        ).grid(row=4, column=0, columnspan=2, pady=20)

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

        for entry in [self.entry_nome, self.entry_equipe, self.entry_cargo, self.entry_email]:
            entry.delete(0, "end")

        self.on_cadastrar_callback()


class AbaChamado(ctk.CTkFrame):
    def __init__(self, parent, on_chamado_criado_callback=None):
        super().__init__(parent, fg_color="transparent")
        self.on_chamado_criado_callback = on_chamado_criado_callback

        _label_titulo(self, "🎫  Detalhes do Chamado")

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=15, pady=10)

        
        ctk.CTkLabel(frame, text="Cliente:", anchor="w").grid(
            row=0, column=0, sticky="w", padx=(15, 5), pady=8
        )
        self.cb_cliente = ctk.CTkComboBox(frame, width=320, state="readonly", values=[])
        self.cb_cliente.grid(row=0, column=1, pady=8, padx=(0, 15))

        
        ctk.CTkLabel(frame, text="Atribuir a (Técnico):", anchor="w").grid(
            row=1, column=0, sticky="w", padx=(15, 5), pady=8
        )
        self.cb_funcionario = ctk.CTkComboBox(frame, width=320, state="readonly", values=[])
        self.cb_funcionario.grid(row=1, column=1, pady=8, padx=(0, 15))

        
        ctk.CTkLabel(frame, text="Categoria:", anchor="w").grid(
            row=2, column=0, sticky="w", padx=(15, 5), pady=8
        )
        self.cb_categoria = ctk.CTkComboBox(
            frame, width=320, state="readonly",
            values=["Hardware", "Software", "Rede", "Sistemas", "Acessos", "Impressora", "Outros"]
        )
        self.cb_categoria.set("Hardware")
        self.cb_categoria.grid(row=2, column=1, pady=8, padx=(0, 15))

        
        ctk.CTkLabel(frame, text="Aplicação:", anchor="w").grid(
            row=3, column=0, sticky="w", padx=(15, 5), pady=8
        )
        self.entry_aplicacao = ctk.CTkEntry(frame, width=320, placeholder_text="Nome da aplicação")
        self.entry_aplicacao.grid(row=3, column=1, pady=8, padx=(0, 15))

        
        ctk.CTkLabel(frame, text="Prioridade:", anchor="w").grid(
            row=4, column=0, sticky="w", padx=(15, 5), pady=8
        )
        self.cb_prioridade = ctk.CTkComboBox(
            frame, width=320, state="readonly",
            values=["Baixa", "Média", "Alta", "Crítica"]
        )
        self.cb_prioridade.set("Média")
        self.cb_prioridade.grid(row=4, column=1, pady=8, padx=(0, 15))

        
        ctk.CTkLabel(frame, text="Descrição:", anchor="w").grid(
            row=5, column=0, sticky="nw", padx=(15, 5), pady=8
        )
        self.txt_desc = ctk.CTkTextbox(frame, width=320, height=80)
        self.txt_desc.grid(row=5, column=1, pady=8, padx=(0, 15))

        
        ctk.CTkLabel(frame, text="SLA (em horas):", anchor="w").grid(
            row=6, column=0, sticky="w", padx=(15, 5), pady=8
        )
        self.entry_sla = ctk.CTkEntry(frame, width=320, placeholder_text="24")
        self.entry_sla.insert(0, "24")
        self.entry_sla.grid(row=6, column=1, pady=8, padx=(0, 15))

        ctk.CTkButton(
            frame, text="Abrir Chamado", width=200, command=self.salvar
        ).grid(row=7, column=0, columnspan=2, pady=20)

        self.atualizar_comboboxes()

    def atualizar_comboboxes(self):
        clientes = db.listar_clientes_db()
        self.cb_cliente.configure(values=[f"{c[0]} - {c[1]}" for c in clientes])

        funcionarios = db.listar_funcionarios_db()
        self.cb_funcionario["values"] = [f"{f[0]} - {f[1]}" for f in funcionarios]

    def salvar(self):
        cli_sel = self.cb_cliente.get()
        func_sel = self.cb_funcionario.get()
        categoria = self.cb_categoria.get()
        aplicacao = self.entry_aplicacao.get().strip()
        prioridade = self.cb_prioridade.get()
        descricao = self.txt_desc.get("1.0", "end").strip()
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

        self.entry_aplicacao.delete(0, "end")
        self.txt_desc.delete("1.0", "end")
        self.entry_sla.delete(0, "end")
        self.entry_sla.insert(0, "24")

        if self.on_chamado_criado_callback:
            self.on_chamado_criado_callback()


class AbaGestaoChamados(ctk.CTkFrame):
    """Nova aba para inclusão de anotações e encerramento dos chamados em aberto."""
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        _aplicar_estilo_treeview()

        
        _label_titulo(self, "Chamados em Aberto")

        frame_tabela = ctk.CTkFrame(self)
        frame_tabela.pack(fill="both", expand=True, padx=15, pady=(5, 0))

        columns = ("id", "cliente", "categoria", "aplicacao", "prioridade", "status")
        self.tree = ttk.Treeview(frame_tabela, columns=columns, show="headings", height=8)

        self.tree.heading("id",        text="ID")
        self.tree.heading("cliente",   text="Cliente")
        self.tree.heading("categoria", text="Categoria")
        self.tree.heading("aplicacao", text="Aplicação")
        self.tree.heading("prioridade",text="Prioridade")
        self.tree.heading("status",    text="Status")

        self.tree.column("id",         width=45,  anchor="center")
        self.tree.column("cliente",    width=130)
        self.tree.column("categoria",  width=100)
        self.tree.column("aplicacao",  width=120)
        self.tree.column("prioridade", width=85,  anchor="center")
        self.tree.column("status",     width=100, anchor="center")

        scrollbar = ctk.CTkScrollbar(frame_tabela, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


        _label_titulo(self, "Registrar Ação / Anotação")

        frame_acoes = ctk.CTkFrame(self)
        frame_acoes.pack(fill="x", padx=15, pady=(5, 15))

        ctk.CTkLabel(frame_acoes, text="Anotação / Solução:", anchor="w").grid(
            row=0, column=0, sticky="nw", padx=(15, 5), pady=10
        )
        self.txt_anotacao = ctk.CTkTextbox(frame_acoes, width=420, height=90)
        self.txt_anotacao.grid(row=0, column=1, pady=10, padx=(0, 15))

        btn_frame = ctk.CTkFrame(frame_acoes, fg_color="transparent")
        btn_frame.grid(row=1, column=0, columnspan=2, pady=(0, 12))

        ctk.CTkButton(
            btn_frame, text="Adicionar Anotação", width=180,
            command=self.adicionar_anotacao
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            btn_frame, text="Encerrar Chamado", width=180,
            fg_color="#c0392b", hover_color="#922b21",
            command=self.encerrar_chamado
        ).pack(side="left", padx=8)

        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for chamado in db.listar_chamados_abertos_db():
            self.tree.insert("", "end", values=chamado)

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

        anotacao = self.txt_anotacao.get("1.0", "end").strip()
        if not anotacao:
            messagebox.showwarning("Atenção", "Escreva uma anotação antes de salvar!")
            return

        db.adicionar_anotacao_db(chamado_id, anotacao)
        messagebox.showinfo("Sucesso", f"Anotação registrada para o chamado #{chamado_id}!")
        self.txt_anotacao.delete("1.0", "end")
        self.atualizar_lista()

    def encerrar_chamado(self):
        chamado_id = self._obter_chamado_selecionado()
        if not chamado_id:
            return

        solucao = self.txt_anotacao.get("1.0", "end").strip()
        if not solucao:
            messagebox.showwarning("Atenção", "Informe a solução final no campo de texto para encerrar!")
            return

        if messagebox.askyesno("Confirmação", f"Deseja encerrar definitivamente o chamado #{chamado_id}?"):
            db.encerrar_chamado_db(chamado_id, solucao)
            messagebox.showinfo("Sucesso", f"Chamado #{chamado_id} encerrado!")
            self.txt_anotacao.delete("1.0", "end")
            self.atualizar_lista()