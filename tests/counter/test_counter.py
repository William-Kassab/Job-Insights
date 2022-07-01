from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word1 = "Python"
    result1 = 1639
    word2 = "Javascript"
    result2 = 122
    assert count_ocurrences(path, word1) == result1
    assert count_ocurrences(path, word2) == result2
