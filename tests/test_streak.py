import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_example_from_prompt():
    """Test the primary example from the prompt."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive_numbers():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_same_positive_numbers():
    """Test a list with all same positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_with_zeros_and_negatives():
    """Test a mixed list of positive, zero, and negative numbers."""
    assert longest_positive_streak([1, 2, -3, 4, 0, 5, 6]) == 2

def test_longest_streak_at_beginning():
    """Test when the longest streak is at the start of the list."""
    assert longest_positive_streak([5, 6, 7, 8, -1, 2, 3]) == 4

def test_longest_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 2, -5, 4, 5, 6, 7]) == 4

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, -10, 0]) == 0

def test_single_positive_number():
    """Test a list with a single positive number."""
    assert longest_positive_streak([10]) == 1

def test_single_non_positive_number():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-10]) == 0
    assert longest_positive_streak([0]) == 0