from PowBin import PowBin
from Euclides import Euclides
from FermatTest import FermatTest
from EulerTest import EulerTest
from RSA.RSA import RSA

if __name__ == '__main__':
    RSA.rsa()
    print(RSA.decrypt(RSA.encrypt()))

