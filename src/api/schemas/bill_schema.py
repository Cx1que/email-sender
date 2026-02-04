from pydantic import BaseModel
from datetime import date
from typing import Optional
from src.domain.enums.status import Status

class BillBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    valor: float
    tipo: str
    data_vencimento: date
    total_parcelas: Optional[int] = None
    parcela_atual: Optional[int] = None
    email_notificacao: str

class BillCreate(BillBase):
    pass

class BillUpdate(BillBase):
    status: Optional[Status] = None

class BillResponse(BillBase):
    id: int
    status: Status

    class Config:
        from_attributes = True