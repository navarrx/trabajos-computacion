def bingo(a,b,c,d,e,f,g,h,i,j):
    nums = [a, b, c, d, e, f, g, h, i, j]
    win = [2,9,14,7,16]
    c = 0
    for i in win:
        if i in nums:
            c = c + 1
    if c == 5:
        return "WIN"
    else:
        return "LOSE"