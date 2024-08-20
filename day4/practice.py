n = 5
for i in range(n):
    for j in range(1, n):
        if i % j != 0:
            print(i, end=" ")
        else:
            print(i+1, end=" ")
    print()