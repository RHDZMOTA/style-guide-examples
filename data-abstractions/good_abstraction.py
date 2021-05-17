
class CashFlow:

    def __init__(self, amount: float, t: int):
        self.amount = amount
        self.t = t

    def present_value(self, rate: float) -> float:
        return self.amount * (1 + rate) ** (-self.t)
