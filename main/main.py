import csv
import os

from typing import Dict, List, Union

from providers.first_bank_provider import FirstBankProvider
from providers.second_bank_provider import SecondBankProvider
from providers.third_bank_provider import ThirdBankProvider


# for each bank document, we have our own provider who parses the data for this particular bank
BANKS_PROVIDERS_DISPATCHER = {
    "bank1.csv": FirstBankProvider,
    "bank2.csv": SecondBankProvider,
    "bank3.csv": ThirdBankProvider,
}


def main(directory: str) -> List[Dict[str, Union[str, List[Dict[str, str]]]]]:
    """
    Main function, here we parse all bank files from directory and convert them into one .csv file
    """
    entries = os.listdir(directory)

    output = []

    # data parsing into list of dicts
    for entry in entries:
        full_path = os.path.join(directory, entry)
        with open(full_path, "r") as f_obj:

            if entry not in BANKS_PROVIDERS_DISPATCHER:
                raise ValueError(f"Can not find provider for bank {f_obj.name}")
            else:
                # here we guarantee that the structure of a
                # specific bank file corresponds to the class written for it
                result = BANKS_PROVIDERS_DISPATCHER[entry].do(file_object=f_obj)
                output += result

    # write structured data into new .csv file

    # csv header
    fieldnames = ["timestamp", "transaction_type", "amount", "from", "to"]

    # csv creating
    with open("output.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output)

    return output


if __name__ == "__main__":
    main(directory="csv_files/")
