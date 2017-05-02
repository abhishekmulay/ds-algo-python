def insertion_sort(data):
    print "UNSORTED: ", data

    for index in range(1, len(data)):
        item = data[index]
        j = index - 1

        while j >= 0 and item < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = item

    print "SORTED: ", data


if __name__ == '__main__':
    data = [5, 2, 4, 6, 1, 3]
    insertion_sort(data)
