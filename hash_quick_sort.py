def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]
    left = [number for number in numbers if number < pivot]
    middle = [number for number in numbers if number == pivot]
    right = [number for number in numbers if number > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def hash_sort(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    result = []
    for number in quick_sort(list(counts)):
        result.extend([number] * counts[number])

    return result


print(hash_sort([4, -2, 4, 1, 0]))
