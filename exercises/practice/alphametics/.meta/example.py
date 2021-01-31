from itertools import permutations, chain, product
"""
This solution will first parse the alphametic expression
grouping and counting letters buy digit ranks
then trace recursively all possible permutations starting from
the lowest rank and genrating additional permutations for new digits
at higer ranks as necessary.
This will allow to avoid unnesessarily large permutations to scan.
Also leading letters in words will be treated as non-zero digits only
to reduce the number of permutations
"""


def digPerms(digset, nzcharset, okzcharset):
    """This function creates permutations given the set of digits,
       letters not alllowed to be 0, and letters allowed to be 0
    """
    nzcnt = len(nzcharset)  # How many letters are non-0
    okzcnt = len(okzcharset)  # How many letters are allowed 0
    totcnt = nzcnt + okzcnt  # Total number of letters
    if totcnt < 1:  # if total numbers of letters is 0
        return [()]  # return a singe empty permutation
    nzdigset = digset - set((0,))  # generate a non-zero digit set
    nzdigsetcnt = len(nzdigset)  # how many non-zero digits are available
    digsetcnt = len(digset)  # how many ok zero digits are available
    # if either fewer digits than letters at all or fewer non-0 digits
    # than letters that need to be non-zero
    if digsetcnt < totcnt or nzdigsetcnt < nzcnt:
        return []  # Return no permutations possible
    # Simple case when zeros are allowed everwhere
    # or no zero is containted within the given digits
    elif nzcnt == 0 or digsetcnt == nzdigsetcnt:
        return permutations(digset, totcnt)
    # Another simple case all letters are non-0
    elif okzcnt == 0:
        return permutations(nzdigset, totcnt)
    else:
        # General case
        # Generate a list of possible 0 positions
        poslst = list(range(nzcnt, totcnt))
        # Chain two iterators
        # first iterator with all non-0 permutations
        # second iterator with all permulations without 1 letter
        # insert 0 in all possible positions of that permutation
        return chain(permutations(nzdigset, totcnt),
                     map(lambda x: x[0][:x[1]] + (0,) + x[0][x[1]:],
                         product(permutations(nzdigset, totcnt - 1),
                                 poslst)))


def check_rec(eqparams, tracecombo=(dict(), 0, set(range(10))), p=0):
    """This function recursively traces a parsed expression from lowest
       digits to highest, generating additional digits when necessary
       checking the digit sum is divisible by 10, carrying the multiple of 10
       up to the next level
    """
    # Basic parameters of the equation,
    # maximal digit rank
    # characters with multipliers by rank
    # unique non-zero characters by rank
    # unique zero-allowed characters by rank
    # all unique characters by rank
    maxp, tchars, unzchars, uokzchars, uchars = eqparams
    # recursion cumulative parameters
    # established characters with digits
    # carry-over from the previous level
    # remaining unassigned digits
    prevdict, cover, remdigs = tracecombo
    # the maximal 10-power (beyond the maximal rank)
    # is reached
    if p == maxp:
        # Carry-over is zero, meaning solution is found
        if cover == 0:
            return prevdict
        else:
            # Otherwise the solution in this branch is not found
            # return empty
            return dict()
    diglets = uchars[p]  # all new unique letters from the current level
    partsum = cover  # Carry over from lower level
    remexp = []  # TBD letters
    # Break down the current level letter into what can be
    # calculated in the partial sum and remaining TBD letter-digits
    for c, v in tchars[p]:
        if c in prevdict:
            partsum += v * prevdict[c]
        else:
            remexp.append((c, v))
    # Generate permutations for the remaining digits and currecnt level
    # non-zero letters and zero-allowed letters
    for newdigs in digPerms(remdigs, unzchars[p], uokzchars[p]):
        # build the dictionary for the new letters and this level
        newdict = dict(zip(diglets, newdigs))
        # complete the partial sum into test sum using the current permutation
        testsum = partsum + sum([newdict[c] * v
                                 for c, v in remexp])
        # check if the sum is divisible by 10
        d, r = divmod(testsum, 10)
        if r == 0:
            # if divisible, update the dictionary to all established
            newdict.update(prevdict)
            # proceed to the next level of recursion with
            # the same eqparams, but updated digit dictionary,
            # new carry over and remaining digits to assign
            rectest = check_rec(eqparams,
                                (newdict, d, remdigs - set(newdigs)),
                                p + 1)
            # if the recursive call returned a non-empty dictionary
            # this means the recursion has found a solution
            # otherwise, proceed to the new permutation
            if rectest and len(rectest) > 0:
                return rectest
    # if no permutations are avaialble or no
    # permutation gave the result return None
    return None


def solve(an):
    """A function to solve the alphametics problem
    """
    # First, split the expresion into left and right parts by ==
    # split each part into words by +
    # strip spaces fro, each word, reverse each work to
    # enumerate the digit rank from lower to higer
    fullexp = [list(map(lambda x: list(reversed(x.strip())), s.split("+")))
               for s in an.strip().upper().split("==")]
    # Find the maximal lenght of the work, maximal possive digit rank or
    # the power of 10, should the < maxp
    maxp = max([len(w) for s in fullexp for w in s])
    # Extract the leading letters for each (reversed) word
    # those cannot be zeros as the number cannot start with 0
    nzchars = set([w[-1] for s in fullexp for w in s])
    # initialize the lists for digit ranks
    unzchars = []  # non-zero letters unique at level
    uokzchars = []  # zero-allowed letters unique at level
    uchars = []  # all letters unique at level
    tchars = []  # all letter with multipliers per level
    for i in range(maxp):
        tchars.append(dict())
        unzchars.append(set())
        uokzchars.append(set())
    # Now lets scan the expression and accumulate the letter counts
    for si, s in enumerate(fullexp):
        sgn = 1 - (si << 1)  # left side (0) is +1, right right (1) is -1
        for w in s:  # for each word in the side (already reversed)
            for p, c in enumerate(w):  # enumerate with ranks
                if c not in tchars[p]:  # check if the letter was alread there
                    tchars[p][c] = 0
                tchars[p][c] += sgn  # append to the rank dictionary

    totchars = set()  # Keep track of letters already seen at lower ranks
    # go through the accumulated rank dictionaries
    for p, chardict in enumerate(tchars):
        for c, cnt in tuple(chardict.items()):
            if cnt == 0:  # if the cumulative is 0
                del chardict[c]  # remove the letter from check dictionry
                # it does not impact the sum with 0-multiplier
            # if the letter contributes to the sum
            # and was not yet seen at lower ranks
            elif c not in totchars:
                # add the letter to either non-zero set
                # or allowed-zero set
                if c in nzchars:
                    unzchars[p].add(c)
                else:
                    uokzchars[p].add(c)
                # add to the list as seen letter to ignore at the next
                # ranks
                totchars.add(c)
        # pre-build the combo list of letters for the rank
        # non-zero first, followed by zero-allowed
        uchars.append(tuple(unzchars[p]) + tuple(uokzchars[p]))
        # pre-convert check dictionaries to tuples
        tchars[p] = tuple(chardict.items())
    # go for the recursion
    return check_rec([maxp, tchars, unzchars, uokzchars, uchars])
