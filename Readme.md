# Product Inventory API 📦
Este é um projeto simples de API RESTful com FastAPI para gerenciar o controle de estoque de produtos. Ele fornece funcionalidades básicas de CRUD e controle de estoque, sendo uma excelente base para o aprendizado de FastAPI.

# ✨ Funcionalidades
📋 Listar todos os produtos.
🔍 Buscar produto por ID.
🔎 Pesquisar produtos por nome.
➕ Adicionar um novo produto.
✏️ Atualizar um produto existente.
❌ Deletar um produto.

## 🌐 Endpoints
### 1️⃣ **Listar Todos os Produtos** 📋
**GET** /products
Retorna a lista de todos os produtos cadastrados.

Exemplo de Resposta:
'''
{
  "status": "success",
  "message": "Products retrieved successfully.",
  "data": [...]
}
'''

### 2️⃣ **Buscar Produto por ID**🔍
**GET** /products/{product_id}

Retorna as informações de um produto utilizando seu ID.

Exemplo de Resposta (se encontrado):

```json
{
  "status": "success",
  "message": "Product retrieved successfully.",
  "data": {
    "id": 1,
    "name": "Mouse Gamer",
    "description": "Mouse RGB com 7 botões programáveis",
    "price": 150.99,
    "stock": 20
  }
}
```

Exemplo de Resposta (se não encontrado):

```json
{
  "detail": "Product not found."
}
```

### 3️⃣ **Pesquisar Produtos por Nome** 🔎
**GET** /products/search?name={name}

Procura por produtos cujo nome contém o termo de busca (case-insensitive).

Exemplo de Resposta:

```json
{
  "status": "success",
  "message": "Products retrieved successfully.",
  "data": [...]
}
```
### 4️⃣ **Adicionar Novo Produto** ➕
**POST** /products

**Body (form-data):**

- `name` (string, required)
- `description` (string, required)
- `price` (string, required)
- `stock` (string, required)

**Exemplo de Requisição (form-data no Postman)**

```json
{
  "status": "success",
  "message": "Product added successfully.",
  "data": {
    "id": 1,
    "name": "Mouse Gamer",
    "description": "Mouse RGB com 7 botões programáveis",
    "price": 150.99,
    "stock": 20
  }
}
```
### 5️⃣ **Atualizar Produto** ✏️
**PUT** /products/{product_id}

Body (form-data):

```json
{
  "status": "success",
  "message": "Product updated successfully.",
  "data": {
    "id": 1,
    "name": "Mouse Gamer PRO",
    "description": "Mouse RGB com 7 botões programáveis e iluminação",
    "price": 199.99,
    "stock": 50
  }
}
```
### 6️⃣ **Deletar Produto** ❌
**DELETE** /products/{product_id}

Remove um produto pelo seu ID.

Exemplo de Resposta:

```json
{
  "status": "success",
  "message": "Product deleted successfully.",
  "data": {
    "id": 1,
    "name": "Mouse Gamer",
    "description": "Mouse RGB com 7 botões programáveis",
    "price": 150.99,
    "stock": 20
  }
}
```
Exemplo de Resposta (se o produto não for encontrado):

```json
{
  "detail": "Product not found."
} 
```

## 🚀 Como Executar
### 🔧 Pré-requisitos
- Python 3.9 ou superior instalado.
- Pip atualizado.

### ⚙️ Passos para rodar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```


Instale as dependências:

```bash
pip install fastapi uvicorn python-multipart
```
Execute o servidor de desenvolvimento:

```bash
uvicorn main:app --reload
```
Acesse o Swagger Docs:

http://127.0.0.1:8000/docs 📄
http://127.0.0.1:8000/redoc 📚

## 📜 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

