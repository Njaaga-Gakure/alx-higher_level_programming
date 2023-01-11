#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    weight_add = 0
    score = 0
    weight = 0
    s_and_w = 0

    for i in range(len(my_list)):
        weight_add += my_list[i][1]

    for j in range(len(my_list)):
        for k in range(len(my_list[j])):
            if k == 0:
                score = my_list[j][k]
            else:
                weight = my_list[j][k]
        s_and_w += score * weight

    return (s_and_w / weight_add)
