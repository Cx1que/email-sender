import smtplib
from email.message import EmailMessage
from src.config.settings import EMAIL_HOST, EMAIL_USER, EMAIL_PASS
from src.config.logger import get_logger

logger = get_logger(__name__)

class SmtpEmailService:
    def send(self, to, subject, body):
        logger.info(f"Enviando e-mail para {to} | Assunto: {subject}")
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = to
        msg.set_content(body)

        with smtplib.SMTP_SSL(EMAIL_HOST, 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            logger.info("E-mail enviado com sucesso")