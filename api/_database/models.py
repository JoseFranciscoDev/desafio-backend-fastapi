from typing import List, Optional
from sqlalchemy import ForeignKey, String, Boolean, Integer, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from enum import Enum as PyEnum


class Base(DeclarativeBase):
    pass


class EnumTipoPergunta(PyEnum):
    SIM_NAO = "SIM_NAO"
    MULTIPLA_ESCOLHA = "MULTIPLA_ESCOLHA"
    UNICA_ESCOLHA = "UNICA_ESCOLHA"
    TEXTO_LIVRE = "TEXTO_LIVRE"
    INTEIRO = "INTEIRO"
    NUMERO_DECIMAL = "NUMERO_DECIMAL"


class Formulario(Base):
    __tablename__ = "formulario"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[Optional[str]] = mapped_column(String(255))
    ordem: Mapped[int]

    perguntas: Mapped[List["Pergunta"]] = relationship("Pergunta", back_populates="formulario")

    def __repr__(self):
        return f"<Formulario(id={self.id}, titulo={self.titulo})>"


class Pergunta(Base):
    __tablename__ = "pergunta"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_formulario: Mapped[int] = mapped_column(ForeignKey("formulario.id"))
    formulario: Mapped["Formulario"] = relationship("Formulario", back_populates="perguntas")

    titulo: Mapped[str] = mapped_column(String(255))
    codigo: Mapped[Optional[str]] = mapped_column(String(50))
    orientacao_resposta: Mapped[Optional[str]] = mapped_column(String(255))
    ordem: Mapped[int]
    obrigatoria: Mapped[bool] = mapped_column(Boolean, default=False)
    sub_pergunta: Mapped[bool] = mapped_column(Boolean, default=False)
    tipo_pergunta: Mapped[EnumTipoPergunta] = mapped_column(Enum(EnumTipoPergunta))

    opcoes_respostas: Mapped[List["OpcoesResposta"]] = relationship("OpcoesResposta", back_populates="pergunta")

    def __repr__(self):
        return f"<Pergunta(id={self.id}, titulo={self.titulo})>"


class OpcoesResposta(Base):
    __tablename__ = "opcoes_respostas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_pergunta: Mapped[int] = mapped_column(ForeignKey("pergunta.id"))
    pergunta: Mapped["Pergunta"] = relationship("Pergunta", back_populates="opcoes_respostas")

    resposta: Mapped[str] = mapped_column(String(255))
    ordem: Mapped[int]
    resposta_aberta: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f"<OpcoesResposta(id={self.id}, resposta={self.resposta})>"


class OpcoesRespostaPergunta(Base):
    __tablename__ = "opcoes_resposta_pergunta"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_opcao_resposta: Mapped[int] = mapped_column(ForeignKey("opcoes_respostas.id"))
    id_pergunta: Mapped[int] = mapped_column(ForeignKey("pergunta.id"))

    def __repr__(self):
        return f"<OpcoesRespostaPergunta(id_opcao_resposta={self.id_opcao_resposta}, id_pergunta={self.id_pergunta})>"
