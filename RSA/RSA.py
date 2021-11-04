from Euclides import Euclides
from FermatTest import FermatTest
from PowBin import PowBin


class RSA:
    @staticmethod
    def rsa():
        p, q = 0, 0
        while True:
            p = FermatTest.getRandomNBitsNumber(256)
            if FermatTest.FermatTest(50, p): break
        while True:
            q = FermatTest.getRandomNBitsNumber(256)
            if FermatTest.FermatTest(50, q) and p != q: break
        n = p * q
        fi = (p - 1) * (q - 1)
        e = 0
        while True:
            e = FermatTest.getRandomNBitsNumber(fi.bit_length() - 1)
            if 1 == Euclides.extendEuclides(e, fi)[2]: break
        d = Euclides.getInv(e, fi)
        pu = open("RSA\public.txt", "w")
        pu.write(str(n) + " " + str(e))
        pu.close()
        pr = open("RSA\private.txt", "w")
        pr.write(str(n) + " " + str(d))
        pr.close()

    @staticmethod
    def encrypt():
        pu = open("RSA\public.txt", "r")
        public = pu.read().split(" ")
        pu.close()
        n = int(public[0])
        e = int(public[1])
        #M = FermatTest.getRandomNBitsNumber(n.bit_length() - 1)
        M = 12345
        print(M)
        C = PowBin.powBinMod(M, e, n)
        return C

    @staticmethod
    def decrypt(C):
        pr = open("RSA\private.txt", "r")
        private = pr.read().split(" ")
        pr.close()
        n = int(private[0])
        d = int(private[1])
        M = PowBin.powBinMod(C, d, n)
        return M
