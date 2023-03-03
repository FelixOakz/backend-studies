def lonelyinteger(a):
    for i in a:
        c = a.count(i)
        if c == 1:
            return i
