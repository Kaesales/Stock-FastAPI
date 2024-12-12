from typing import List

from fastapi import FastAPI, Form, HTTPException

app = FastAPI()

# Armazenamento de produtos em memória (usando lista)
products = []
@app.get("/")  # Define a rota para a raiz
async def read_root():
    return {"message": "Estoque de produtos"}

#  Listar todos os produtos
@app.get("/products") #É um decorator, que é usado para associar uma função a uma rota HTTP no aplicativo. Nesse caso, essa rota aceita apenas requisicoes do tipo get
async def list_products():
    """
    Listar todos os produtos cadastrados.
    """
    return {
        "status": "success",
        "message": "Products retrieved successfully.",
        "data": products
    }

# Buscar produto por ID
@app.get("/products/{product_id}")
async def get_product_by_id(product_id: int):
    """
    Retorna um produto pelo seu ID.
    """
    for product in products:
        if product["id"] == product_id:
            return {
                "status": "success",
                "message": "Product retrieved successfully.",
                "data": product
            }
    raise HTTPException(status_code=404, detail="Product not found.")

#  Adicionar novo produto
@app.post("/products")
async def create_product(
    name: str = Form(...),  # '...' é uma forma de dizer que o campo é obrigatório. 
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...)
):
    """
    Adicionar um novo produto.
    """
    product_id = products[-1]["id"] + 1 if products else 1  # O índice negativo -1 representa o último item (em Python, índices negativos percorrem a lista de trás para frente).
    product = {
        "id": product_id,
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }
    products.append(product)
    return {
        "status": "success",
        "message": "Product added successfully.",
        "data": product
    }

#  Atualizar um produto existente
@app.put("/products/{product_id}")
async def update_product(
    product_id: int,
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...)
):
    """
    Atualizar um produto pelo ID.
    """
    for product in products:
        if product["id"] == product_id:
            product.update({
                "name": name,
                "description": description,
                "price": price,
                "stock": stock
            })
            return {
                "status": "success",
                "message": "Product updated successfully.",
                "data": product
            }
    raise HTTPException(status_code=404, detail="Product not found.")

# Remover um produto
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """
    Remover um produto pelo ID.
    """
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index) # o metodo pop remove e retorna o valor removido
            return {
                "status": "success",
                "message": "Product deleted successfully.",
                "data": deleted_product
            }
    raise HTTPException(status_code=404, detail="Product not found.")
