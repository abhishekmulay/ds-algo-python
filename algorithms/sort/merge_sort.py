def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) / 2
        left = arr[:middle]
        right = arr[middle:]
        print "[merge_sort] left=", left, " right=", right
        sortedLeft = merge_sort(left)
        print "[merge_sort] sortedLeft=", sortedLeft
        sortedRight = merge_sort(right)
        print "[merge_sort] sortedRight=", sortedRight
        result = merge(sortedLeft, sortedRight)
        print "[merge_sort] result=", result, "\n"
        return result


def merge(left, right):
    print "\tMerging: left=", left, " right=", right

    left_index, right_index = 0, 0
    temp = []
    while left_index < len(left) and right_index < len(right):
        left_item = left[left_index]
        right_item = right[right_index]

        if left_item < right_item:
            temp.append(left_item)
            left_index += 1
        else:
            temp.append(right_item)
            right_index += 1

    item_remaining_in_left = left_index < len(left)
    items_remaining_in_right = right_index < len(right)

    if item_remaining_in_left:
        for index in range(left_index, len(left)):
            temp.append(left[index])
    elif items_remaining_in_right:
        for index in range(right_index, len(right)):
            temp.append(right[index])

    arr = list(temp)
    print "\tMerged:", arr
    return arr


if __name__ == '__main__':
    data = [2, 4, 5, 7, 19, 1, 2, 3, 6]
    print "--------------------------------------------------------------------"
    print "\t\t\tUNSORTED: ", data
    print "--------------------------------------------------------------------"
    print "SORTED:", merge_sort(data)
