def komm(sum_nodes, pasted, current_node):
    global result
    global path
    if len(pasted) == len(matrix):                                     # 3{��} + &{1/n?}
        pasted.append(0)                                               # (   +1
        sum_nodes += matrix[current_node][0]                           #   +2
        if result == -1 or result > sum_nodes:                         #  3{��} + &{log(n)?} 
            result = sum_nodes                                         # ( �� +2)
            path = pasted                                              # )
        return                                                         # 

    for next_node in range(len(matrix)):                               # 1+n*( 
        if next_node not in pasted:                                    # 2{��} + &{1/2n??? ������ � ����?}
            new_pasted = pasted.copy()                                 #  (  +2
            new_pasted.append(next_node)                               #     +1
            komm(sum_nodes + matrix[current_node][next_node],          # +1 + ��������))
                 new_pasted,
                 next_node)


#���� & ������������ ��� ����������� �������� �����������

# ����� : �������� �� ( 3+&(1+2+3+&(2)+1+n*(1+ &(+2+1+1) )) 
# ����� : !( 3+&(3+3+&(2)+1+n*(1+ &(4) ))+1



def find_kommivoyajer_path(cycle):
    meeted_nodes = []                             # +1 
    for node in cycle:                            # (2n-1)*(
        if node not in meeted_nodes:              # 2{��} + &{1/2n??? ������ � ����?x2}
            meeted_nodes.append(node)             #   (+1)
    meeted_nodes.append(meeted_nodes[0])          #  ) +1
    return meeted_nodes

# ����� :  1 + (2n-1)*(2 + &(1)) +1
# ����� : ��������� �� ������������� :� 

#+1 � �����

def eilerov_cycle(matrix, current_node, edges_history, start_node):  # [[���, ������, ����],...]
    global pasted_nodes                                                                     # contains_all+get_list_nodes 
    if contains_all(get_list_nodes(matrix), pasted_nodes) and current_node == start_node:   # 2+(0,5*n +n){��} + &{������}
        return                                                                              #   
    else:
        is_there_path = False                                                               # !&( +1
        for node in range(len(matrix)):                                                     # +1 + n*
            if matrix[current_node][node] > 0:                                              # ( 1{��} + &{idk}
                next_edge = [matrix[current_node][node], current_node, node]                # ( 1
                if matrix[current_node][node] > 0 and next_edge not in edges_history:       #   +4{��} + &{}
                    is_there_path = True                                                    #   +1
                    edges_history.append(next_edge)                                         #    +1
                    pasted_nodes.append(node)                                               #    +1
                    eilerov_cycle(matrix, node, edges_history, start_node)                  #   ! ))
        if not is_there_path and not contains_all(get_list_nodes(matrix), pasted_nodes):    # +3+(0,5*n +n){��} + &
            rollback_eilerov_cycle(pasted_nodes, edges_history)                             #  (+2)  )

# ����� :  2+(0,5*n +n){��} + !&( 1+1 + n*(1{��} + &( 1+4{��} +& +1+1+1 ~tut!))+3+(0,5*n +n){��} + &(+2)  )
# ����� :  2n((2+1,5*n){��} + !&( 2 + n*(1{��} + &(1+4{��} +&*3))+(3+1,5*n){��} + &*2 ))
#           | 2n - min, n^2 - max


def contains_all(list, collection):
    for element in list:                  
        if element not in collection:     
            return False
    return True
# ����� :  0,5*n

# �� ���������























































