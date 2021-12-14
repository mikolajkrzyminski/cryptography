import copy


class ByteNumber:

    # decimal number
    def __init__(self, number):
        self.number = number

    @staticmethod
    def hexToBinaryString(hex_code):
        bin_code = bin(hex_code)[2:]
        padding = (8 - len(bin_code) % 8) % 8
        return '0' * padding + bin_code

    @staticmethod
    def hexToInt(hex_code):
        bin_code = bin(hex_code)[2:]
        padding = (8 - len(bin_code) % 8) % 8
        return int('0' * padding + bin_code, 2)

    def toBinaryString(self):
        bin_code = bin(self.number)[2:]
        padding = (8 - len(bin_code) % 8) % 8
        return '0' * padding + bin_code

    def __add__(self, other):
        return ByteNumber(int(self.toBinaryString(), 2) ^ int(other.toBinaryString(), 2))

    def xTime(self, n):
        resultNumber = self
        for i in range(n):
            if resultNumber.toBinaryString()[0] == '0':
                tempNum = resultNumber.number << 1
                binString = ByteNumber(tempNum).toBinaryString()
                resultNumber = ByteNumber(int(binString, 2))
            else:
                resultInt = ByteNumber(int(bin(resultNumber.number << 1)[3:], 2)) + ByteNumber(int("1B", 16))
                resultNumber = resultInt
        return resultNumber

    def __mul__(self, other):
        resultNumber = None
        for i in range(len(other.toBinaryString())):
            if '1' == (other.toBinaryString()[i]):
                xTimeRes = self.xTime(len(other.toBinaryString()) - (i + 1))
                if None != resultNumber:
                    resultNumber = resultNumber + xTimeRes
                else:
                    resultNumber = xTimeRes
        return resultNumber

    @staticmethod
    def odwrotnosc():
        pass
