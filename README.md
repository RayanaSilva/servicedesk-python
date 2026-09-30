# 🖥️ Service Desk — Sistema de Gerenciamento de Chamados

Sistema desktop de gerenciamento de chamados de suporte técnico, desenvolvido em Python como projeto de estudo.

A aplicação permite abrir, acompanhar e encerrar chamados de Service Desk, com cadastro de clientes e funcionários, controle de prioridade, SLA e histórico de anotações.

---

## 📋 Funcionalidades

- ✅ Cadastro de clientes
- ✅ Cadastro de funcionários (técnicos)
- ✅ Abertura de chamados com categoria e prioridade
- ✅ Atribuição de chamados a funcionários
- ✅ Definição de SLA (prazo em horas)
- ✅ Registro de anotações durante o atendimento
- ✅ Alteração automática de status (Aberto → Em Andamento → Encerrado)
- ✅ Encerramento de chamados com registro da solução
- ✅ Histórico completo de ações por chamado

---

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — Interface gráfica
- [Oracle Database](https://www.oracle.com/database/) — Banco de dados relacional
- [oracledb](https://python-oracledb.readthedocs.io/) — Conexão Python com Oracle
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Gerenciamento de variáveis de ambiente

---

## 📁 Estrutura do projeto

```
ServiceDesk/
├── main.py           # Ponto de entrada da aplicação e configuração das abas
├── views.py          # Telas e componentes da interface gráfica (Tkinter)
├── database.py       # Conexão com o banco de dados e operações CRUD
├── icon.ico          # Ícone da aplicação
├── requirements.txt  # Dependências do projeto
├── .env.example      # Exemplo de configuração das variáveis de ambiente
└── .gitignore        # Arquivos ignorados pelo Git
```

---

## ⚙️ Como executar o projeto

### Pré-requisitos

- Python 3.10 ou superior instalado
- Oracle Database configurado e em execução
- `pip` disponível no terminal

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/service-desk-python.git
cd service-desk-python
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
ORACLE_USER=seu_usuario
ORACLE_PASSWORD=sua_senha
ORACLE_DSN=localhost:1521/FREEPDB1
```

> ⚠️ **Nunca compartilhe o arquivo `.env`.** Ele contém suas credenciais e já está listado no `.gitignore`.

### 5. Execute a aplicação

```bash
python main.py
```

As tabelas serão criadas automaticamente no banco de dados na primeira execução.

---

## 🗄️ Modelo do banco de dados

O sistema utiliza 4 tabelas no Oracle Database:

| Tabela | Descrição |
|---|---|
| `clientes` | Dados dos clientes que abrem chamados |
| `funcionarios` | Dados dos técnicos responsáveis pelo atendimento |
| `chamados` | Registro dos chamados com status, prioridade e SLA |
| `historico_chamados` | Anotações e histórico de ações de cada chamado |

---

## 🚀 Próximas melhorias planejadas

- ✅ Consulta de chamados encerrados com filtro por período, cliente ou técnico 30/09/26
- ✅ Visualização detalhada do chamado encerrado (solução, histórico e data de fechamento) 30/09/26
- [ ] Autenticação de usuários (login e senha)
- [ ] Filtros por status, prioridade e categoria na tela de gestão
- [ ] Tela de histórico completo por chamado
- [ ] Relatórios e métricas de atendimento
- [ ] Validação de e-mail e telefone nos formulários
- [ ] Melhor tratamento de erros de conexão com o banco
- [ ] Separação em camadas (MVC)
- [ ] Testes automatizados

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar e consolidar os seguintes conhecimentos:

- Programação em Python
- Programação orientada a objetos (POO)
- Criação de interfaces gráficas com Tkinter
- Operações CRUD com banco de dados relacional
- Relacionamentos entre tabelas e chaves estrangeiras
- Boas práticas de segurança (variáveis de ambiente)
- Organização de um projeto desktop

---

## ⚠️ Observação

Este projeto foi desenvolvido para fins de estudo e aprendizado. Não é uma aplicação pronta para uso em produção. Melhorias serão implementadas conforme o avanço nos estudos.

---

## 👤 Autor

**Rayana da Silva**
- LinkedIn: [linkedin.com/in/rayana-silvaa](https://linkedin.com/in/rayana-silvaa)
- GitHub: [github.com/RayanaSilva](https://github.com/RayanaSilva)
