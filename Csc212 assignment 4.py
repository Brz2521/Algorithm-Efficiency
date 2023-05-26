
def check_list(items):
    lst = []
    for num in items:
        if num in lst:
            return False
        else:
            lst.append(num)
    return True

def check_list2(stuff):
    d = {}
    for num in stuff:
        if num in d:
            return False
        else:
            d[num] = 0

    return True

print(check_list2([56,78,2, 56,45,5]))
