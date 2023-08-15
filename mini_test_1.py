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
arr = arr[::-1]
for i in arr:
    if isinstance(i, int):
        is_prime = True
        for num in range(2, i):
            if (i % num) == 0:
                is_prime = False
                break
        if i == 1:
            print(i, end=", ")
        elif not is_prime:
            print(i, end=", ")

    else:
        print(i, end=", ")
