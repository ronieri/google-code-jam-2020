cases = int(input())

for case in range(cases):
    inp = input()
    opens = 0
    string = ""
    for char in inp[::1]:
        if opens < int(char):
            while opens < int(char):
                string += '('
                opens += 1
        if opens > int(char):
            while opens > int(char):
                string += ')'
                opens -= 1
        string += char
    while opens > 0:
        string += ')'
        opens -= 1
    print("Case #" + str(case+1) + ":", string, sep=' ')
