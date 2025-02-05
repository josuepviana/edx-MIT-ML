def get_sum_metrics(predictions, metrics=None):
    #inicia metrics como lista vazia
    if metrics is None:
        metrics = []

    for i in range(3):
        metrics.append(lambda x, i=i: x + i)

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)

    return sum_metrics


def main():
    print(get_sum_metrics(0))  # 3
    print(get_sum_metrics(1))  # 6
    print(get_sum_metrics(2))  # 9
    print(get_sum_metrics(3, [lambda x: x]))  # 15
    print(get_sum_metrics(0))  # 3
    print(get_sum_metrics(1))  # 6
    print(get_sum_metrics(2))  # 9
