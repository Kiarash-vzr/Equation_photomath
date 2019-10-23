n = input()
def split1(n,a,b):
    l = []
    i = 0
    for i in range(len(n)):
        j = 0
        s=''
        if i+j<len(n):
            while a!=n[i+j] and b!=n[i+j]:
                s = s+n[i]
                j+=1
                if i+j>=len(n):
                    break
        l.append(s)
    return l
n1 = split1(n,'+','-')
n2 = split1(n1,'*','/')
n3 = split1(n2,'^','^')
print(n)
print(n1)
print(n2)
print(n3)
