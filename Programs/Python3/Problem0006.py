def problem0006(MaxNumber):
    SumOfSquares = 0
    TheSquareOfTheSum = 0
    for n in list(range(1,MaxNumber + 1)):
        SumOfSquares += (n ** 2)
        TheSquareOfTheSum += n
    answer = TheSquareOfTheSum ** 2 - SumOfSquares
    return answer

if __name__ == "__main__":
    assert problem0006(2) == 4
    assert problem0006(3) == 22
    assert problem0006(4) == 70
    assert problem0006(5) == 170
    assert problem0006(6) == 350
    assert problem0006(7) == 644
    assert problem0006(8) == 1092
    assert problem0006(9) == 1740
    assert problem0006(10) == 2640
    print(problem0006((100)))