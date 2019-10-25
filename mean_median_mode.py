import math

def mean(numbers, places):
    sumNums = 0
    for x in numbers:
        sumNums += x

    ans = (sumNums / (len(numbers)))
    ans = str(ans)
    ans = ans[:ans.index('.')+(places+1)]
    return float(ans)


def median(numbers):
    ans = []
    numbers = sorted(numbers)
    l = len(numbers)
    if l % 2 == 0: # Means that length is even. 
        pos1 = int(l / 2)
        pos2 = int(l / 2) - 1
        
        ans.append(numbers[pos1])
        ans.append(numbers[pos2])
        return sorted(ans)
    else: # Means that length is odd. 
        return numbers[int(l/2)]



def mode(numbers):
    d = {}
    for x in numbers:
        d.


numbers = [12, 4546.332, 11, 1, 1, 90, 90, 77]
print(mean(numbers, 3))
print(median(numbers))
print(mode(numbers))







































'''
def mode(numbers):
    d = {}
    for x in numbers:
        d.setdefault(x)
    for x in numbers:
        d[x] = numbers.count(x)
    k=list(d.keys())
    v=list(d.values())
    return k[v.index(max(v))]
'''
