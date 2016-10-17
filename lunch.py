# -*- coding=utf-8 -*-
def add_express(money, average_express):
    for m in money:
        money[m] = money[m] + average_express
    return money


def print_info(money):
    for m in money.items():
        print m[0] + ': ' + str(m[1])


def calculate_money(money, express, actual_cost):
    """
    :param money: Dict
    :param express: float
    :param actual_cost: float
    :return: money: List
    """
    average_express = express / len(money)
    money = add_express(money, average_express)
    total = reduce(lambda x, y: x + y, money.values())
    result = list()
    for m in money:
        money[m] = money[m] * 1.0 / total * actual_cost

    print_info(money)


money = {
    'big wei': 0,
    'dragon lady': 41,
    'two brother': 31
}


express = 5

actual_cost = 60

calculate_money(money, express, actual_cost)