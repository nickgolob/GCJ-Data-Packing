
# grabs the index for the optimal disc for particular data
#   typical binary search, and assumes discs is non empty
def seek(discs, data):
    discs = sorted(discs)
    up, low = len(discs), 0
    j = (up - low) // 2
    while (discs[j] != data):
        if discs[j] < data:
            low = j
            j = (up - j) // 2 + low
            if low == j:
                while (discs[j] < data):
                    j += 1
                    if j == len(discs):
                        return False, None
                break
        else:
            up = j
            j = (j - low) // 2 + low
            if up == j:
                while (j > 0 and discs[j - 1]> data):
                    j -= 1
                break         
    return True, j

def seek2(discs, data):
    discs = sorted(discs)
    i = 0
    while (discs[i] < data):
        i += 1
        if i == len(discs):
            return False, None
    return True, i

def solve(n, x, data):
    data = sorted(data, reverse=True)
    discs = [x - data.pop(0)]
    while (data):
        i = data.pop(0)
        j, k = seek(discs, i)
        if j:
            discs[k] = 0 # nothing else may be inserted here
            discs.insert(discs.pop(k), 0)
        else:
            discs.append(x - i) # new disc with data          
    return len(discs)


content = [[int(j) for j in i] for i in
           [j.rstrip('\n').split(' ') for j in open('large.in').readlines()]]
for i in range(content.pop(0)[0]):
    print('Case #{0}: {1}'.format(i + 1, solve(content[0][0], content.pop(0)[1], content.pop(0))))
