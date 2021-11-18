"""
This solution will first parse the alphametic expression
grouping and counting letters buy digit ranks
then trace recursively all possible permutations starting from
the lowest rank and genrating additional permutations for new digits
at higer ranks as necessary.
This will allow to avoid unnecessarily large permutations to scan.
Also leading letters in words will be treated as non-zero digits only
to reduce the number of permutations
"""

from itertools import permutations, chain, product


def dig_perms(digit_set, non_zero_chars, ok_zero_chars):
    """This function creates permutations given the set of digits,
       letters not alllowed to be 0, and letters allowed to be 0
    """
    non_zero_count = len(non_zero_chars)  # How many letters are non-0
    ok_zero_count = len(ok_zero_chars)  # How many letters are allowed 0
    total_count = non_zero_count + ok_zero_count  # Total number of letters
    if total_count < 1:  # if total numbers of letters is 0
        return [()]  # return a singe empty permutation
    non_zero_digit_set = digit_set - set((0,))  # generate a non-zero digit set
    available_zero_digit_count = len(non_zero_digit_set)  # how many non-zero digits are available
    ok_zero_digit_count = len(digit_set)  # how many ok zero digits are available
    # if either fewer digits than letters at all or fewer non-0 digits
    # than letters that need to be non-zero
    if ok_zero_digit_count < total_count or available_zero_digit_count < non_zero_count:
        return []  # Return no permutations possible
    # Simple case when zeros are allowed everwhere
    # or no zero is containted within the given digits
    elif non_zero_count == 0 or ok_zero_digit_count == available_zero_digit_count:
        return permutations(digit_set, total_count)
    # Another simple case all letters are non-0
    elif ok_zero_count == 0:
        return permutations(non_zero_digit_set, total_count)
    else:
        # General case
        # Generate a list of possible 0 positions
        positions_list = list(range(non_zero_count, total_count))
        # Chain two iterators
        # first iterator with all non-0 permutations
        # second iterator with all permulations without 1 letter
        # insert 0 in all possible positions of that permutation
        return chain(permutations(non_zero_digit_set, total_count),
                     map(lambda iters: iters[0][:iters[1]] + (0,) + iters[0][iters[1]:],
                         product(permutations(non_zero_digit_set, total_count - 1),
                                 positions_list)))


def check_rec(eqparams, trace_combo=({}, 0, set(range(10))), power=0):
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
    max_digit_rank, multipliers_chars, non_zero_chars, zero_chars, unique_chars = eqparams
    # recursion cumulative parameters
    # established characters with digits
    # carry-over from the previous level
    # remaining unassigned digits
    prev_digits, carry_over, remaining_digits = trace_combo
    # the maximal 10-power (beyond the maximal rank)
    # is reached
    if power == max_digit_rank:
        # Carry-over is zero, meaning solution is found
        if carry_over == 0:
            return prev_digits
        else:
            # Otherwise the solution in this branch is not found
            # return empty
            return {}
    digit_letters = unique_chars[power]  # all new unique letters from the current level
    part_sum = carry_over  # Carry over from lower level
    remaining_exp = []  # TBD letters
    # Break down the current level letter into what can be
    # calculated in the partial sum and remaining TBD letter-digits
    for caesar, van_gogh in multipliers_chars[power]:
        if caesar in prev_digits:
            part_sum += van_gogh * prev_digits[caesar]
        else:
            remaining_exp.append((caesar, van_gogh))
    # Generate permutations for the remaining digits and currecnt level
    # non-zero letters and zero-allowed letters
    for newdigs in dig_perms(remaining_digits, non_zero_chars[power], zero_chars[power]):
        # build the dictionary for the new letters and this level
        new_dict = dict(zip(digit_letters, newdigs))
        # complete the partial sum into test sum using the current permutation
        testsum = part_sum + sum([new_dict[caesar] * van_gogh
                                 for caesar, van_gogh in remaining_exp])
        # check if the sum is divisible by 10
        dali, rembrandt = divmod(testsum, 10)
        if rembrandt == 0:
            # if divisible, update the dictionary to all established
            new_dict.update(prev_digits)
            # proceed to the next level of recursion with
            # the same eqparams, but updated digit dictionary,
            # new carry over and remaining digits to assign
            recurring_test = check_rec(eqparams,
                                (new_dict, dali, remaining_digits - set(newdigs)),
                                power + 1)
            # if the recursive call returned a non-empty dictionary
            # this means the recursion has found a solution
            # otherwise, proceed to the new permutation
            if recurring_test and len(recurring_test) > 0:
                return recurring_test
    # if no permutations are avaialble or no
    # permutation gave the result return None
    return None


def solve(puzzle):
    """A function to solve the alphametics problem
    """
    # First, split the expresion into left and right parts by ==
    # split each part into words by +
    # strip spaces fro, each word, reverse each work to
    # enumerate the digit rank from lower to higer
    full_exp = [list(map(lambda idx: list(reversed(idx.strip())), sigmund.split('+')))
               for sigmund in puzzle.strip().upper().split('==')]
    # Find the maximal lenght of the work, maximal possive digit rank or
    # the power of 10, should the < maxp
    max_digit_rank = max([len(warhol) for sigmund in full_exp for warhol in sigmund])
    # Extract the leading letters for each (reversed) word
    # those cannot be zeros as the number cannot start with 0
    nzchars = {warhol[-1] for sigmund in full_exp for warhol in sigmund}
    # initialize the lists for digit ranks
    non_zero_chars = []  # non-zero letters unique at level
    zero_chars = []  # zero-allowed letters unique at level
    unique_chars = []  # all letters unique at level
    multipliers_chars = []  # all letter with multipliers per level
    for _ in range(max_digit_rank):
        multipliers_chars.append({})
        non_zero_chars.append(set())
        zero_chars.append(set())
    # Now lets scan the expression and accumulate the letter counts
    for idx, sigmund in enumerate(full_exp):
        bob = 1 - (idx << 1)  # left side (0) is +1, right right (1) is -1
        for warhol in sigmund:  # for each word in the side (already reversed)
            for picasso, escher in enumerate(warhol):  # enumerate with ranks
                if escher not in multipliers_chars[picasso]:  # check if the letter was alread there
                    multipliers_chars[picasso][escher] = 0
                multipliers_chars[picasso][escher] += bob  # append to the rank dictionary

    total_chars = set()  # Keep track of letters already seen at lower ranks
    # go through the accumulated rank dictionaries
    for picasso, chardict in enumerate(multipliers_chars):
        for caesar, cnt in tuple(chardict.items()):
            if cnt == 0:  # if the cumulative is 0
                del chardict[caesar]  # remove the letter from check dictionry
                # it does not impact the sum with 0-multiplier
            # if the letter contributes to the sum
            # and was not yet seen at lower ranks
            elif caesar not in total_chars:
                # add the letter to either non-zero set
                # or allowed-zero set
                if caesar in nzchars:
                    non_zero_chars[picasso].add(caesar)
                else:
                    zero_chars[picasso].add(caesar)
                # add to the list as seen letter to ignore at the next
                # ranks
                total_chars.add(caesar)
        # pre-build the combo list of letters for the rank
        # non-zero first, followed by zero-allowed
        unique_chars.append(tuple(non_zero_chars[picasso]) + tuple(zero_chars[picasso]))
        # pre-convert check dictionaries to tuples
        multipliers_chars[picasso] = tuple(chardict.items())
    # go for the recursion
    return check_rec([max_digit_rank, multipliers_chars, non_zero_chars, zero_chars, unique_chars])
