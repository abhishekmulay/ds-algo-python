def insertion_sort(data):
    print "UNSORTED: ", data

    # main loop counter goes from left to right
    for index in range(1, len(data)):
        item = data[index]
        j = index - 1

        # checking in sorted portion from right to left
        while j >= 0 and item < data[j]:
            data[j + 1] = data[j]
            j = j - 1

        # insert item into sorted sequence data[0...(index-1)]
        data[j + 1] = item

    print "SORTED: ", data


if __name__ == '__main__':
    data = [5, 2, 4, 6, 1, 3]
    insertion_sort(data)
