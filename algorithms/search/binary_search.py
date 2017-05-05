def binary_search(data, search_val):
    mid = len(data) / 2
    print "Searching for", search_val, "in:", data, " mid:", mid

    if len(data) <= 1:
        return mid == search_val

    if search_val == mid:
        return True
    elif search_val < mid:
        left_half = data[:mid]
        return binary_search(left_half, search_val)
    elif search_val > mid:
        right_half = data[mid:]
        return binary_search(right_half, search_val)


if __name__ == '__main__':
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search_val = 22
    found = binary_search(data, search_val)
    print found