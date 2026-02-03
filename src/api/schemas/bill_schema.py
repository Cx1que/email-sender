from pydantic import BaseModel
from datetime import date
from typing import Optional

class BillCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    tipo: str
    data_vencimento: date
    total_parcelas: Optional[int] = None
    parcela_atual: Optional[int] = None
    email_notificacao: str

class BillUpdate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    tipo: str
    data_vencimento: date
    total_parcelas: Optional[int] = None
    parcela_atual: Optional[int] = None
    email_notificacao: str

class BillResponse(BaseModel):
    id: int
    nome: str
    tipo: str
    descricao: Optional[str] = None
    data_vencimento: date
    total_parcelas: Optional[int] = None
    parcela_atual: Optional[int] = None
    email_notificacao: str
