📋 Projeto FastAPI - Formulários & Autenticação
Este projeto é uma API REST desenvolvida com FastAPI para gerenciamento de formulários e perguntas, incluindo autenticação via OAuth2.

🚀 Tecnologias Utilizadas
FastAPI - Framework web moderno para Python

SQLAlchemy - ORM para manipulação de banco de dados

Alembic - Controle de migrações

PostgreSQL - Banco de dados relacional

Pydantic - Validação de dados

Uvicorn - Servidor ASGI para rodar a aplicação

OAuth2 - Autenticação e autorização

✅ Pré-requisitos
Antes de começar, você precisa ter instalado em sua máquina:

Python 3.11+

PostgreSQL

Git

📦 Como rodar o projeto localmente
1️⃣ Clonar o repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2️⃣ Criar e ativar um ambiente virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Instalar as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

ini
Copiar
Editar
DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/nome_do_banco
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
5️⃣ Rodar as migrações
bash
Copiar
Editar
alembic upgrade head
6️⃣ Iniciar o servidor
bash
Copiar
Editar
uvicorn api.main:app --reload
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
