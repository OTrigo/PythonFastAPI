from fastapi import FastAPI

app = FastAPI()

nomes = {
  1:{"name": "Jorge"},
  2:{"name": "Bruna"},
  3:{"name": "João"},
  4: {"name": "Alfredo"}
}

@app.get("/")
def home():
  return "Python API! See all endpoints in /docs"

@app.get("/api/v1/nomes")
def get_nomes():
  return nomes

@app.get("/api/v1/nomes/{id_nome}")
def get_nome(id_nome: int):
  return nomes[id_nome]