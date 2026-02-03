from datetime import date, timedelta
from src.infra.repositories.bill_repository import BillRepository

class DashboardService:
    def __init__(self, db):
        self.repo = BillRepository(db)

    def resumo(self):
        hoje = date.today()

        contas = self.repo.listar_contas_ativas()

        vencidas = []
        a_vencer = []
        fixas = []
        variaveis = []

        total_vencido = 0.0
        total_mes = 0.0

        for conta in contas:
            # vencidas
            if conta.data_vencimento < hoje:
                vencidas.append(conta)
                total_vencido += getattr(conta, "valor", 0)

            # a vencer (próximos 7 dias)
            if hoje <= conta.data_vencimento <= hoje + timedelta(days=7):
                a_vencer.append(conta)

            # tipo
            if conta.tipo == "FIXA":
                fixas.append(conta)
            elif conta.tipo == "VARIAVEL":
                variaveis.append(conta)

            # resumo mensal
            if conta.data_vencimento.month == hoje.month:
                total_mes += getattr(conta, "valor", 0)

        return {
            "contas_vencidas": vencidas,
            "contas_a_vencer": a_vencer,
            "gastos_fixos": fixas,
            "gastos_variaveis": variaveis,
            "resumo": {
                "total_vencido": total_vencido,
                "total_mes": total_mes
            }
        }
