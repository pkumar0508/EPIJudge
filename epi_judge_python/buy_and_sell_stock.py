from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    low = prices[0]
    profit = 0.0

    for price in prices:
        if price < low:
            low = price

        potential = price - low
        if profit < potential:
            profit = potential

    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
