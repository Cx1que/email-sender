import smtplib
import ssl
from email.message import EmailMessage
from src.config.settings import EMAIL_HOST, EMAIL_USER, EMAIL_PASS
from src.config.logger import get_logger

logger = get_logger(__name__)

class SmtpEmailService:
    def send(self, to, subject, body):
        logger.info(f"📨 Iniciando processo de envio para {to}")

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = to
        msg.set_content(body)

        try:
            context = ssl.create_default_context()
            
            logger.info(f"🔌 Conectando ao host {EMAIL_HOST} via SSL na porta 465...")
            
            with smtplib.SMTP_SSL(EMAIL_HOST, 465, context=context, timeout=30) as smtp:
                logger.info("🔐 Autenticando...")
                smtp.login(EMAIL_USER, EMAIL_PASS)
                
                logger.info("📤 Enviando mensagem...")
                smtp.send_message(msg)
            
            logger.info("✅ E-mail enviado com sucesso!")

        except smtplib.SMTPAuthenticationError:
            logger.error("❌ Erro de Autenticação: Verifique se a 'Senha de App' está correta.")
            raise
        except Exception as e:
            logger.error(f"❌ Falha crítica no envio: {str(e)}")
            raise