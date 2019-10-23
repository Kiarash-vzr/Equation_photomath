n = input()
# defs
def alamat_gozari(e):
    for i in range(len(e)):
        if (e[i][0] != '+' and e[i][0] != '-') and e[i] != '=':
            e[i] = '+' + e[i]
    return e

def make_two_sides(e):
    i = 0
    e_1 = []
    e_2 = []
    while e[i] != '=':
        e_1.append(e[i])
        i += 1
    i += 1
    while i <= len(e)-1:
        e_2.append(e[i])
        i += 1
    return [e_1,e_2]

def remove_x(n):
    e1 = ''
    for i in range(len(n)):
        if n[i]!='x':
            e1+=n[i]
        else:
            d = i
    return(e1)

def sum_of_sides(e1):
    sum1 = 0
    sum2 = 0
    for i in range(len(e1[0])):
        e1[0][i] = int(e1[0][i])
        sum1 += e1[0][i]
    for i in range(len(e1[1])):
        e1[1][i] = int(e1[1][i])
        sum2 += e1[1][i]
    return [sum1 , sum2]
# defs </>

e1 = remove_x(n) # index [1] == x index         
e1 = e1.split()
e1 = alamat_gozari(e1)
e1 = make_two_sides(e1)

sum_side1 = sum_of_sides(e1)[0]
sum_side2 = sum_of_sides(e1)[1]


if sum_side1 > 0:
    sum_side2 = sum_side2 - sum_side1
    sum_side1 = 0
else:
    sum_side2 = sum_side1 - sum_side2
    sum_side1 = 0

print('x = '+str(sum_side2))
    
