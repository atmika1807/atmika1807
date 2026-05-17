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
