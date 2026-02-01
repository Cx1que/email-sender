from application.check_due_bills import CheckDueBills
from infra.storage.json_bill_repository import JsonBillRepository
from infra.email.smtp_email_service import SmtpEmailService
from config.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Iniciando verificação de contas")

    try:
        bill_repository = JsonBillRepository("data/bills.json")
        email_service = SmtpEmailService()

        use_case = CheckDueBills(
            bill_repository=bill_repository,
            email_service=email_service
        )
        use_case.execute()

        logger.info("Finalizando execução com sucesso")
        
    except Exception:
        logger.exception("Erro fatal durante execução")
        raise

if __name__ == "__main__":
    main()
