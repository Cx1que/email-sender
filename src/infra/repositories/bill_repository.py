from src.domain.models.bill import Bill
from sqlalchemy.orm import Session

class BillRepository:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, bill):
        self.db.add(bill)
        self.db.commit()
        self.db.refresh(bill)
        return bill

    def listar(self):
        return self.db.query(Bill).all()
    
    def listar_contas_ativas(self):
        return self.db.query(Bill).filter(Bill.ativa == True).all()
    
    def atualizar(self, bill: Bill):
        if not bill:
            return None
        
        self.db.commit()
        self.db.refresh(bill)
        return bill
    
    def desativar(self, bill_id: int):
        bill = self.db.query(Bill).get(bill_id)
        if not bill:
            return None
        
        bill.ativa = False
        self.db.commit()
        return bill
    
    def buscar_por_id(self, bill_id: int):
        return self.db.get(Bill, bill_id)