import pytest

from second_part.src import div, raise_something, add, ForceToList, random_gen, get_info


def test_generator():
    g = random_gen()
    assert isinstance(g, type((x for x in [])))
    a = next(g)
    while a != 15:
        assert 10 <= a <= 20
        a = next(g)
    with pytest.raises(StopIteration):
        next(g)


def test_to_str():
    assert add(5, 30) == '35'
    assert get_info({'info': [1, 2, 3]}) == '[1, 2, 3]'


def test_ignore_exception():
    assert div(10, 2) == 5
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)


def test_meta_list():
    test = ForceToList([1, 2])
    assert test[1] == 2
    assert test.x == 4

