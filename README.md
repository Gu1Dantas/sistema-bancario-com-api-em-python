# 🏦 Sistema Bancário com API REST — Python

Sistema bancário com API REST desenvolvido em Python, com arquitetura modular e persistência de dados em JSON.

## 🚀 Tecnologias

- **Python 3**
- **FastAPI** — API REST com endpoints documentados automaticamente
- **Uvicorn** — servidor ASGI para rodar a API
- **POO** — Orientação a Objetos com separação de responsabilidades

## 📁 Estrutura do Projeto

```
├── app.py         # Ponto de entrada — menu terminal
├── api.py         # API REST com FastAPI (endpoints)
├── banco.py       # Classe Conta — lógica de negócio
├── utils.py       # Funções auxiliares (carregar/salvar dados)
└── historico.json # Persistência de dados
```

## 📌 Endpoints da API

| Método | Rota          | Descrição                        |
|--------|---------------|----------------------------------|
| GET    | `/`           | Status da API                    |
| GET    | `/saldo`      | Consulta saldo atual             |
| GET    | `/historico`  | Histórico de transações          |
| POST   | `/deposito`   | Realiza um depósito              |
| POST   | `/saque`      | Realiza um saque                 |
| POST   | `/transferir` | Realiza uma transferência        |

## ▶️ Como executar

### Via terminal

```bash
git clone https://github.com/Gu1Dantas/sistema-bancario-com-api-em-python.git
cd sistema-bancario-com-api-em-python
pip install fastapi uvicorn
python app.py
```

### Via API REST

```bash
uvicorn api:app --reload
```

Acesse a documentação automática em: `http://localhost:8000/docs`

## ✅ Funcionalidades

- Criar e consultar contas
- Depositar, sacar e transferir valores
- Validação de operações (saldo insuficiente, valor inválido)
- Histórico de transações persistido em JSON
- Dados salvos entre sessões

## Autor

**Guilherme Dantas** — [LinkedIn](https://www.linkedin.com/in/guilherme-dantas-541678273) · [GitHub](https://github.com/Gu1Dantas)
