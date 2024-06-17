def max_count(s):
    compte = 1
    lt = []
    for i in s:
        if i not in lt:
            lt.append(i)
        elif i in lt:
            compte += 1
    print(compte)
    return compte
        
max_count("ABCA")