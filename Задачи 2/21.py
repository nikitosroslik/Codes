def find_median(numbers):
    numb = sorted(numbers)
    length = len(numbers)
    mid = length // 2
    if length % 2 == 0:
        median = (numb[mid - 1] + numb[mid]) / 2
    else:
        median = numb[mid]
    return median
numbers = [1,2,3,4,5]
median = find_median(numbers)
print(median)

