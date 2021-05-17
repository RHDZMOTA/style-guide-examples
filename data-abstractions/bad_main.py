from bad_abstraction import present_value


data_0 = {
    "amount": -1000,
    "t": 0
}

data_1 = {
    "amount": 2000,
    "t": 5
}

if __name__ == "__main__":
    rate = 0.08
    net_present_value = 0
    for data in [data_0, data_1]:
        net_present_value += present_value(data=data, rate=rate)
    print("Net Present Value:", net_present_value)
