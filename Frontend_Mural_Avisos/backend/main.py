
from datetime import datetime

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from models import AvisoEntrada, AvisoSaida

app = FastAPI(
    title="Mural de Avisos Acadêmicos",
    description="API para publicação e consulta de avisos acadêmicos",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

avisos: list[dict] = []


@app.get("/api/avisos", response_model=list[AvisoSaida])
def listar_avisos():
    return avisos


@app.post(
    "/api/avisos",
    response_model=AvisoSaida,
    status_code=status.HTTP_201_CREATED,
)
def publicar_aviso(aviso: AvisoEntrada):
    novo_aviso = aviso.model_dump()
    novo_aviso["id"] = len(avisos) + 1
    novo_aviso["publicado_em"] = datetime.now()

    avisos.append(novo_aviso)
    return novo_aviso

from datetime import datetime
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from models import AvisoEntrada, AvisoSaida

app = FastAPI(
    title="Mural de Avisos Acadêmicos",
    description="API para publicação de avisos acadêmicos",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

avisos: list[AvisoSaida] = []


@app.get("/api/avisos", response_model=list[AvisoSaida])
def listar_avisos():
    return avisos


@app.post(
    "/api/avisos",
    response_model=AvisoSaida,
    status_code=status.HTTP_201_CREATED,
)
def publicar_aviso(dados: AvisoEntrada):
    novo_aviso = AvisoSaida(
        **dados.model_dump(),
        id=len(avisos) + 1,
        publicado_em=datetime.now(),
    )

    avisos.append(novo_aviso)
    return novo_aviso
