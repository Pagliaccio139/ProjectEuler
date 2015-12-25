def problem0005(MaxValue):
    print(MaxValue)
    base = 1
    if MaxValue == 1:
        return base
    primeList = primes(MaxValue)
    for p in primeList:
        base *= p
    counter = 1
    while True:
        answer = base * counter
        if checker(answer,MaxValue):
            return answer
        else:
            counter += 1

def checker(candidate,MaxValue):
    for n in list(range(2,MaxValue + 1,1)):
        if candidate % n != 0:
            return False
    return True

def primes(UpperLimit):
    primes = [2]
    candidate = list(range(2,UpperLimit + 1,1))
    while primes[len(primes) - 1] ** 2 <= UpperLimit ** 2:
        for n in candidate:
            for p in primes:
                if n % p == 0:
                    candidate.remove(n)
        if candidate != []:
            primes.append(candidate[0])
        else:
            return primes


if __name__ == "__main__":
    assert problem0005(1) == 1
    assert problem0005(2) == 2
    assert problem0005(3) == 6
    assert problem0005(4) == 12
    assert problem0005(5) == 60
    assert problem0005(10) == 2520
    print(problem0005(20))