from typing import List


def rolling_average(values: List, period: int) -> List:
    """
    Calculate the average of period numbers in the value, for example:
    """
    rolling_averages = []

    for i in range(period, len(values) + 1):
        average = sum(values[i - period : i]) / period
        rolling_averages.append(average)

    return rolling_averages
