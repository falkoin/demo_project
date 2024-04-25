from unittest import TestCase
from main import say_hi


class TestApp(TestCase):
    def test_say_hi(self) -> None:
        # given
        name = "someone"
        # when
        result = say_hi(name)
        # then
        self.assertEqual("Hi, someone! You are awesome!", result)
