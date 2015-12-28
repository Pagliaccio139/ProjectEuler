def problem0007(Number):
    return primes(Number)

def primes(number):
    primes = [2]
    counter = 2
    while number > len(primes):
        if primeChecker(counter,primes):
            primes.append(counter)
        counter += 1
    return primes[len(primes) - 1]
def primeChecker(candidate,primeList):
    for p in primeList:
        if candidate % p == 0:
            return False
    return True

if __name__ == "__main__":
    assert problem0007(1) == 2
    assert problem0007(2) == 3
    assert problem0007(3) == 5
    assert problem0007(4) == 7
    assert problem0007(5) == 11
    assert problem0007(6) == 13
    assert problem0007(7) == 17
    assert problem0007(8) == 19
    assert problem0007(9) == 23
    assert problem0007(10) == 29
    print(problem0007(10001))