import copy
import random

from Euclides import Euclides
from EulerTest import EulerTest
from FermatTest import FermatTest
from PowBin import PowBin


class EllipticCurve:

    def __init__(self, A, B, p):
        self.A = A
        self.B = B
        self.p = p

    def __eq__(self, other):
        return self.A == other.A and self.B == other.B and self.p == other.p

    def getRandomEllipticPoint(self):
        while True:
            x = random.randint(0, self.p - 1)
            fx = (PowBin.powBinMod(x, 3, self.p) + self.A * x + self.B) % self.p
            legendreResult = EulerTest.legendre(fx, self.p)
            if 1 == legendreResult or 0 == legendreResult:
                i = random.randint(0, 1)
                y = EulerTest.squareModField(fx, self.p)
                if 0 == i:
                    y = -y % self.p
                if self.checkPoint(EllipticPoint(x, y, self)): break
        return x, y

    def checkPoint(self, ePoint):
        result = (PowBin.powBinMod(ePoint.x, 3, self.p) + self.A * ePoint.x + self.B) % self.p
        return PowBin.powBinMod(ePoint.y, 2, self.p) == result

    @staticmethod
    def getEllipticCurveWithKBits(kBits):
        while True:
            prime = FermatTest.getRandomNBitsNumber(kBits)
            if FermatTest.FermatTest(50, prime): break
        pairList = []
        while True:
            A = random.randint(0, prime - 1)
            B = random.randint(0, prime - 1)
            if (A, B) not in pairList:
                pairList.append((A, B))
                deltaE = (4 * PowBin.powBinMod(A, 3, prime) + 27 * PowBin.powBinMod(B, 2, prime)) % prime
                if 0 != deltaE:
                    return EllipticCurve(A, B, prime)

    @staticmethod
    def getEllipticCurve(prime):
        pairList = []
        while True:
            A = random.randint(0, prime - 1)
            B = random.randint(0, prime - 1)
            if (A, B) not in pairList:
                pairList.append((A, B))
                deltaE = (4 * PowBin.powBinMod(A, 3, prime) + 27 * PowBin.powBinMod(B, 2, prime)) % prime
                if 0 != deltaE:
                    return EllipticCurve(A, B, prime)


class EllipticPoint:
    def __init__(self, x, y, eCurve):
        self.x = x
        self.y = y
        self.eCurve = eCurve

    # def invPoint(self):
    #     return EllipticPoint(self.x, Euclides.getInv(self.y, self.eCurve.p), self.eCurve)

    def invPoint(self):
        return EllipticPoint(self.x, -self.y % self.eCurve.p, self.eCurve)

    def isSpecialPoint(self):
        return self.x == "inf" and self.y == "inf"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.eCurve == other.eCurve

    def __add__(self, other):
        l, resultX, resultY = 0, 0, 0
        if self.x == "inf" and self.y == "inf": resultX, resultY = other.x, other.y
        elif other.x == "inf" and other.y == "inf": resultX, resultY = self.x, self.y
        elif self.x != other.x:
            l = ((other.y - self.y) * Euclides.getInv((other.x - self.x) % self.eCurve.p, self.eCurve.p)) % self.eCurve.p
            resultX = (PowBin.powBinMod(l, 2, self.eCurve.p) - self.x - other.x) % self.eCurve.p
            resultY = (l * (self.x - resultX) - self.y) % self.eCurve.p
        elif self == other:
            l = ((3 * PowBin.powBinMod(self.x, 2, self.eCurve.p) + self.eCurve.A) * Euclides.getInv(2 * self.y, self.eCurve.p)) % self.eCurve.p
            resultX = (PowBin.powBinMod(l, 2, self.eCurve.p) - 2 * self.x) % self.eCurve.p
            resultY = (l * (self.x - resultX) - self.y) % self.eCurve.p
        elif self == other.invPoint(): resultX, resultY = "inf", "inf"
        elif self.x == "inf" and self.y == "inf": resultX, resultY = other.x, other.y
        elif other.x == "inf" and other.y == "inf": resultX, resultY = self.x, self.y
        return EllipticPoint(resultX, resultY, self.eCurve)

    def __str__(self):
        if self.isSpecialPoint(): return "inf, " + "inf"
        else: return str(self.x) + ", " + str(self.y)

    def nMultiple(self, nInp):
        n = nInp
        Q = copy.deepcopy(self)
        R = EllipticPoint("inf", "inf", self.eCurve)
        while n > 0:
            if 1 == n % 2:
                R = R + Q
                n = n - 1
            Q = Q + Q
            n = n / 2
        return R
