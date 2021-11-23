import copy
import sys

from PowBin import PowBin
from Euclides import Euclides
from FermatTest import FermatTest
from EulerTest import EulerTest
from RSA.RSA import RSA
from CryptoAlg.EllipticCurve import EllipticCurve, EllipticPoint

if __name__ == '__main__':
    # print(EllipticalCurves.getEllipticalCurve(1000))
    A, B, p = 0, 1, 7
    eCurve = EllipticCurve(A, B, p)

    P = EllipticPoint(19, 5, eCurve)
    Q = EllipticPoint(2, 4, eCurve)
    R = EllipticPoint(6, 0, eCurve)
    O = EllipticPoint("inf", "inf", eCurve)
    #print(Q.invPoint())
    #print(R + O)
    #print(P + Q)
    #print(P + P)
    pointSet = set()
    for i in range(1000):
        pointSet.add(eCurve.getRandomEllipticPoint())
    print(pointSet)
    # for i in range(100):
    #     print(P.nMultiple(i + 1))
