def all_eq(lst):
    max_item = max(lst, key=lambda x: len(x))
    max_len = len(max_item)
    return [item.ljust(max_len, '_') for item in lst]
print(all_eq(['м', 'макс', 'максимум']))