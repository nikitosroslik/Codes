def count_lucky_numbers(length):
    if length == 1:
        return 0
    count = 0
    for i in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
        left_part = str(i).zfill(length // 2)
        left_sum = sum(map(int, left_part))
        for j in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
            right_part = str(j).zfill(length // 2)
            right_sum = sum(map(int, right_part))
            if left_sum == right_sum:
                count += 1
    return count
length = 4
result = count_lucky_numbers(length)
print(result)
