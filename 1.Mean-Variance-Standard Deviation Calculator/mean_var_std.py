import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        a = np.array(list).reshape(3, 3)

    mean = [(a.mean(axis=0).tolist()), (a.mean(axis=1).tolist()),
            (a.flatten().mean())]

    var = [(a.var(axis=0).tolist()), (a.var(axis=1).tolist()),
           (a.flatten().var())]

    std = [(a.std(axis=0).tolist()), (a.std(axis=1).tolist()),
           (a.flatten().std())]

    max = [(a.max(axis=0).tolist()), (a.max(axis=1).tolist()),
           (a.flatten().max())]

    min = [(a.min(axis=0).tolist()), (a.min(axis=1).tolist()),
           (a.flatten().min())]

    sum = [(a.sum(axis=0).tolist()), (a.sum(axis=1).tolist()),
           (a.flatten().sum())]

    calculations = {
        "mean": mean,
        "variance": var,
        "standard deviation": std,
        "max": max,
        "min": min,
        "sum": sum,
    }
    return calculations