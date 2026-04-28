def rolar_dados (n):
    import random 
    result = []
    for i in range(n):
        result.append(random.randint(1,6))
    return result