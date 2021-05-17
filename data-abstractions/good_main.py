from good_abstraction import CashFlow

cashflow_0 = CashFlow(amount=-1000, t=0)
cashflow_1 = CashFlow(amount=2000, t=5)


if __name__ == "__main__":
    rate = 0.08
    net_present_value = 0
    for cf in [cashflow_0, cashflow_1]:
        net_present_value += cf.present_value(rate=rate)
    print("Net Present Value:", net_present_value)
