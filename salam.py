def joda_sazi(moadele,joda):
    for i in range(len(moadele)):
        if moadele == joda:
            break
    return moadele[:i-1],moadele[i:]
def str_to_int(part):
    jam = 0
    str_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    str_jam=''
    for i in part:
        f=0
        for j in str_list:
            if j in i  and f==0:
                f=1
                str_jam=str_jam+i
                break
        if f==0 :
            jam = jam + int(i)
    return str_jam+str(jam)
            
    
moadele = input().split()
part1,part2 = joda_sazi(moadele,'=')
print(part1,part2)

part1=str_to_int(part1)
part2=str_to_int(part2)
print(part1,part2)
