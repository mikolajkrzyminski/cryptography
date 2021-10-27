class PowBin:

    @staticmethod
    def powBinMod(a, x, n):
        y = 1
        i = x.bit_length()
        while i > 0:
            if (x & 1) == 1:
                y = (y * a) % n
            a = (a ** 2) % n
            x = x >> 1
            i = i - 1
        return y

    @staticmethod
    def powBin(a, x):
        y = 1
        i = x.bit_length() - 1
        while i >= 0:
            if (x & 1) == 1:
                y = (y * a)
            a = (a ** 2)
            x = x >> 1
            i = i - 1
        return y