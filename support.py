import pytest

entrada = [[0,1,2],[4,2,3]]
saida = [[None, None, None],[4, None, None]]
min_supp = 3

def support(entrada, min_supp):
    supp_list = []

    for temp1 in entrada:
        temp_list = []
        for temp2 in temp1:
            if int(temp2) <= min_supp:
	        temp_list.append(None)
            else:
                temp_list.append(temp2)
        supp_list.append(temp_list)
    return supp_list

assert saida == support(entrada, min_supp)
