import time
def problem0009(Value):
    a = 1
    b = 2
    c = 3
    while True:
        if ((a ** 2) + (b ** 2) == (c ** 2)) and (a + b + c) == Value:
            return a*b*c
        if (c - b) == 1 and (b - a) == 1:
            c += 1
            b = 2
            a = 1
        elif (c - b) != 1 and (b - a) == 1:
            b += 1
            a = 1
        else:
            a += 1
if __name__ == "__main__":
    assert problem0009(12) == 60
    start = time.time()
    print(problem0009(1000))
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")