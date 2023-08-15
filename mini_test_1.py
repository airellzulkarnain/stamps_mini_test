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
for i in range(len(arr), 0, -1):
        is_prime = True
        for num in range(2, i):
            if (i % num) == 0:
                is_prime = False
                break
        if i == 1:
            print(arr[i-1], end=", ")
        elif not is_prime:
            print(arr[i-1], end=", ")
