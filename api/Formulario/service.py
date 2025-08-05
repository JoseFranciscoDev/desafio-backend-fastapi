from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from typing import Optional
from api._database.models import Formulario, Pergunta
from api._shared.schemas import FormularioCreate


def create_formulario_service(db: Session, formulario: FormularioCreate):
    perguntas_data = formulario.perguntas
    new_formulario = Formulario(
        titulo=formulario.titulo,
        descricao=formulario.descricao,
        ordem=formulario.ordem,
    )

    if perguntas_data:
        new_formulario.perguntas = [Pergunta(**p.dict()) for p in perguntas_data]
    db.add(new_formulario)
    db.commit()
    db.refresh(new_formulario)
    return new_formulario


def list_formularios_service(
    db: Session,
    titulo: Optional[str],
    descricao: Optional[str],
    ordem: Optional[int],
    sort_by: str,
    sort_order: str,
    skip: int,
    limit: int,
):
    query = db.query(Formulario)

    if titulo:
        query = query.filter(Formulario.titulo.ilike(f"%{titulo}%"))
    if descricao:
        query = query.filter(Formulario.descricao.ilike(f"%{descricao}%"))
    if ordem:
        query = query.filter(Formulario.ordem == ordem)

    sort_column = getattr(Formulario, sort_by, Formulario.id)
    if sort_order.lower() == "desc":
        query = query.order_by(desc(sort_column))
    else:
        query = query.order_by(asc(sort_column))

    return query.offset(skip).limit(limit).all()


def list_perguntas_service(
    db: Session, formulario_id: int, tipo: Optional[str], obrigatoria: Optional[bool], skip: int, limit: int
):
    query = db.query(Pergunta).filter(Pergunta.id_formulario == formulario_id)

    if tipo:
        query = query.filter(Pergunta.tipo_pergunta == tipo)
    if obrigatoria is not None:
        query = query.filter(Pergunta.obrigatoria == obrigatoria)

    return query.offset(skip).limit(limit).all()
