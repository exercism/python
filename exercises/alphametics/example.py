from itertools import permutations
from string import ascii_uppercase as acu, digits
acuset = set(acu)
dset = set(range(10))
nzdset = dset.copy()
nzdset.remove(0)


def solve(an):
    # Break down to words
    an = an.upper()
    alphaexp = [tuple(map(str.strip, s.split("+")))
                for s in an.split("==")]
    # Sum powers of 10 for letters ready for computation
    expdict = dict()
    loexpdict = dict()
    for si, s in enumerate(alphaexp):
        esign = 1 - (si << 1)
        for t in s:
            lowletter = t[-1]
            if lowletter not in loexpdict:
                loexpdict[lowletter] = 0
            loexpdict[lowletter] += esign
            for p, letter in enumerate(reversed(t)):
                if letter not in expdict:
                    expdict[letter] = 0
                expdict[letter] += esign * (10 ** p)

    # Last digits expression only, to check
    lowdigittexp = [[w[-1] for w in s] for s in alphaexp]

    # Extract all letters and check if they are really letters
    alldigits = set("".join([w for s in alphaexp for w in s]))
    if not alldigits <= acuset:
        raise ValueError

    # extract high and low digigts
    hidigits = set([w[0] for s in alphaexp for w in s])
    lodigits = set([w[-1] for s in alphaexp for w in s])

    # Break down low digits to nonzeros (also high digits) and possible zeros
    lonzdigits = lodigits & hidigits
    lorestdigits = lodigits - lonzdigits

    # Main digits, all but not low
    maindigits = alldigits - lodigits

    # Break down main digit list into nonzeroees and possible zeroes
    mainnzdigits = maindigits & hidigits
    mainrestdigits = maindigits - mainnzdigits

    # change sets to tuples to guarantee the stable order
    t_lorestdigits = tuple(lorestdigits)
    t_lonzdigits = tuple(lonzdigits)
    t_lowdigs = t_lorestdigits + t_lonzdigits

    t_mainrestdigits = tuple(mainrestdigits)
    t_mainnzdigits = tuple(mainnzdigits)
    t_maindigs = t_mainrestdigits + t_mainnzdigits
    t_alldigs = t_lowdigs + t_maindigs

    # Check all possible digit permunations with zeros
    for lorest in permutations(dset, len(lorestdigits)):
        remnzdigs = nzdset - set(lorest)
        # Generate addtional non-zero digit permutations
        for lonz in permutations(remnzdigs, len(lonzdigits)):
            # Build a dictionary for to test the expression
            t_digvals = lorest + lonz
            # Evaluate the expression sides
            testsum = sum([dig * loexpdict[let]
                           for let, dig in zip(t_lowdigs, t_digvals)])
            if testsum % 10 == 0:
                # Low digit test passed, check the main digits
                # print(lowdigdict)
                # if there are no other digits that low digits,
                # test the whole expression and return if OK
                if len(maindigits) == 0:
                    testsum = sum([dig * expdict[let]
                                   for let, dig in zip(t_lowdigs, t_digvals)])
                    if testsum == 0:
                        return dict(zip(t_lowdigs, t_digvals))
                else:
                    # non-assigned digits
                    remdigs = dset - set(t_digvals)
                    # non-assigned without 0
                    remnzdigs = remdigs - set((0,))
                    # permutations for the rest of the digits
                    for mainrest in permutations(remdigs,
                                                 len(t_mainrestdigits)):
                        lastnzdigs = remnzdigs - set(mainrest)
                        # permutations for the non-zero rest of the digits
                        for mainnz in permutations(lastnzdigs,
                                                   len(t_mainnzdigits)):
                            # Evaluate
                            t_alldigvals = lorest + lonz + mainrest + mainnz
                            testsum = sum([dig * expdict[let]
                                           for let, dig in zip(t_alldigs,
                                                               t_alldigvals)])
                            if testsum == 0:
                                return dict(zip(t_alldigs, t_alldigvals))

    return {}
