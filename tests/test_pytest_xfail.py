import pytest

@pytest.mark.xfail(reasone="Найден баг в приложении, из-за которого тест падает с ошибкой")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reasone="Баг уже исправлен но на тесте висит маркировка xfail")
def test_without_bug():
    ...
