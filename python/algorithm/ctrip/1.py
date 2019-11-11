import sys

def edit(s1, s2):
    tab = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    # tab[i][j] means editing distance from s1[:i] to s2[:j]
    for i in range(0, len(s1)+1):
        tab[i][0] = i
    for j in range(1, len(s2)+1):
        tab[0][j] = j
    import pdb
    # pdb.set_trace()
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            tab[i][j] = min(tab[i-1][j] + 1, # del
                            tab[i][j-1] + 1, # add
                            tab[i-1][j-1] + (0 if s1[i-1] == s2[j-1] else 1)) # sub
    return tab[len(s1)][len(s2)]

def main():
    line = sys.stdin.readline().rstrip('\n')
    s1, s2 = line.split('<ctrip>')
    print(edit(s1, s2))

if __name__ == '__main__':
    main()

