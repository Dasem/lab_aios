def komm(sum_nodes, pasted, current_node):
    global result
    global path
    if len(pasted) == len(matrix):                                     # 3{СУ} + &{1/n?}
        pasted.append(0)                                               # (   +1
        sum_nodes += matrix[current_node][0]                           #   +2
        if result == -1 or result > sum_nodes:                         #  3{СУ} + &{log(n)?} 
            result = sum_nodes                                         # ( то +2)
            path = pasted                                              # )
        return                                                         # 

    for next_node in range(len(matrix)):                               # 1+n*( 
        if next_node not in pasted:                                    # 2{СУ} + &{1/2n??? откуда я знаю?}
            new_pasted = pasted.copy()                                 #  (  +2
            new_pasted.append(next_node)                               #     +1
            komm(sum_nodes + matrix[current_node][next_node],          # +1 + рекурсия))
                 new_pasted,
                 next_node)


#Знак & используется для обозначения ебанутой вероятности

# Итого : рекурсия из ( 3+&(1+2+3+&(2)+1+n*(1+ &(+2+1+1) )) 
# Итого : !( 3+&(3+3+&(2)+1+n*(1+ &(4) ))+1



def find_kommivoyajer_path(cycle):
    meeted_nodes = []                             # +1 
    for node in cycle:                            # (2n-1)*(
        if node not in meeted_nodes:              # 2{СУ} + &{1/2n??? откуда я знаю?x2}
            meeted_nodes.append(node)             #   (+1)
    meeted_nodes.append(meeted_nodes[0])          #  ) +1
    return meeted_nodes

# Итого :  1 + (2n-1)*(2 + &(1)) +1
# Итого : Упрощение не потребовалось :с 

#+1 в мэйне

def eilerov_cycle(matrix, current_node, edges_history, start_node):  # [[вес, откуда, куда],...]
    global pasted_nodes                                                                     # contains_all+get_list_nodes 
    if contains_all(get_list_nodes(matrix), pasted_nodes) and current_node == start_node:   # 2+(0,5*n +n){СУ} + &{низнаю}
        return                                                                              #   
    else:
        is_there_path = False                                                               # !&( +1
        for node in range(len(matrix)):                                                     # +1 + n*
            if matrix[current_node][node] > 0:                                              # ( 1{СУ} + &{idk}
                next_edge = [matrix[current_node][node], current_node, node]                # ( 1
                if matrix[current_node][node] > 0 and next_edge not in edges_history:       #   +4{СУ} + &{}
                    is_there_path = True                                                    #   +1
                    edges_history.append(next_edge)                                         #    +1
                    pasted_nodes.append(node)                                               #    +1
                    eilerov_cycle(matrix, node, edges_history, start_node)                  #   ! ))
        if not is_there_path and not contains_all(get_list_nodes(matrix), pasted_nodes):    # +3+(0,5*n +n){СУ} + &
            rollback_eilerov_cycle(pasted_nodes, edges_history)                             #  (+2)  )

# Итого :  2+(0,5*n +n){СУ} + !&( 1+1 + n*(1{СУ} + &( 1+4{СУ} +& +1+1+1 ~tut!))+3+(0,5*n +n){СУ} + &(+2)  )
# Итого :  2n((2+1,5*n){СУ} + !&( 2 + n*(1{СУ} + &(1+4{СУ} +&*3))+(3+1,5*n){СУ} + &*2 ))
#           | 2n - min, n^2 - max


def contains_all(list, collection):
    for element in list:                  
        if element not in collection:     
            return False
    return True
# Итого :  0,5*n

# На караскале























































