import os


def read_input_as_list_int(file_name):
    dir_name = os.path.dirname(__file__)
    file_path = os.path.join(dir_name, "../data", file_name)

    assert os.path.isfile(file_path)

    with open(file_path, "r") as opened_file:
        list_str = opened_file.read().splitlines()
        list_int = list(map(int, list_str))

        return list_int


def sliding_window(list_int_input, len_window):
    list_int_output = []
    for index, _ in enumerate(list_int_input):
        if index <= len(list_int_input) - len_window:
            sum_slide_window = sum(list_int_input[index : index + len_window])
            list_int_output.append(sum_slide_window)
    return list_int_output


def depth_change(list_int):
    list_depth_change = list()
    previous_depth = None
    for index, depth in enumerate(list_int):
        if index == 0:
            list_depth_change.append("N/A - no previous measurement")
            previous_depth = depth
        else:
            if depth - previous_depth > 0:
                list_depth_change.append("increased")
            elif depth - previous_depth < 0:
                list_depth_change.append("decreased")
            else:
                list_depth_change.append("no change")
            previous_depth = depth

    return list_depth_change


def count_increased_depth(list_depth_change):
    total_increased_depth = 0
    for depth_change in list_depth_change:
        if depth_change == "increased":
            total_increased_depth += 1

    return total_increased_depth


def main():
    list_int_input = read_input_as_list_int("input_hnfo_day1_a.txt")
    list_int_slidding_window = sliding_window(list_int_input, 3)
    list_depth_change = depth_change(list_int_slidding_window)
    return count_increased_depth(list_depth_change)


if __name__ == "__main__":
    total_increased_depth = main()
    print(total_increased_depth)
