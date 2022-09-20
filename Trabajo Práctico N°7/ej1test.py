
def sum_of_differences(a,b,c):
    list = [a,b,c]
    k = 0
    list.sort(reverse=True)
    c = len(list)
    while c < 2:
        print(0)
        break
    else:
        for i in range(len(list)-1):
            sum = list[i] - list[i+1]
            k = k + sum
    return k
