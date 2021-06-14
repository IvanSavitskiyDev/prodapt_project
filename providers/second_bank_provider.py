from typing import Dict, Any
from decimal import Decimal

from .base_provider import BaseBankProvider


class SecondBankProvider(BaseBankProvider):
    date_format: str = "%d-%m-%Y"
    data_schema: Dict[str, str] = {
        "timestamp": "date",
        "transaction_type": "transaction",
        "amount": "amounts",
        "from": "from",
        "to": "to",
    }

    @staticmethod
    def _get_amount(line: Dict[str, Any]) -> Decimal:
        return line["amounts"]
