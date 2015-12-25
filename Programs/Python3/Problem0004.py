def problem0004(digits):
    multiplicand = int("9" * digits)
    lowerLimit = (int("9" * digits) - int("9" * (digits - 1)))
    while multiplicand >= lowerLimit:
        multiplier = int("9" * digits)
        while multiplier >= lowerLimit:
            answer = str(multiplicand * multiplier)
            if answer == answer[::-1]:
                return int(answer)
            multiplier -= 1
        multiplicand -= 1
    return 0


if __name__ in "__main__":
    assert problem0004(2) == 9009
    print(problem0004(3))