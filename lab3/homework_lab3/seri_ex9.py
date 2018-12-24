def get_even_list(l):
    new_l = []
    for i in range(len(l)):
        if (l[i]% 2 == 0):
           new_l.append(l[i])
    return new_l
# l = [1,4,5,-1,10]
# test_l = get_even_list(l)
# print(test_l)