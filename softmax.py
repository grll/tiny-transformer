from math import e


def softmax(t: list[float]) -> list[float]:
    s = sum(e**i for i in t)
    return [(e**i) / s for i in t]


if __name__ == "__main__":
    from math import log

    assert softmax([log(1), log(2), log(3)]) == [1 / 6, 2 / 6, 3 / 6]
