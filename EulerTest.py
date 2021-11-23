from Euclides import Euclides
from PowBin import PowBin


class EulerTest:

    @staticmethod
    def eulerTest(a, p):
        result = PowBin.powBinMod(a, int((p - 1) / 2), p)
        if 1 == result: return True
        else: return False

    @staticmethod
    def legendre(a, p):
        return PowBin.powBinMod(a, int((p - 1) / 2), p)

    @staticmethod
    def squareMod(a, p):
        result = PowBin.powBinMod(a, int((p + 1)/4), p)
        return result, Euclides.getInv(result, p)

    @staticmethod
    def squareModField(a, p):
        return PowBin.powBinMod(a, int((p + 1) / 4), p)