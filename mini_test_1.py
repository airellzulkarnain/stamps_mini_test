arr = [i+1 for i in range(100)]

def mutate_arr(n: int) -> int|str:
    if n % 3 == 0 and n % 5 == 0:
        return "FooBar"
    elif n % 3 == 0:
        return "Foo"
    elif n % 5 == 0:
        return "Bar"
    else:
        return n
    
arr = [i for i in map(mutate_arr, arr)]
print(*arr, sep=", ")
