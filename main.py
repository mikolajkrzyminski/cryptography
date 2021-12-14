from PowBin import PowBin
from Euclides import Euclides
from FermatTest import FermatTest
from EulerTest import EulerTest
from RSA.RSA import RSA
from CryptoAlg.EllipticCurve import EllipticCurve, EllipticPoint
from proj3.ByteNumber import ByteNumber
if __name__ == '__main__':

    f = ByteNumber(int('10011110', 2))

    g = ByteNumber(int("00011001", 2))

    print("f: " + f.toBinaryString())
    print("g: " + g.toBinaryString())
    print("f * g: " + (f * g).toBinaryString())
    #print(f.xTime(0).toBinaryString())