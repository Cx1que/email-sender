from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, Enum
from src.infra.database.base import Base
from src.domain.enums.status import Status

class Bill(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    status = Column(
        Enum(Status, name="status"),
        nullable=False,
        default=Status.ABERTA
    )

    tipo = Column(String, nullable=False) # AVULSA | PARCELADA | RECORRENTE fazer ENUM
    data_vencimento = Column(Date, nullable=False)

    total_parcelas = Column(Integer)
    parcela_atual = Column(Integer)

    email_notificacao = Column(String, nullable=False)
    
    ativa = Column(Boolean, default=True)