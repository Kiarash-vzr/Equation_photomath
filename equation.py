n = input()
# defs
def alamat_gozari(e1):# return e1 with + and -
    for i in range(len(e1)):
        if (e1[i][0] != '+' and e1[i][0] != '-' and e1[i][0] != '*' and e1[i][0] != '/' and e1[i][0] != '^')\
        and e1[i] != '=':
            e1[i] = '+' + e1[i]
    return e1
def split_list_by(n, p, q):#split n by p and q, return the new "n" as "m"\
    # m = list of n splited by p and q + p and q
    m = []
    l = []
    for i in range(len(n)):
        if n[i] != p and n[i] != q:
            l.append(n[i])
        if n[i] == p or n[i] == q or i == len(n)-1:
            m.append(l)
            m.append(n[i])  
            l = []
        
    return m[:-1] 
def make_two_sides(e1):#make two sides for e1 by '=' , return two sides
    
    i = 0
    side_1 = []
    side_2 = []
    while e1[i] != '=':
        side_1.append(e1[i])
        i += 1
    i += 1
    while i <= len(e1)-1:
        side_2.append(e1[i])
        i += 1
    #making two sides by '='
    return [side_1,side_2]

'''def remove_and_save_x(e1):# making a new equation without x
    
    new_e1 = [e1[0],[]]
    for j in range(len(e1[0])):
        if e1[i][j] == '+x': #not adding x
            pass
        if e1[i][j] == '+x' and e1[i][j-1] == '*': #not adding zaribe x
            pass
        if e1[i][j] == '+x' and e1[i][j-1] == '^': #not adding a^x
            pass
        if e1[i][j] == '+x' and e1[i][j-1] == '^': #not adding tavane x
            pass
        
                
def sum_of_sides(e1):# 
    sum1 = 0
    sum2 = 0
    for i in range(len(e1[0])):
        e1[0][i] = int(e1[0][i])
        sum1 += e1[0][i]
    for i in range(len(e1[1])):
        e1[1][i] = int(e1[1][i])
        sum2 += e1[1][i]
    return [sum1 , sum2]'''

# defs </>




e1 = n
e1 = e1.split()
e1 = alamat_gozari(e1)
e1 = make_two_sides(e1)

print(e1)
print(split_list_by(e1[0], '+', '-'))
print(split_list_by(e1[1], '+', '-'))

def solve_algebra_phrase_layer(e1, layer_counter):# solving without ()
    if layer_counter == 1:
        print(e1,'round 1')
        split_e1 = split_list_by(e1, '-', '+')
        print(split_e1,'round 1','splited')
        #split equation by + and -
        
        first_layer_answer = solve_algebra_phrase(split_e1[0], 2)
        for i in range(len(split_e1)):
            if split_e1[i] == '+':
                first_layer_answer = first_layer_answer + solve_algebra_phrase(split_e1[i+1], 2)
            if split_e1[i] == '-':
                first_layer_answer = first_layer_answer - solve_algebra_phrase(split_e1[i+1], 2)
        #sending parts to the second layer   
        final_answer = first_layer_answer
        print(final_answer)
        return (final_answer)

    
    if layer_counter == 2:
        print(e1,'round 2')
        split_e1 = split_list_by(e1, '*', '/')
        #split equation by * and /
        
        second_layer_answer = solve_algebra_phrase(split_e1[0], 3)
        for i in range(len(split_e1)):
            if split_e1[i] == '*':
                second_layer_answer = second_layer_answer * solve_algebra_phrase(split_e1[i+1], 3)
            if split_e1[i] == '/':
                second_layer_answer = second_layer_answer / solve_algebra_phrase(split_e1[i+1], 3)

        #sending parts to the third layer
        print (second_layer_answer)
        return (second_layer_answer)

    
    if layer_counter == 3:
        print(e1,'round 3')
        split_e1 = split_list_by(e1, '^', '^')
        #split equation by ^ and ^
        third_layer_answer = solve_algebra_phrase(split_e1[0], 4)
        for i in range(len(split_e1)):
            if split_e1[i] == '^':
                third_layer_answer = third_layer_answer ** solve_algebra_phrase(split_e1[i+1], 4)
        #sending parts to the last layer
        #start solving from the lowewst layer
        return (third_layer_answer)

    
    elif layer_counter > 3:
        e1 = float(e1[0])
        print(e1, 'round 4')
        return (e1)
def solve_algebra_phrase(e1, layer_counter):# with () using "solve_algebra_phrase_layer"
    return
    
print(solve_algebra_phrase(e1[1], 1))
e1[1] = solve_algebra_phrase(e1[1], 1)
    
