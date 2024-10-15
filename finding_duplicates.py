def find_duplicates(arr):
    hash_table = {}
    duplicates = []

    for num in arr:
        if num in hash_table:
            duplicates.append(num)
        else:
            hash_table[num] = True

    return duplicates

arr = [1, 2, 3, 4, 3, 2, 5, 1, 6, 9, 5, 6]
print(find_duplicates(arr))
