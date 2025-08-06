### 🧩 **Stack que vamos usar:**

* **Linguagem:** Python
* **Framework:** Flask (leve e ideal para APIs e web apps simples)
* **Banco de Dados:** PostgreSQL
* **IDE:** VSCode
* **ORM (opcional):** SQLAlchemy (facilita integração com o banco)
* **Recursos do projeto:**

  * Login/logout de usuários
  * Cadastro, remoção e edição de produtos
  * Listagem de produtos
  * Interface web simples com HTML (Flask com Jinja2)

---

### ✅ Etapa 1: Estrutura de diretórios e `README.md`

Vamos começar criando uma estrutura de projeto organizada e um `README.md` explicativo.

---

#### 📁 Estrutura inicial da pasta do projeto

```
ecommerce/
│
├── app.py
├── requirements.txt
├── config.py
├── .gitignore
├── README.md
│
├── templates/
│   ├── login.html
│   ├── index.html
│   └── produtos.html
│
├── static/
│   └── style.css
│
├── models/
│   └── models.py
│
└── instance/
    └── config.py
```

markdown
# 🛒 Projeto E-commerce Flask

Este é um projeto simples de e-commerce feito com Flask + PostgreSQL. Ele permite o cadastro, edição e remoção de produtos, além de sistema de login/logout de usuários.

## 🚀 Funcionalidades

- Login e logout de usuários
- Cadastro de novos produtos
- Edição e remoção de produtos
- Listagem de produtos cadastrados

## 🧰 Tecnologias

- Python 3
- Flask
- PostgreSQL
- SQLAlchemy

## ⚙️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/adamanssouza/ecommerce.git
cd ecommerce
````

2. Crie um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # no Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados no arquivo `instance/config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:senha@localhost:5432/ecommerce'
```

5. Execute o projeto:

```bash
python app.py
```

## 📌 Observações

* Crie o banco `ecommerce` no PostgreSQL antes de executar o projeto.
* Para testar login, um usuário admin será criado automaticamente no primeiro acesso (configurável).

---

## 📷 Tela inicial (em breve)



