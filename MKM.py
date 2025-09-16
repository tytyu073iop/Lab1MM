import math

def modM(value, module):
    return value - module * math.trunc(value / module)

def getCB(n: int, beta: float, module: int, a_0: int):
    if (a_0 >= module):
        raise ValueError("a_0 should be less than module")
    a = [0.0] * (n - 1)
    aStar = [0.0] * n
    aStar[0] = float(a_0)
    for i in range(1, n):
        aStar[i] = modM(beta * aStar[i - 1], module)
        a[i - 1] = aStar[i] / module
    return a

def getLSF(n: int, p: int, c: int, betaArr, aArr):
    if ():
        raise ValueError("")
    a = [0.0] * (n - 1)
    aStar = [0.0] * n
    aStar[0] = float(a_0)
    for i in range(1, n):
        aStar[i] = modM(beta * aStar[i - 1], module)
        a[i - 1] = aStar[i] / module
    return a

# def getMM(n: int, beta: float, module: int, a_0: int):


if __name__ == "__main__":
    a_0 = 79507
    beta = 79507
    module = 2147483648
    n = 1000
    print(getCB(n, beta, module, a_0))
