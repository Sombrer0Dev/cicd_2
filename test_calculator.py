from calculator import add


def test_add():
    assert add(2, 3) == 5, "Сложение не работает"
    assert add(-1, 1) == 0, "Сложение не работает"
    assert add(0, 0) == 0, "Сложение не работает"
