i = 0
DEBUG = False
def findKth(a, b, k):
    global i
    if (len(a) + len(b) < k):
        return "this isn't a valid input: len(a)[{}] + len(b)[{}] = k[{}]".format(len(a), len(b), k)
    if (DEBUG): print()
    if (DEBUG): print('iteration {}, k = {}'.format(i, k))
    if (DEBUG): print('a:',a)
    if (DEBUG): print('b:',b)
    i += 1
    # base cases
    z_ind = k - 1 # zero-indexing
    if len(a) == 0 or len(b) == 0:
        if (z_ind < len(b)):
            return b[z_ind]
        if (z_ind < len(a)):
            return a[z_ind]
    if k == 1:
        return min(a[0], b[0])

    aVal = a[len(a) // 2]
    bVal = b[len(b) // 2]
    if (DEBUG): print('medians: aVal = {}, bVal = {}'.format(aVal, bVal))
    # Get rid of all numbers that can't possibly be the kth number
    # - Compare medians
    if (aVal > bVal):
        # numbers we know for sure are less than aVal 
        # [everything up to aVal and everything up to and including bVal]
        # a[0:len(a) // 2] and b[0:len(b) // 2 + 1]
        valsBeforeMax = (len(a) // 2) + (len(b) // 2 + 1)

        # numbers we know for sure are more than bVal
        # [everything after and including aVal and everything after bVal]
        valsAfterMin = (len(a) - len(a) // 2) + (len(b) - (len(b) // 2 + 1))

        if (DEBUG): print('max = aVal, valsBeforeMax = {}, valsAfterMin = {}'.format(valsBeforeMax, valsAfterMin))

        # Essentially trim based on what we know about k and its relationship to 
        # a and b.
        if (k <= valsBeforeMax):
            # kth smallest is somewhere before median of a [max median] or somewhere in b
            # Note: can only rule out in a because things in b later on might be k, 
            
            # We know nothing after median of a can be the kth smallest because 
            # there at least k values less than the max median, so everything after 
            # it is irrelevant

            # that are smaller than 
            # two cases arise:
            # 1. k is in a, so it is before 
            # 2. k is in b, so 
            return findKth(a[0:len(a) // 2], b, k)
        else: # k > valsBeforeMax
            # m + n - k <= valsAfterMin
            # m + n - kth largest is somewhere in a or after median of b [min median]
            # kth smallest = (m + n - k)th largest
            # 
            # can get rid of everything before the median in b because to find 
            # the (m + n - k)th largest number, there are at least (m + n - k)
            # values larger than the minimum value, so the (m + n - k)th largest
            # value must be within that portion.

            # k is somewhere after median of b or somewhere in a
            return findKth(a, b[len(b) // 2 + 1:len(b)], k - (len(b) // 2 + 1))
    else: # aVal < bVal
        # inclusive of median of a because it is before max, but we are not sure if what's
        # after is over max
        valsBeforeMax = (len(a) // 2 + 1) + (len(b) // 2)
        valsAfterMin = (len(a) - (len(a) // 2 + 1)) + (len(b) - len(b) // 2)
        if (DEBUG): print('max = bVal, valsBeforeMax = {}, valsAfterMin = {}'.format(valsBeforeMax, valsAfterMin))


        if (k <= valsBeforeMax):
            # kth smallest is somewhere before median of b [max median] or somewhere in a
            return findKth(a, b[0:len(b) // 2], k)
        else:
            # kth smallest is somewhere after median of a [min median] or somewhere in b
            return findKth(a[len(a) // 2 + 1:len(a)], b, k - (len(a) // 2 + 1))

import random
# TODO: Test random generation with set vs randomly picking
def randGen(cant=[]):
    ret = []
    for i in range(random.randint(0, 50)):
        a = random.randint(0, 1000)
        while a in cant or a in ret:
            a = random.randint(0, 1000)
        ret.append(a)
    ret.sort()
    return ret

# a = [1,2,3,4,5,91]
# b = [6,7,9,123]
for i in range(100):
    a = randGen()
    b = randGen(cant=a)
    print('a:',a)
    print('b:',b)
    c = a + b
    c.sort()
    for k in range(1, len(a) + len(b) + 1):
        res = findKth(a, b, k)
        assert res == c[k - 1]
