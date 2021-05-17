from typing import Dict


def present_value(data: Dict, rate: float):
    return data["amount"] * (1 + rate) ** (-data["t"])
