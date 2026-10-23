
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class AvisoEntrada(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    mensagem: str = Field(min_length=10, max_length=1000)
    autor: str = Field(min_length=2, max_length=100)
    prioridade: Literal["normal", "importante"]


class AvisoSaida(AvisoEntrada):
    id: int
    publicado_em: datetime
