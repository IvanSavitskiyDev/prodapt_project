import os
import shutil
import csv
from typing import List, Dict


test_input_data = [
    {
        "filename": "bank1.csv",
        "fieldnames": ["timestamp", "type", "amount", "from", "to"],
        "rows": [
            {
                "timestamp": "May 11 2020",
                "type": "remove",
                "amount": "324.21",
                "from": "184",
                "to": "134",
            },
        ],
    },
    {
        "filename": "bank2.csv",
        "fieldnames": ["date", "transaction", "amounts", "from", "to"],
        "rows": [
            {
                "date": "12-05-2020",
                "transaction": "add",
                "amounts": "41.10",
                "from": "101",
                "to": "169",
            },
        ],
    },
    {
        "filename": "bank3.csv",
        "fieldnames": ["date_readable", "type", "euro", "cents", "from", "to"],
        "rows": [
            {
                "date_readable": "13 May 2020",
                "type": "remove",
                "euro": "50",
                "cents": "1",
                "from": "204",
                "to": "184",
            },
        ],
    },
]

test_output_data = [
    {
        "timestamp": "2020-05-11",
        "transaction_type": "remove",
        "amount": "324.21",
        "from": "184",
        "to": "134",
    },
    {
        "timestamp": "2020-05-12",
        "transaction_type": "add",
        "amount": "41.10",
        "from": "101",
        "to": "169",
    },
    {
        "timestamp": "2020-05-13",
        "transaction_type": "remove",
        "amount": "50.01",
        "from": "204",
        "to": "184",
    },
]


def creating_test_files(filename, fieldnames: List, rows: List[Dict[str, str]]):
    with open("files/" + filename, "w", encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def clean(directory):
    shutil.rmtree(directory)


def test_parse_banks_data(test_data: List):
    from main.main import main

    directory = os.getcwd() + "/files/"

    # create temp folder
    os.makedirs(directory)

    # create test .csv files
    for data in test_data:
        creating_test_files(
            filename=data["filename"],
            fieldnames=data["fieldnames"],
            rows=data["rows"],
        )

    # parse data
    main(directory=directory)

    # delete temp folder
    clean(directory=directory)

    output_file = os.getcwd() + "/output.csv"

    result: List = []
    with open(output_file, "r") as f_obj:
        for line in csv.DictReader(f_obj):
            result.append(line)

    # remove test output file
    os.remove(output_file)

    assert result == test_output_data


# run test
test_parse_banks_data(test_input_data)
