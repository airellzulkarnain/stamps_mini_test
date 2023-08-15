arr = [i+1 for i in range(100)]
    
for i in arr[::-1]:
        is_prime = True
        for num in range(2, i):
            if (i % num) == 0:
                is_prime = False
                break
        if i == 1:
            print(i, end=", ")
        elif not is_prime:
            if i % 3 == 0 and i % 5 == 0: 
                 print("FooBar", end=", ")
            elif i % 5 == 0 :
                 print("Bar", end=", ")
            elif i % 3 == 0 :
                 print("Foo", end=", ")
            else: 
                print(i, end=", ")
