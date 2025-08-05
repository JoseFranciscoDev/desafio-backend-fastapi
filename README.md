# 📋 Projeto FastAPI - Formulários & Autenticação

Este projeto é uma **API REST** desenvolvida com **FastAPI** para gerenciamento de formulários e perguntas, incluindo autenticação via OAuth2.

---

## 🚀 Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno para Python
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para manipulação de banco de dados
- **[Alembic](https://alembic.sqlalchemy.org/)** - Controle de migrações
- **[PostgreSQL](https://www.postgresql.org/)** - Banco de dados relacional
- **[Pydantic](https://docs.pydantic.dev/)** - Validação de dados
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI para rodar a aplicação
- **[OAuth2](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)** - Autenticação e autorização

---

## ✅ Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:

- [Python 3.11+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Git](https://git-scm.com/)

---

## 📦 Como rodar o projeto localmente

### 1️⃣ **Clonar o repositório**
```bash
git clone git@github.com:JoseFranciscoDev/desafio-backend-fastapi.git
cd seu-repositorio
````
2️⃣ Criar e ativar um ambiente virtual
````bash
python -m venv venv
````
# Linux/Mac
````bash
source venv/bin/activate

# Windows
````
venv\Scripts\activate
````
3️⃣ Instalar as dependências
````bash
pip install -r requirements.txt
````
4️⃣ Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
````bash
DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/nome_do_banco
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
````
5️⃣ Rodar as migrações
```
alembic upgrade head
````
6️⃣ Iniciar o servidor
````bash
fastapi dev main.py
````
A API estará disponível em:
👉 http://127.0.0.1:8000

📚 Documentação interativa
Acesse a documentação automática do FastAPI:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

🔑 Autenticação
A autenticação é feita via OAuth2 com Password Flow.
Para obter um token de acesso:

Endpoint: POST /auth/token

Body (form-data):

makefile
Copiar
Editar
username: seu_usuario
password: sua_senha
📌 Endpoints disponíveis
🔐 Autenticação
Método	Rota	Descrição
POST	/auth/token	Gera um token JWT para login

📝 Formulários
Método	Rota	Descrição
POST	/api/v1/formularios	Cria um novo formulário
GET	/api/v1/formularios	Lista os formulários com filtros, paginação e ordenação

Parâmetros de Query para listagem:

titulo → Filtra por título

descricao → Filtra por descrição

ordem → Filtra por ordem

sort_by → Campo para ordenar (ex.: id, titulo)

sort_order → asc ou desc

skip → Pular registros (paginação)

limit → Limitar quantidade de registros

Exemplo:

bash
Copiar
Editar
GET /api/v1/formularios/?sort_by=id&sort_order=asc&skip=0&limit=10
❓ Perguntas
Método	Rota	Descrição
POST	/api/v1/formularios/{formulario_id}/perguntas	Adiciona perguntas a um formulário
GET	/api/v1/formularios/{formulario_id}/perguntas	Lista perguntas de um formulário

Parâmetros de Query para listagem:

tipo → Filtra por tipo de pergunta

obrigatoria → Filtra por obrigatoriedade (true ou false)

skip → Paginação (pular registros)

limit → Limitar registros

🛠 Estrutura do projeto
css
Copiar
Editar
📂 projeto/
├── api/
│   ├── _database/
│   │   ├── models.py
│   │   └── ...
│   ├── Formulario/
│   │   ├── controller.py
│   │   └── service.py
│   ├── utils/
│   │   └── db_services.py
│   ├── main.py
│   └── ...
├── migrations/
├── requirements.txt
└── README.md

