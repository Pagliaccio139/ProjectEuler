def problem0001(MaxNumber):
    answer = 0
    for n in list(range(1,MaxNumber)):
        if (n % 3 == 0) or (n % 5 == 0):
            answer += n
    return answer

if __name__ == "__main__":
    assert problem0001(3) == 0
    assert problem0001(4) == 3
    assert problem0001(5) == 3
    assert problem0001(6) == 8
    assert problem0001(7) == 14
    assert problem0001(9) == 14
    assert problem0001(10) == 23
    print(problem0001(1000))