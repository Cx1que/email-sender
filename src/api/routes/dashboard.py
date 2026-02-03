from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.application.services.dashboard_service import DashboardService
from src.infra.database.connection import get_db

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/")
def dashboard(db: Session = Depends(get_db)):
    service = DashboardService(db)
    return service.resumo()
