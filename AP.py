l, x, y, z = [], 0, 0, 0
while True:
    an = input("AN: ")
    a1 = input("A1: ")
    r = input("R: ")
    n = input("N: ")

    if a1 == "x":
        an,n,r = float(an),int(n),float(r)
        x = r * (n - 1)
        y = an
        an -= x
        x = z
        for i in range(n):
            l.append(an)
            an += r
        print(l, "\n", y, "\n")
        print("SN:", sum(l), "\n")

    if an == "x":
        a1,n,r = float(a1),int(n),float(r),
        z,y = a1,n
        a1 = a1 - r
        for i in range(n):
            a1 = a1 + r
            l.append(a1)
        print(l, "\n", a1, "\n")
        print("SN:", sum(l), "\n")

    if n == "x":
        an,r,a1 = float(an),float(r),float(a1),
        y = an
        an = ((an - a1) - (r * -1))/r
        x = an.__trunc__()
        for i in range(x):
            l.append(a1)
            a1 += r
        print(l, "\n", an, "\n")
        print("SN:", sum(l), "\n")

    if r == "x":
        an,n,a1 = float(an),int(n),float(a1)
        x = (an - a1) / (n - 1)
        for i in range(n):
            l.append(a1)
            a1 += x
        print(l, "\n", sum(l), "\n")