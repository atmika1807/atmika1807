# ATTEMPT 2
# ok two things to fix:
# - underscores in base: need to strip them before int()
# - i is off by one: the existing code already does i += 1 after ...
#   so i should point AT the '#', not past it
#
# also wait -- what if base_str has letters in it like 'ab#xyz#'?
# int('ab') will crash too. i'll deal with that after

def solution(line):
    atLeastOneDigit = False
    if line[len(line) - 1] == '#':
        i = 0
        base = 0

        # my fill-in v2:
        hash_idx = line.find('#')
        base_str = line[:hash_idx].replace('_', '')
        base = int(base_str) if base_str else 0   # empty -> 0, will fail base<2 check anyway
        i = hash_idx    # point AT '#', then the existing i+=1 moves past it correctly

        if base < 2 or base > 16:
            return False
        i += 1
        while i < len(line) - 1:
            if line[i] != '_':
                digit = -1
                if 'a' <= line[i] and line[i] <= 'f':
                    digit = ord(line[i]) - ord('a') + 10
                if 'A' <= line[i] and line[i] <= 'F':
                    digit = ord(line[i]) - ord('A') + 10
                if '0' <= line[i] and line[i] <= '9':
                    digit = ord(line[i]) - ord('0')
                if 0 <= digit and digit < base:
                    atLeastOneDigit = True
                else:
                    return False
            i += 1
    else:
        for i in range(len(line)):
            if line[i] != '_':
                if '0' <= line[i] and line[i] <= '9':
                    atLeastOneDigit = True
                else:
                    return False
    return atLeastOneDigit

# still crashes!
# test case: something like 'ab#xyz#' -> base_str = 'ab' -> int('ab') -> ValueError
# the problem says base must be a number (format 1 = decimal digits only)
# so 'ab#xyz#' should return False, but we crash instead of returning False cleanly
# need to handle non-digit characters in the base section
