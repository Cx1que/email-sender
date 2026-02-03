from datetime import date, timedelta
from src.config.logger import get_logger

logger = get_logger(__name__)

class CheckDueBills:
    def __init__(self, bill_repository, email_service):
        self.bill_repository = bill_repository
        self.email_service = email_service

    def execute(self):
        today = date.today()
        logger.info(f"📅 Data atual: {today}")

        bills = self.bill_repository.listar_contas_ativas()

        for bill in bills:
            logger.info(
                f"🔍 Conta: {bill.nome} | Tipo: {bill.tipo} | Vencimento: {bill.data_vencimento}"
            )

            self._process_bill(bill, today)

    def _process_bill(self, bill, today: date):
        if bill.tipo == "AVULSA":
            self._process_avulsa(bill, today)

        elif bill.tipo == "RECORRENTE":
            self._process_recorrente(bill, today)

        elif bill.tipo == "PARCELADA":
            self._process_parcelada(bill, today)


    # Tipos de conta
    def _process_avulsa(self, bill, today):
        self._check_notifications(bill, today)

        if bill.data_vencimento < today:
            logger.info(f"❌ Conta avulsa vencida, desativando: {bill.nome}")
            self.bill_repository.desativar(bill.id)

    def _process_recorrente(self, bill, today):
        self._check_notifications(bill, today)

        if bill.data_vencimento < today:
            # avança para o próximo mês
            bill.data_vencimento = self._next_month(bill.data_vencimento)
            self.bill_repository.atualizar(bill)
            logger.info(f"🔁 Conta recorrente atualizada para {bill.data_vencimento}")

    def _process_parcelada(self, bill, today):
        self._check_notifications(bill, today)

        if bill.data_vencimento < today:
            bill.parcela_atual += 1

            if bill.parcela_atual > bill.total_parcelas:
                logger.info(f"✅ Parcelamento finalizado: {bill.nome}")
                self.bill_repository.desativar(bill.id)
                return

            bill.data_vencimento = self._next_month(bill.data_vencimento)
            self.bill_repository.atualizar(bill)

            logger.info(
                f"📦 Parcela {bill.parcela_atual}/{bill.total_parcelas} - Próximo vencimento: {bill.data_vencimento}"
            )

    # Notificações
    def _check_notifications(self, bill, today):
        if bill.data_vencimento - timedelta(days=3) == today:
            self._send_notice(bill)

        if bill.data_vencimento == today:
            self._send_due_date(bill)

    def _send_notice(self, bill):
        subject = "⏰ Lembrete: conta próxima do vencimento"
        body = (
            f"Olá!\n\n"
            f"A conta '{bill.nome}' vencerá em {bill.data_vencimento}.\n"
            f"Descrição: {bill.descricao}\n\n"
            f"Evite juros 🙂"
        )

        self.email_service.send(
            to=bill.email_notificacao,
            subject=subject,
            body=body
        )

    def _send_due_date(self, bill):
        subject = "🚨 Conta vence HOJE"
        body = (
            f"Atenção!\n\n"
            f"A conta '{bill.nome}' vence hoje ({bill.data_vencimento}).\n"
            f"Descrição: {bill.descricao}"
        )

        self.email_service.send(
            to=bill.email_notificacao,
            subject=subject,
            body=body
        )

    # utils
    def _next_month(self, current_date):
        if current_date.month == 12:
            return current_date.replace(year=current_date.year + 1, month=1)
        return current_date.replace(month=current_date.month + 1)
