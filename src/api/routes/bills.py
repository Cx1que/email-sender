from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.api.schemas.bill_schema import BillCreate, BillResponse, BillUpdate
from src.application.services.bill_service import BillService
from src.infra.database.connection import get_db

router = APIRouter(
    prefix="/bills",
    tags=["Contas"]
)

@router.post("/", response_model=BillResponse)
def criar_conta(conta: BillCreate, db: Session = Depends(get_db)):
    service = BillService(db)
    return service.criar(conta)

@router.get("/")
def listar_contas(db: Session = Depends(get_db)):
    service = BillService(db)
    return service.listar()

@router.get("/ativas")
def listar_contas_ativas(db: Session = Depends(get_db)):
    service = BillService(db)
    return service.listar_contas_ativas()

@router.put("/{bill_id}")
def atualizar_conta(
    bill_id: int,
    data: BillUpdate,
    db: Session = Depends(get_db)
):
    service = BillService(db)
    return service.atualizar(bill_id, data)


@router.delete("/{bill_id}")
def desativar(bill_id: int, db: Session = Depends(get_db)):
    service = BillService(db)
    return service.desativar(bill_id)
