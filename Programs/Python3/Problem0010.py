def problem0010(MaxValue):
    primes = prime_table(MaxValue)
    answer = 0
    for x in primes:
        answer += x
    return answer


def prime_table(n):
    list = [True for _ in range(n)]
    i = 2
    while i * i <= n:
        if list[i - 1]:
            j = i + i
            while j <= n:
                list[j - 1] = False
                j += i
        i += 1
    table = [i for i in range(n) if list[i - 1] and i >= 2]
    return table


if __name__ == "__main__":
    assert problem0010(2) == 0
    assert problem0010(3) == 2
    assert problem0010(4) == 5
    assert problem0010(5) == 5
    assert problem0010(6) == 10
    print(problem0010(2000000))
