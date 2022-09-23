l, x, y, z = [],0,0,0
while True:
    an = input("Last value: ")
    a1 = input("First value: ")
    r = input("Ratio: ")
    n = input("Number of values: ")

    if a1 == "X" or a1 == "x":
        an, n, r = float(an),int(n),float(r)
        a1 = an - (n-1) * r
        x = a1

        while a1 <= an:
            l.append(a1)
            a1 += r

        print(f'{l} \n{x} \n')
        print(f'Sum: {sum(l)} \n')

    if an == "X" or an == "x":
        a1, n, r = float(a1), int(n), float(r)
        z, y = a1, n

        while n != 0:
            l.append(a1)
            a1 += r
            n -= 1

        print(f'{l} \n{a1-r} \n')
        print(f'Sum: {sum(l)} \n')

    if n == "X" or n == "x":
        a1, an, r = float(a1), float(an), float(r)
        y = an
        an = ((an - a1) - (r * -1))/r
        x = an.__trunc__()

        while x != 0:
            l.append(a1)
            a1 += r
            x -= 1

        print(f'{l} \n{an} \n')
        print(f'Sum: {sum(l)} \n')


    if r == "X" or r == "x":
        a1, an, n = float(a1), float(an), int(n)

        r = (an - a1) / (n-1)
        while n > 0:
            l.append(a1)
            a1 += r
            n -= 1

        print(f'{l} \n{r} \n')
        print(f'Sum: {sum(l)} \n')
