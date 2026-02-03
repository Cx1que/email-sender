from src.application.check_due_bills import CheckDueBills
from src.infra.repositories.bill_repository import BillRepository
from src.infra.email.smtp_email_service import SmtpEmailService
from src.infra.database.connection import SessionLocal
from src.config.logger import get_logger

logger = get_logger(__name__)

def main():
    db = SessionLocal()
    try:
        logger.info("Iniciando scheduler de contas")

        repo = BillRepository(db)
        email_service = SmtpEmailService()
        checker = CheckDueBills(repo, email_service)

        checker.execute()
    finally:
        db.close_all()
    
    logger.info("Finalizando scheduler")

if __name__ == "__main__":
    main()
