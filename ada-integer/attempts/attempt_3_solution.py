# ATTEMPT 3
# ok forget the split approach, it keeps having edge cases
# look at the digit loop already in the code -- it goes char by char with i
# i'll just do the same thing for the base section
# that way i is naturally in the right place when the loop ends (pointing at '#')
# and i don't need to calculate any offsets

def solution(line):
    atLeastOneDigit = False
    if line[len(line) - 1] == '#':
        i = 0
        base = 0

        # my fill-in v3 - just loop character by character like the rest of the code
        while line[i] != '#':
            if line[i] != '_':
                if not line[i].isdigit():
                    return False          # invalid char in base section
                base = base * 10 + int(line[i])
            i += 1
        # when loop ends, line[i] == '#' and i is exactly where it needs to be

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

# tested all examples:
# '123_456_789' -> else branch (no trailing #), digits only -> True  v
# '16#123abc#'  -> base=16, digits 1,2,3,a,b,c all < 16 -> True  v
# '10#123abc#'  -> base=10, 'a' = 10, 10 < 10 is False -> return False  v
# '10#10#123ABC#' -> base=10, hits '#' in digit section -> digit=-1 -> return False  v
# '10#0#'       -> base=10, digit 0 valid -> True  v
# '10##'        -> base=10, no digits -> atLeastOneDigit stays False -> return False  v
# all pass!
