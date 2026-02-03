import smtplib
from email.message import EmailMessage
from src.config.settings import EMAIL_HOST, EMAIL_USER, EMAIL_PASS
from src.config.logger import get_logger

logger = get_logger(__name__)

class SmtpEmailService:
    def send(self, to, subject, body):
        logger.info(f"📨 Enviando e-mail para {to} | Assunto: {subject}")

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = to
        msg.set_content(body)

        try:
            smtp = smtplib.SMTP(timeout=30)
            
            smtp.connect(EMAIL_HOST, 587)
            
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            smtp.quit()
            
            logger.info("✅ E-mail enviado com sucesso")
            
        except smtplib.SMTPServerDisconnected:
            logger.error("❌ O servidor SMTP desconectou inesperadamente. Verifique se o IP do GitHub não foi bloqueado.")
            raise
        except Exception as e:
            logger.error(f"❌ Falha ao enviar e-mail: {str(e)}")
            raise