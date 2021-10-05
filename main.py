def build_stats(capture):
    # Calling functions to gather stats within a list
    # Inverting the list to get the greater to optimize the program
    stats = [less(capture, 4), between(capture, 3, 6), greater(capture[::-1], 4)]
    return stats


def less(l_capture, n_less):
    # Getting the amount of numbers less than 4
    count = 0
    for i in l_capture:
        if i < n_less:
            count += 1
        else:
            break
    return count


def between(b_capture, n1, n2):
    # Getting the amount of numbers between 3 and 6
    count = 0
    for i in b_capture:
        if n1 <= i <= n2:
            count += 1
        else:
            break
    return count


def greater(g_capture, n_great):
    # Getting the amount of numbers greater than 4
    count = 0
    for i in g_capture:
        if i > n_great:
            count += 1
        else:
            break
    return count


def data_capture():
    # Capturing user input data for the list
    capture1 = []
    while True:
        i = (input("Please enter a digit to be added to the list or hit enter to end the list"))
        if i == "": break
        capture1.append(int(i))
    return capture1


if __name__ == '__main__':
    capture = data_capture()
    sorted_capture = sorted(capture)
    # Print on the screen the results
    print(f"Original Capture: ", capture)
    print(f"Less ", build_stats(sorted_capture)[0])
    print(f"Between ", build_stats(sorted_capture)[1])
    print(f"Greater ", build_stats(sorted_capture)[2])
