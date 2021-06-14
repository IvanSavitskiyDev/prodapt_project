from typing import Dict, Any
from decimal import Decimal

from .base_provider import BaseBankProvider


class ThirdBankProvider(BaseBankProvider):
    date_format: str = "%d %b %Y"
    data_schema: Dict[str, str] = {
        "timestamp": "date_readable",
        "transaction_type": "type",
        "from": "from",
        "to": "to",
    }

    @staticmethod
    def _get_amount(line: Dict[str, Any]) -> Decimal:
        """
        Find amount value for specific bank providers
        """
        euro = Decimal(line["euro"])
        cents = Decimal(line["cents"]) / 100
        return euro + cents
