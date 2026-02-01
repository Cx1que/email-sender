from config.logger import get_logger
from datetime import date

logger = get_logger(__name__)

class CheckDueBills:
    def __init__(self, bill_repository, email_service):
        self.bill_repository = bill_repository
        self.email_service = email_service
    
    def execute(self):
        today = date.today()
        logger.info(f"Data atual: {today}")

        for bill in self.bill_repository.get_all():
            logger.info(
            f"Conta '{bill.name}' | Vencimento: {bill.due_date}"
        )

            if bill.is_due_in_days(today, 3):
                logger.info(f"Enviando AVISO para {bill.name}")
                self.email_service.send(
                    bill.email,
                    f"Lembrete: {bill.name} vence em 3 dias",
                    f"A conta {bill.name} vence em {bill.due_date.strftime('%d/%m/%y')}"
                )
            
            elif bill.is_due_today(today):
                logger.info(f"Enviando LEMBRETE para {bill.name}")
                self.email_service.send(
                    bill.email,
                    f"Lembrete: pagar {bill.name}",
                    f"A conta {bill.name} vence hoje."
                )
            else:
                logger.info(f"Nenhum envio para {bill.name}")