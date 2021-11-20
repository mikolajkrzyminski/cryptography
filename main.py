import sys

from PowBin import PowBin
from Euclides import Euclides
from FermatTest import FermatTest
from EulerTest import EulerTest
from RSA.RSA import RSA
from CryptoAlg.EllipticCurve import EllipticCurve, EllipticPoint

if __name__ == '__main__':
    # print(EllipticalCurves.getEllipticalCurve(1000))
    A, B, p = 1, 1, 7
    eCurve = EllipticCurve(A, B, p)
    # listXY = [(7,1),(7,10),(6,2),(6,9),(10,2),(10,9), (1, 3)]
    # for e in listXY:
    #    print(EllipticalCurves.checkPoint(A, B, p, e[0], e[1]))
    # setResult = set()
    # for i in range(100):
    #    x, y = EllipticalCurves.getRandomEllipticalPoint(A, B, p)
    #    setResult.add((x,y))

    # print(setResult)
    # print(EllipticalCurves.invPoint(p, 2, 1))
    # print(x, y)
    # print(EllipticalCurves.checkPoint(A, B, p, x, y))

    # print(Euclides.getInv(0, 11))

    P = EllipticPoint(2, 5, eCurve)
    Q = EllipticPoint(3, 10, eCurve)
    R = EllipticPoint(6, 0, eCurve)
    O = EllipticPoint("inf", "inf", eCurve)
    if eCurve.checkPoint(P): print(O + P)

    if eCurve.checkPoint(P): print(P.nMultiple(5))