def merge_arr(left, right, destination):
    print "Merging| left:", left, " right:", right
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        left_item = left[left_index]
        right_item = right[right_index]
        if left_item < right_item:
            destination.append(left_item)
            left_index = left_index + 1
        else:
            destination.append(right_item)
            right_index = right_index + 1

    print "left_index:", left_index, "right_index:", right_index, \
        "len(left):", len(left), "len(right):", len(right)
    elements_remaining_in_left_arr = left_index < len(left)
    elements_remaining_in_right_arr = right_index < len(right)
    if elements_remaining_in_left_arr:
        for index in range(left_index, len(left)):
            destination.append(left[index])
    elif elements_remaining_in_right_arr:
        for index in range(right_index, len(right)):
            destination.append(right[index])

    print "Merged: ", destination
    return destination


def merge_sort(arr, start, end):
    # print "[merge_sort] arr:", arr, "start:", start, "end:", end
    # print "UNSORTED: ", arr
    if start < end:
        mid = (start + end) / 2
        print "merge_sort(arr=", arr, ") start=", start, "end=", mid
        merge_sort(arr, start, mid)
        print "merge_sort(arr=", arr, ") start=", mid + 1, "end=", end
        merge_sort(arr, mid + 1, end)

        merge(arr, start, mid, end)
        # print "SORTED: ", result


def merge(arr, start, mid, end):
    temp = []
    left = arr[start:mid]
    right = arr[mid:end]
    # print "\t\t[merge] left:", left, "right:", right, "start:", start, "mid:", mid, "end:", end

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        left_item = left[left_index]
        right_item = right[right_index]

        if left_item <= right_item:
            temp.append(left_item)
            left_index += 1
        elif right_item < left_item:
            temp.append(right_item)
            right_index += 1

    # print "left_index:", left_index, "right_index:", right_index, \
    #     "len(left):", len(left), "len(right):", len(right)

    left_elements_remaining = left_index < len(left)
    right_elements_remaining = right_index < len(right)

    if left_elements_remaining:
        for i in range(left_index, len(left)):
            temp.append(left[i])
    elif right_elements_remaining:
        for i in range(right_index, len(right)):
            temp.append(right[i])

    arr = list(temp)
    print "SORTED:", arr


if __name__ == '__main__':
    data = [2, 4, 5, 7, 1, 2, 3, 6]
    print "--------------------------------------------------------------------"
    print "\t\t\tUNSORTED: ", data
    print "--------------------------------------------------------------------"
    merge_sort(data, 0, len(data))

    # a = [2, 4, 5, 7, 19]
    # b = [1, 2, 3, 6]
    # c = a + b
    # merge(c, 0, 5, 10)
