# ATTEMPT 4 - Final fix: use the actual strings "true" and "false" (lowercase)
# Also switched to a set for faster lookups (though a list works too for small inputs)

def solution(queries):
    container = set()
    results = []
    for query in queries:
        if query[0] == "ADD":
            container.add(int(query[1]))
            results.append("")
        elif query[0] == "EXISTS":
            results.append("true" if int(query[1]) in container else "false")
    return results

# Expected: ["", "", "", "", "true", "true", "true", "false", "false", "false"]
# Actual:   ["", "", "", "", "true", "true", "true", "false", "false", "false"]
# Correct!
