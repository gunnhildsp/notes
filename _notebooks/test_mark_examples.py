import pytest

@pytest.mark.this
def test_example():
    print("Hello")
    assert True

@pytest.mark.this
@pytest.mark.that
def test_several_marks():
    print("Nothing")
    assert True

def test_unmarked():
    print("Hello")
    assert 1
