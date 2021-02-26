

def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            current = l[index]
            previous = l[index - 1]

            if current < previous:
                l[index] = previous
                l[index-1] = current


def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            current_h, current_m = l[index]

            previous_h, previous_m = l[index - 1]

            if (current_h > previous_h) or (current_h == previous_h and current_m > previous_m):
                l[index] = (previous_h, previous_m)
                l[index-1] = (current_h, current_m)

            # if current_h > previous_h:
            #     l[index] = (previous_h, previous_m)
            #     l[index-1] = (current_h, current_m)
            # elif current_h == previous_h:
            #     if current_m > previous_m:
            #         l[index] = (previous_h, previous_m)
            #         l[index - 1] = (current_h, current_m)


if __name__ == '__main__':
    wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
    bubble_sort_1(wakeup_times)
    print("Pass" if (wakeup_times[0] == 3) else "Fail")

    # Entries are (h, m) where h is the hour and m is the minute
    sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]
    bubble_sort_2(sleep_times)
    print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")