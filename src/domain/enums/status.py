from enum import Enum

class Status(str, Enum):
    ABERTA = "ABERTA"
    PAGA = "PAGA"
    ATRASADA = "ATRASADA"