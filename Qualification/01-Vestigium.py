cases = int(input())

for case in range(cases):
    matrix = []
    s = l = r = 0
    size = int(input())
    compare = range(1, size+1)
    for i in range(size):
        line = [int(value) for value in input().split()]
        s += line[i]
        matrix.append(line)
        if set(sorted(line)) != set(compare):
            l += 1
    for i in range(size):
        row = [e[i] for e in matrix]
        if set(sorted(row)) != set(compare):
            r += 1
    print("Case #" + str(case+1) + ":", s, l, r, sep=' ')