l = [161,182,161,154,176,170,167,171,170,174]

def average(array):
    sets = set(array)
    result = sum(sets)/len(sets)
    return result

print(average(l))
