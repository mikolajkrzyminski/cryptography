import random
from PowBin import PowBin
from Euclides import Euclides

class FermatTest:

    @staticmethod
    def FermatTest(k, n):
        l = set()
        bitLengthRand = n.bit_length() - 1
        isPrime = True
        for i in range(k):
            while True:
                a = FermatTest._getRandomNBits(bitLengthRand)
                if 1 == Euclides.extendEuclides(n, a)[2]:
                    if a not in l:
                        l.add(a)
                        break
            if 1 != PowBin.powBinMod(a, n - 1, n):
                isPrime = False
                break
        return isPrime

    @staticmethod
    def _getRandomNBits(n):
        res = 1
        for i in range(n):
            bit = random.randint(0, 1)
            res = res << 1
            if 1 == bit:
                res = res | bit
        return res


