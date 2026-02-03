from src.infra.repositories.bill_repository import BillRepository
from src.domain.models.bill import Bill
from sqlalchemy.orm import Session
from fastapi import HTTPException

class BillService:
    def __init__(self, db: Session):
        self.repo = BillRepository(db)

    def criar(self, data):
        conta = Bill(
            nome=data.nome,
            descricao=data.descricao,
            tipo=data.tipo,
            data_vencimento=data.data_vencimento,
            total_parcelas=data.total_parcelas,
            parcela_atual=data.parcela_atual,
            email_notificacao=data.email_notificacao,
            ativa=True
        )
        return self.repo.criar(conta)

    def listar(self):
        return self.repo.listar()
    
    def listar_contas_ativas(self):
        return self.repo.listar_contas_ativas()
    
    def atualizar(self, data, bill_id: int):
        bill = self.db.query(Bill).get(bill_id)

        if not bill:
            raise ValueError("Conta não encontrada")
        
        if not bill.ativa:
            raise ValueError("Conta desativada não pode ser atualizada")

        bill.nome = data.nome
        bill.descricao = data.descricao
        bill.email_notificacao = data.email_notificacao

        return self.repo.atualizar(bill) 
    
    def desativar(self, bill_id: int):
        bill = self.repo.desativar(bill_id)

        if not bill:
            raise HTTPException(
                status_code=404,
                detail="Não encontramos a conta esperada."
            )
        return bill
    

