import math
import random
import scipy.stats as stats

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

def getMM(n: int, K: int, cArr, bArr):
    v = bArr[0:K]
    a = [0.0] * n
    for i in range(n):
        s = math.floor(cArr[i] * K)
        a[i] = v[s]
        v[s] = bArr[i+K]
    return a

def pirson(L: int, checkedArr, epsilon: float):
    bins = [0] * L
    step = 1 / L
    for i in checkedArr:
        bins[int(i // step)] += 1
    criticalValue = stats.chi2.ppf(1 - epsilon, L)
    x = 0.0
    avg = float(n / L)
    for i in range(L):
        x += ((bins[i] - avg) ** 2) / avg
    return x < criticalValue

def getCriticalDK(n: int, epsilon:float):
    if(epsilon != 0.05):
        raise ValueError("epsilon must be 0.05!")
    return 1.36 / math.sqrt(n) # hardcoded :(

def Kolmogorov(checkedArr, epsilon: float):
    sortedArr = sorted(checkedArr)
    D = 0.0
    for i, j in enumerate(sortedArr):
        data_driven = float(i) / len(sortedArr)
        ideal = j # Равномерное расспределение
        D = max(D, abs(data_driven - ideal))
    return D < getCriticalDK(len(sortedArr), epsilon)
    


if __name__ == "__main__":
    a_0 = 79507
    beta = 79507
    module = 2147483648
    n = 1000
    K = 64
    CB = getCB(n, beta, module, a_0)
    print("CB: ", CB)
    MM = getMM(n, K, getCB(n+K, beta, module, a_0), [random.random() for i in range(n+K)])
    print("MM: ", MM)
    epsilon = 0.05
    print("check CB by pirson has", "passed" if pirson(100, CB, epsilon) else "failed")
    print("check MM by pirson has", "passed" if pirson(100, MM, epsilon) else "failed")
    print("check CB by Kolmogorov has", "passed" if Kolmogorov(CB, epsilon) else "failed")
    print("check MM by Kolmogorov has", "passed" if Kolmogorov(MM, epsilon) else "failed")
