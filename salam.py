def joda(moadele,joda):
    for i in range(len(moadele)):
        if moadele == joda:
            break
    return moadele[:i-1],moadele[i:]

moadele = input().split()
moadele = joda(moadele,'=')
print(moadele)
