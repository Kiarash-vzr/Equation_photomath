n = input()
# defs
def alamat_gozari(e):
    for i in range(len(e)):
        if (e[i][0] != '+' and e[i][0] != '-' and e[i][0] != '*' and e[i][0] != '/')\
        and e[i] != '=':
            e[i] = '+' + e[i]
        #else:
    
    return e
def split_list_by(n, p, q):
    m = []
    l = []
    for i in range(len(n)):
        if n[i] != p and n[i] != q:
            l.append(n[i])
        if n[i] == p or n[i] == q or i == len(n)-1:
            m.append(l)
            l = []
        
    return m
def make_two_sides(e):
    i = 0
    side_1 = []
    side_2 = []
    while e[i] != '=':
        side_1.append(e[i])
        i += 1
    i += 1
    while i <= len(e)-1:
        side_2.append(e[i])
        i += 1
    return [side_1,side_2]

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

e1 = n
e1 = e1.split()
e1 = alamat_gozari(e1)
e1 = make_two_sides(e1)

print(e1)
print(split_list_by(e1[0], '+', '-'))
      
def solve(e1, round_counter):
    if round_counter == 1:
        split_e1 = split_list_by(e1, '-', '+')
        #split equation by + and -
        
        first_layer_answer = 0
        for i in range(len(split_e1)):
            first_layer_answer = first_layer_answer + solve(split_e1[i], 2)
            
        final_answer = first_layer_answer
        print(final_answer)
        return (final_answer)

    
    if round_counter == 2:
        split_e1 = split_list_by(e1, '*', '/')
        #split equation by * and /
        
        second_layer_answer = 0
        for i in range(len(split_e1)):
            second_layer_answer = second_layer_answer * solve(split_e1[i], 3)

        return (second_layer_answer)

    
    if round_counter == 3:
        split_e1 = split_list_by(e1, '^', '^')
        #split equation by ^ and ^
        third_layer_answer = 0
        for i in range(len(split_e1)):
            third_layer_answer = third_layer_answer ** solve(split_e1[i], 4)
        #start solving from the lowewst layer
        return (third_layer_answer)

    
    elif round_counter > 3:
        e1 = int(e1[0])
        return (e1)
print(solve(e1[1], 1))
'''sum_side1 = sum_of_sides(e1)[0]
sum_side2 = sum_of_sides(e1)[1]


if sum_side1 > 0:
    sum_side2 = sum_side2 - sum_side1
    sum_side1 = 0
else:
    sum_side2 = sum_side1 - sum_side2
    sum_side1 = 0

print('x = '+str(sum_side2))'''
    
