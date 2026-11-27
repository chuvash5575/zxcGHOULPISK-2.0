def add(a: int, b: int) -> int:
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
