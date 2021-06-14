from typing import Dict, Any
from decimal import Decimal

from .base_provider import BaseBankProvider


class FirstBankProvider(BaseBankProvider):
    date_format: str = "%b %d %Y"
    data_schema: Dict[str, str] = {
        "timestamp": "timestamp",
        "transaction_type": "type",
        "amount": "amount",
        "from": "from",
        "to": "to",
    }

    @staticmethod
    def _get_amount(line: Dict[str, Any]) -> Decimal:
        return line["amount"]
