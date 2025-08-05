from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import routes

app = FastAPI(title="API para formulários dinâmicos")
app.include_router(routes)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status")
def status():
    return {"message": "api funcionando"}
