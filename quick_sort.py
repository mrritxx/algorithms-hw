table = [2,1,6,5,8,15,32,44]

def quick_sort(x):
    if len(x) <= 1:
        return x
    pivot = x[0]
    left = [i for i in x[1:] if i < pivot]
    right = [i for i in x[1:] if i >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(table))
