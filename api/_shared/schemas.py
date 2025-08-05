from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from enum import Enum


class EnumTipoPergunta(str, Enum):
    SIM_NAO = "SIM_NAO"
    MULTIPLA_ESCOLHA = "MULTIPLA_ESCOLHA"
    UNICA_ESCOLHA = "UNICA_ESCOLHA"
    TEXTO_LIVRE = "TEXTO_LIVRE"
    INTEIRO = "INTEIRO"
    NUMERO_DECIMAL = "NUMERO_DECIMAL"


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int


class PerguntaCreate(BaseModel):
    titulo: str
    codigo: Optional[str] = None
    orientacao_resposta: Optional[str] = None
    ordem: Optional[int] = 0
    obrigatoria: Optional[bool] = False
    sub_pergunta: Optional[bool] = False
    tipo_pergunta: Optional[EnumTipoPergunta] = EnumTipoPergunta.TEXTO_LIVRE


class FormularioCreate(BaseModel):
    titulo: str
    descricao: Optional[str]
    ordem: int
    perguntas: Optional[List[PerguntaCreate]] = Field(default_factory=list)


class FormularioResponse(BaseModel):
    titulo: str
    descricao: str
    ordem: int
    perguntas: List[PerguntaCreate]


class PerguntaResponse(BaseModel):
    titulo: str
    codigo: str
    orientacao_resposta: str
    ordem: int
    obrigatoria: bool
    sub_pergunta: bool
    tipo_pergunta: EnumTipoPergunta


class UserSchema(BaseModel):
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    email: EmailStr


class PerguntaCreate(BaseModel):
    titulo: str
    codigo: Optional[str] = None
    orientacao_resposta: Optional[str] = None
    ordem: Optional[int] = 0
    obrigatoria: Optional[bool] = False
    sub_pergunta: Optional[bool] = False
    tipo_pergunta: Optional[EnumTipoPergunta] = EnumTipoPergunta.TEXTO_LIVRE


class Token(BaseModel):
    token_type: str
    acess_token: str
