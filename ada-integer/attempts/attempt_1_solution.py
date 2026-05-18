# ATTEMPT 1
# ok so i need to fill in the ... part
# the code already handles the digit loop, i just need to get the base number
# easiest thing - split on '#' and grab the first part
# i already know last char is '#' so we're in the base-number branch

def solution(line):
    atLeastOneDigit = False
    if line[len(line) - 1] == '#':
        i = 0
        base = 0

        # my fill-in:
        parts = line.split('#')
        base = int(parts[0])      # just convert the base part directly
        i = len(parts[0]) + 1    # move i past the base AND the '#'

        if base < 2 or base > 16:
            return False
        i += 1   # <-- wait this moves i ONE MORE time... so i'm now 2 past '#'
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

# TWO bugs:
# 1. int(parts[0]) crashes on underscores like '1_6#abc#' -> int('1_6') -> ValueError
# 2. i is set to len(parts[0]) + 1 (already past '#'), then i += 1 runs again
#    so for '16#abc#', i lands at index 4 instead of 3, skipping the first digit 'a'
# ran it on '16#abc#' and got wrong answer, printed i to debug, saw it was off by one
