# ATTEMPT 1 - First instinct: just loop the queries and handle ADD/EXISTS
# Forgot that ADD also needs to return something (an empty string "")
# So the output array ends up shorter than expected -- only EXISTS results are in it

def solution(queries):
    container = []
    results = []
    for query in queries:
        if query[0] == "ADD":
            container.append(query[1])   # add the value, but return nothing
        elif query[0] == "EXISTS":
            results.append("true" if query[1] in container else "false")
    return results

# Expected: ["", "", "", "", "true", "true", "true", "false", "false", "false"]
# Actual:   ["true", "true", "true", "false", "false", "false"]
# Missing the four empty strings for the ADD operations!
