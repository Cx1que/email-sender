import json
from domain.bill import Bill
from config.logger import get_logger

logger = get_logger(__name__)

class JsonBillRepository:
    def __init__(self, path):
        self.path = path

    def get_all(self):
        logger.info("Carregando contas do JSON")

        with open(self.path) as f:
            data = json.load(f)

        logger.info(f"{len(data)} contas carregadas")

        return [
            Bill(item["name"], item["due_date"], item["email"])
            for item in data
        ]