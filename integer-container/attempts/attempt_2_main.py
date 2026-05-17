# ATTEMPT 2 - Added results.append("") for ADD. Good.
# But converted query[1] to int for storage, then forgot to convert when checking EXISTS
# Comparing string "5" against int 5 in Python -- they are NOT equal!
# So all EXISTS checks return "false" even when the value is in the container

def solution(queries):
    container = []
    results = []
    for query in queries:
        if query[0] == "ADD":
            container.append(int(query[1]))   # stored as int
            results.append("")
        elif query[0] == "EXISTS":
            results.append("true" if query[1] in container else "false")  # checked as string!
    return results

# Expected: ["", "", "", "", "true", "true", "true", "false", "false", "false"]
# Actual:   ["", "", "", "", "false", "false", "false", "false", "false", "false"]
# "5" in [1, 2, 5, 2] is False because str != int in Python
