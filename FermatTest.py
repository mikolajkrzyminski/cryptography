import random
from PowBin import PowBin
from Euclides import Euclides

class FermatTest:

    @staticmethod
    def FermatTest(k, n):
        testedRandomValues = set()
        bitLengthRand = n.bit_length() - 1
        isPrime = True
        for i in range(k):
            while True:
                # generate random n-1 size number
                a = FermatTest.getRandomNBitsNumber(bitLengthRand - 1)
                # checks if it wasn't generate
                if a not in testedRandomValues:
                    # checks co-prime
                    if 1 == Euclides.extendEuclides(n, a)[2]:
                        testedRandomValues.add(a)
                        break
            # Fermat formula
            if 1 != PowBin.powBinMod(a, n - 1, n):
                isPrime = False
                break
        return isPrime

    @staticmethod
    def getRandomNBitsNumber(n):
        res = 1
        for i in range(n):
            bit = random.randint(0, 1)
            res = res << 1
            # if 1 generated
            if 1 == bit:
                res = res | bit
        return res


