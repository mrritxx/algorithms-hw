table = [2,1,6,5,8,15,32,44]

def bubble_sort(x):
    for j in range(len(x) - 1):
        for i in range(len(x) - 1):
            if int(x[i]) > int(x[i + 1]):
                x[i], x[i + 1] = x[i + 1], x[i]
    return x

print(bubble_sort(table))
