def test_user_login():
    print("Hello!")


class TestUserLogin:
    def test_1(self):
        ...

    def test_2(self):
        ...


def test_assert_positive_case():
    assert 2 + 2 == 4
    assert 2 + 2 == 3
    assert 2 + 2 == 7

def test_assert_negative_case():
    four = 2 + 2
    assert four == 6, "2+2 != 6"