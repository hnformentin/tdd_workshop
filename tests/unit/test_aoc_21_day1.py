from aoc_21.part_a import (
    read_input_as_list_int,
    depth_change,
    count_increased_depth,
    sliding_window,
)
import pytest


# Given with the read_input_as_list_int function
def test_read_input_as_list_int():
    file_name = "input_test_day1_a.txt"
    expected_result = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    result = read_input_as_list_int(file_name)
    assert result == expected_result


@pytest.mark.parametrize(
    "len_window,expected_result",
    [
        (1, [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]),
        (3, [607, 618, 618, 617, 647, 716, 769, 792]),
    ],
)
def test_sliding_window(len_window, expected_result):
    list_int_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    result = sliding_window(list_int_input, len_window)
    assert result == expected_result


# Only the test is given
def test_depth_change():
    list_int = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected_result = [
        "N/A - no previous measurement",
        "increased",
        "increased",
        "increased",
        "decreased",
        "increased",
        "increased",
        "increased",
        "decreased",
        "increased",
    ]
    result = depth_change(list_int)
    assert result == expected_result


# Only test is given, instruct to use @pytest.mark.parametrize
def test_count_increased_depth():
    list_depth_change = [
        "N/A - no previous measurement",
        "increased",
        "increased",
        "increased",
        "decreased",
        "increased",
        "increased",
        "increased",
        "decreased",
        "increased",
    ]
    expected_result = 7
    result = count_increased_depth(list_depth_change)

    assert expected_result == result


# Integration test: to make test and main function
# Refactor: names of files, have more tests for edge cases (validate input),
# use argparser
