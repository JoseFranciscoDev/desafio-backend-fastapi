from fastapi import APIRouter, Depends, Query
from typing import Optional, List
from sqlalchemy.orm import Session
from api.utils.db_services import get_db
from api.Formulario.service import list_formularios_service, create_formulario_service, list_perguntas_service
from api._shared.schemas import FormularioCreate, FormularioResponse, PerguntaResponse

router = APIRouter(prefix="/formularios", tags=["Formulários"])


@router.get("/", response_model=List[FormularioResponse])
def list_formularios(
    titulo: Optional[str] = Query(None, description="Filtrar por título"),
    descricao: Optional[str] = Query(None, description="Filtrar por descrição"),
    ordem: Optional[int] = Query(None, description="Filtrar por ordem exata"),
    sort_by: Optional[str] = Query("id", description="Campo para ordenar"),
    sort_order: Optional[str] = Query("asc", description="asc ou desc"),
    skip: int = Query(0, ge=0, description="Offset para paginação"),
    limit: int = Query(10, ge=1, le=100, description="Quantidade de itens por página"),
    db: Session = Depends(get_db),
):
    return list_formularios_service(db, titulo, descricao, ordem, sort_by, sort_order, skip, limit)


@router.post("/")
def create_formulario(formulario: FormularioCreate, db: Session = Depends(get_db)):
    return create_formulario_service(db, formulario)


@router.get("/{formulario_id}/perguntas", response_model=List[PerguntaResponse])
def get_perguntas(
    formulario_id: int,
    tipo: Optional[str] = Query(None, description="Filtrar por tipo"),
    obrigatoria: Optional[bool] = Query(None, description="Filtrar por obrigatoriedade"),
    skip: int = Query(0, ge=0, description="Offset para paginação"),
    limit: int = Query(10, ge=1, le=100, description="Quantidade de itens por página"),
    db: Session = Depends(get_db),
):
    return list_perguntas_service(db, formulario_id, tipo, obrigatoria, skip, limit)


@router.post("/{formulario_id}/perguntas", response_model=List[PerguntaResponse])
def post_perguntas(
    formulario_id: int,
    tipo: Optional[str] = Query(None, description="Filtrar por tipo"),
    obrigatoria: Optional[bool] = Query(None, description="Filtrar por obrigatoriedade"),
    skip: int = Query(0, ge=0, description="Offset para paginação"),
    limit: int = Query(10, ge=1, le=100, description="Quantidade de itens por página"),
    db: Session = Depends(get_db),
):
    return
