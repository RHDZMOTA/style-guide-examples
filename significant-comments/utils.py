import logging
from typing import List

logger = logging.getLogger(__name__)


class CashFlow:

    def __init__(self, amount: float, t: int):
        self.amount = amount
        self.t = t

    def present_value(self, rate: float) -> float:
        return self.amount * (1 + rate) ** (-self.t)


def net_present_value(cashflows: List[CashFlow], rate: float) -> float:
    return sum([cf.present_value(rate=rate) for cf in cashflows])
