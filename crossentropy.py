from math import log

eps = 1e-15

def crossentropy(p: list[float], q: list[float]) -> float:
    """
    On average, how much bits would I need to encode a message using q
    when the message comes from a distribution p.

    information / number of bits = -log(proba)

    Args:
        p: pmf of true distribution 
        q: pmf of distribution used to encode
    
    Returns:
        cross entropy loss
    """
    return sum(x * (-log(min(y + eps, 1))) for x, y in zip(p, q))


if __name__ == "__main__":
    p = [0.0, 1.0]
    q = [0.0, 1.0]
    assert crossentropy(p, q) == 0.0

    p = [0.0, 1.0]
    q = [0.5, 0.5]
    assert crossentropy(p, q) == 0.6931471805599433