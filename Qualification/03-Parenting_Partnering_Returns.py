T = int(input())

for testcase in range(T):
    N = int(input())
    impossible = False
    cameron = []
    jamie = []
    schedules = []
    output = []
    for line in range(N):
         schedules.append([int(v) for v in input().split()])
         schedules[line].append(line)
    schedules.sort(key=lambda x: x[0])
    last = 0
    for event in schedules:
        if event[0] >= last:
            cameron.append(event)
            output.append([event[2], 'C'])
            last = event[1]
        else:
            jamie.append(event)
            output.append([event[2], 'J'])
    last = 0
    for j in jamie:
        if j[0] < last:
            impossible = True
            break
        last = j[1]
    out = ""
    for o in sorted(output, key=lambda x: x[0]):
        out += o[1]
    print("Case #" + str(testcase+1) + ":", "IMPOSSIBLE" if impossible else out, sep=' ')