from Euclides import Euclides
from PowBin import PowBin


class EulerTest:

    @staticmethod
    def eulerTest(a, p):
        result = PowBin.powBinMod(a, int((p - 1) / 2), p)
        #print("a: " + str(a) + ", p: " + str(p), end=" | ")
        if 1 == result: return True
        else: return False

    @staticmethod
    def squareMod(a, p):
        result = PowBin.powBinMod(a, int((p + 1)/4), p)
        return result, Euclides.getInv(result, p)