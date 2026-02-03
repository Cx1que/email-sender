from sqlalchemy import Column, Integer, String, Date, Boolean
from src.infra.database.base import Base

class Bill(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

    tipo = Column(String, nullable=False) # AVULSA | PARCELADA | RECORRENTE
    data_vencimento = Column(Date, nullable=False)

    total_parcelas = Column(Integer)
    parcela_atual = Column(Integer)

    email_notificacao = Column(String, nullable=False)
    
    ativa = Column(Boolean, default=True)