from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

nomes = {
    1: {"name": "Jorge"},
    2: {"name": "Bruna"},
    3: {"name": "João"},
    4: {"name": "Alfredo"}
}

@app.get("/")
def home():
    return "Python API! See all endpoints in /docs"

@app.get("/api/v1/nomes")
def get_names():
    return nomes

@app.get("/api/v1/nomes/{id_nome}")
def get_name(id_nome: int):
    if id_nome not in nomes:
        raise HTTPException(status_code=404, detail="Nome não encontrado")
    return nomes[id_nome]

@app.post("/api/v1/nomes/")
def create_name(nome: str = Body(...)):
    new_id = max(nomes.keys()) + 1
    nomes[new_id] = {"name": nome}
    return {"id_nome": new_id, "name": nome}

@app.delete("/api/v1/nomes/{id_nome}")
def delete_name(id_nome: int):
    if id_nome not in nomes:
        raise HTTPException(status_code=404, detail="Nome não encontrado")
    del nomes[id_nome]
    return {"message": "Nome deletado com sucesso"}

@app.put("/api/v1/nomes/{id_nome}")
def update_name(id_nome: int, nome: str = Body(...)):
    if id_nome not in nomes:
        raise HTTPException(status_code=404, detail="Nome não encontrado")
    nomes[id_nome]["name"] = nome
    return {"id_nome": id_nome, "name": nome}
