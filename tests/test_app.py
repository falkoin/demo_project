from unittest import TestCase
from main import say_hi, say_reverse


class TestApp(TestCase):
    def test_say_hi(self) -> None:
        # given
        name = "someone"
        # when
        result = say_hi(name)
        # then
        self.assertEqual("Hi, someone! You are awesome!", result)
    def test_say_reverse(self) -> None:
        # given
        name = "someone"
        # when
        result = say_reverse(name)
        # then
        self.assertEqual("Hi, enoemos! You are awesome!", result)
