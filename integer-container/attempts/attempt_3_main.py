# ATTEMPT 3 - Fixed the type mismatch, converting both sides to int.
# But then used Python's built-in True/False (capitalized!) instead of the string "true"/"false"
# Python's boolean True != the string "true"
# The test expects lowercase string, not Python boolean

def solution(queries):
    container = []
    results = []
    for query in queries:
        if query[0] == "ADD":
            container.append(int(query[1]))
            results.append("")
        elif query[0] == "EXISTS":
            results.append(True if int(query[1]) in container else False)  # Python bool, not string!
    return results

# Expected: ["", "", "", "", "true", "true", "true", "false", "false", "false"]
# Actual:   ["", "", "", "",  True,   True,   True,  False,  False,  False ]
# Looks right when you print it but the TYPE is wrong -- bool not str
# This fails the automated test because True != "true"
