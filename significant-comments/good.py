import json
from typing import List

from utils import CashFlow, net_present_value


def get_flows_from_file(path: str) -> List[CashFlow]:
    # Validate if the file is has json ending.
    if not path.endswith(".json"):
        raise ValueError(f"File should be a json: {path}")
    with open(path, "r") as file:
        content = file.read()
    list_of_kwargs = json.loads(content)
    # Validate if the list_of_kwargs is a list
    if not isinstance(list_of_kwargs, list):
        raise ValueError(f"File content should be a list: {path}")
    return [CashFlow(**kwargs) for kwargs in list_of_kwargs]


if __name__ == "__main__":
    cashflow_list = get_flows_from_file(path="cashflow_list.json")
    npv = net_present_value(cashflows=cashflow_list)
