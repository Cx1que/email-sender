from src.infra.database.connection import engine
from src.infra.database.base import Base

from src.domain.models.bill import Bill

Base.metadata.create_all(bind=engine)

print("Banco criado com sucesso")
