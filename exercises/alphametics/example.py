from itertools import permutations
from string import ascii_uppercase as acu, digits
acuset = set(acu)
dset = set(digits)


def solve(an):
    fullexp = [tuple(map(str.strip, s.split("+")))
               for s in an.upper().split("==")]
    digexp = [[w[-1] for w in s] for s in fullexp]

    alphas = set("".join([w for s in fullexp for w in s]))
    if not alphas <= acuset:
        raise ValueError
    leadchars = set([w[0] for s in fullexp for w in s])
    digchars = set([x for s in digexp for x in s])
    leadigchars = leadchars & digchars
    leadigcharslen = len(leadigchars)
    leadother = leadchars - leadigchars
    leadotherlen = len(leadother)

    digtuple = tuple(leadigchars) + tuple(set(digchars) - leadigchars)
    othertuple = tuple(leadother) + tuple(alphas - digchars - leadother)
    combostg = "".join(digtuple + othertuple)
    olen = len(othertuple)
    for digtest in permutations(digits, len(digtuple)):
        if any(map(lambda x: x == "0", digtest[:leadigcharslen])):
            continue
        td = dict(zip(digtuple, digtest))
        digeval = [[int(td[w]) for w in s] for s in digexp]
        if (sum(digeval[0]) % 10) == (sum(digeval[1]) % 10):
            for otest in permutations(dset - set(digtest), olen):
                if any(map(lambda x: x == "0", otest[:leadotherlen])):
                    continue
                alldict = dict(zip(combostg, "".join(digtest + otest)))
                fulleval = [[int("".join([alldict[c] for c in w])) for w in s] for s in fullexp]
                if sum(fulleval[0]) == sum(fulleval[1]):
                    return dict(zip(combostg, map(int, digtest + otest)))
    return {}
