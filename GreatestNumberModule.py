def greatest_number(l):
    max = l[0]
    for num in l:
        if max < num:
            max = num
    return max