def is_inside(l1,l2):
    if l2[0] <= l1[0] & l1[0] <= l2[0]+l2[2]:
        if l2[1] <= l1[1] & l1[1] <= l2[1] + l2[3]:
            return True
    else:
        return False

l1 = [180, 160]
l2 = [140,60,100,200]
test = is_inside(l1,l2)
print(test)




