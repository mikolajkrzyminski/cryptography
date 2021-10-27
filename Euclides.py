import copy

#Rozszerzony algorytm Euklidesa pozwala na wyznaczenie współczynników p i q w równaniu NWD(a, b) = a·p + b·q

class Euclides:

    @staticmethod
    def euclidesNWD(aInp, bInp):
        if(aInp >= bInp):
            a = aInp
            b = bInp
        else:
            a = bInp
            b = aInp
        print(str(a) + " = ", end="")
        while True:
            t = (a - (a // b) * b)
            a = b
            b = t
            if 0 == b : break
        print(str(a))

    @staticmethod
    def extendEuclides(x, N):
        A = N
        B = x
        U = 0
        V = 1
        while True:
            q = A // B
            A_new = copy.deepcopy(B)
            B = A - B * q
            A = A_new
            U_new = copy.deepcopy(V)
            V = U - V * q
            U = U_new
            if B == 0: break
        d = A
        u = U
        v = (d - x * u)/N
        # NWD(x, N) = d
        # u = x^{-1}
        return u, v, d
