n = input()
# defs
def alamat_gozari(e1):# return e1 with + and -
    for i in range(len(e1)):
        if e1[i][0] != '+' and e1[i][0] != '-' and e1[i][0] != '*' and e1[i][0] != '/' and e1[i][0] != '^'\
        and e1[i] != '=' and e1[i] != ')' and e1[i] != '(':
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
    i = e1.index('=')
    return (e1[:i], e1[i+1:])

def solve_minus_times_sth(e1):#return new e1 as e
    #e = replace '-(' with '-1 * ('
    e = []
    for i in range(len(e1)):
        print(i,e1[i])
        if e1[i][0] == '-' and e1[i] != '-':
            e.append('-1')
            e.append('*')
            e.append(e1[i][1:])
        else:
            e.append(e1[i])
    return e
            
# defs </>




def Solve_polynomial_phrase(e1, layer_counter):# solving without ()
    print(e1)
    if layer_counter == 1:
        split_e1 = split_list_by(e1, '-', '+')
        #split equation by + and -
        first_layer_answer = Solve_polynomial_phrase(split_e1[0], 2)
        for i in range(len(split_e1)):
            if split_e1[i] == '+':
                first_layer_answer = first_layer_answer + Solve_polynomial_phrase(split_e1[i+1], 2)
            if split_e1[i] == '-':
                first_layer_answer = first_layer_answer - Solve_polynomial_phrase(split_e1[i+1], 2)
        #sending parts to the second layer
        final_answer = first_layer_answer
        print(final_answer)
        return (final_answer)
    
    if layer_counter == 2:
        split_e1 = split_list_by(e1, '*', '/')
        #split equation by * and /
        second_layer_answer = Solve_polynomial_phrase(split_e1[0], 3)
        for i in range(len(split_e1)):
            if split_e1[i] == '*':
                second_layer_answer = second_layer_answer * Solve_polynomial_phrase(split_e1[i+1], 3)
            if split_e1[i] == '/':
                second_layer_answer = second_layer_answer / Solve_polynomial_phrase(split_e1[i+1], 3)
        print(second_layer_answer, "second")
        #sending parts to the third layer
        return (second_layer_answer)

    if layer_counter == 3:
        split_e1 = split_list_by(e1, '^', '^')
        #split equation by ^ and ^
        third_layer_answer = Solve_polynomial_phrase(split_e1[-1], 4)
        for i in range(len(split_e1)-1, -1, -1):
            if split_e1[i] == '^':
                print(third_layer_answer, "third")
                third_layer_answer = Solve_polynomial_phrase(split_e1[i-1], 4) ** third_layer_answer  
        #sending parts to the last layer
        #start solving from the lowewst layer
        return (third_layer_answer)

    elif layer_counter > 3:
        e1 = float(e1[0])
        return (e1)




def Solve_brackets(e1):#solve algebra phrase (with brackets)\
    # \using Solve_polynomial_phrase 
    # e = replacing e1's brackets as their answers
    # bracket_list = list of a bracket
    # each bracket_list will be recalled in function
    e = []
    bracket_exists = False
    for i in range(len(e1)):#chek if e1 has brackets
        if e1[i] == '(' or e1[i] == ')':
            bracket_exists = True
    
    if bracket_exists == False:# final layer
        return (Solve_polynomial_phrase(e1, 1))
    
    if bracket_exists == True:# layering
        i = 0
        b_counter = 0
        inside_bracket = False
        bracket_list = []
        while i < len(e1):

            if e1[i] != '(' and e1[i] != ')':
                if inside_bracket == True:
                    bracket_list.append (e1[i])
                else:
                    e.append(e1[i])
                i += 1
          
            elif e1[i] == '(':#beggining of bracket
                if inside_bracket == True:
                    bracket_list.append (e1[i])   
                b_counter += 1
                inside_bracket = True
                i += 1
                
            elif e1[i] == ')':
                print(") hastam")
                if inside_bracket == True:
                    bracket_list.append (e1[i])
                b_counter -= 1
                i += 1
                
            if inside_bracket == True and e1[i-1] == ')' and b_counter == 0:
                #ending of one bracket
                #adding bracket list to e
                #caling the function for the bracket
                bracket_list = bracket_list[:-1]
                e.append (Solve_brackets(bracket_list))
                inside_bracket = False
                bracket_list = []
            if b_counter < 0:# if ")"s more than "("s
                return ("false equation")
        if b_counter != 0:# if "("s are more than ")"s
            return ("false equation")
            
    return(e)




def Find_coefficient_of_variables(e1):
    e1 = Solve_brackets(e1)
    split_e1 = split_list_by(e1, '-', '+')
    print(split_e1)


    
e1 = n
e1 = e1.split()
e1 = solve_minus_times_sth(e1)
print(e1)
e1 = alamat_gozari(e1)
print (e1)
e1 = make_two_sides(e1)
Find_coefficient_of_variables(e1[1])
