result = {}
for k in range(3, 21):
    a = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                a += str(i) + str(j)
    result[k] = a
    print(f"{k}: '{result[k]}'")

