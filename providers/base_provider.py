import csv

from typing import Dict, Any, List
from datetime import datetime
from decimal import Decimal


class BaseBankProvider:
    date_format: str = None
    data_schema: Dict = {}

    @classmethod
    def do(cls, file_object) -> List:
        """
        Common part for parsing data
        :param file_object: bank file
        :return:
        """
        # local_dict = {'filename': file_object.name, 'data': []}
        local_dict = []

        assert cls.date_format
        assert cls.data_schema

        for line in csv.DictReader(file_object):

            current = {}
            for map_key, map_value in cls.data_schema.items():
                current.update({map_key: line[map_value]})

            current["timestamp"] = datetime.strptime(
                current["timestamp"], cls.date_format
            ).date()

            if "amount" not in current:
                current["amount"] = cls._get_amount(line)

            else:
                current["amount"] = Decimal(current["amount"])

            current = dict(sorted(current.items()))
            local_dict.append(current)

        return local_dict

    @staticmethod
    def _get_amount(line: Dict[str, Any]) -> Decimal:
        """
        Find amount value for specific bank providers
        """
        raise NotImplementedError()
