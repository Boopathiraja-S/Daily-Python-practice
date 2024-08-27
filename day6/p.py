a = list(map(int, input().strip()))
odd = 0
even = 0
for i in a:
    if i %2 ==0:
        even += i
    else:
        odd += i
if even>odd:
    print("even:")
    print(even)
else:
    print("odd:")
    print(odd)
