def problem0003(Value):
    dividend = Value
    denominator = 2
    if dividend <= 1:
        return -1
    elif dividend == 2:
        return 2
    while True:
        if dividend == denominator:
            return denominator
        if dividend % denominator == 0:
            dividend = dividend / denominator
        else:
            denominator += 1


if __name__ == "__main__":
    assert problem0003(2) == 2
    assert problem0003(3) == 3
    assert problem0003(4) == 2
    assert problem0003(5) == 5
    assert problem0003(13195) == 29
    print(problem0003(600851475143))