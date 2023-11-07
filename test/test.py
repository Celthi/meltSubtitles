import unittest

from meltsubtitles.main import get_page, translate2chinese, translate2english


class TestStringMethods(unittest.TestCase):
    def test_translate2chinese(self):
        self.assertIn("测试", translate2chinese("test"))

    # this seems has problem
    def test_translate2english(self):
        self.assertEqual(translate2english("测试"), "")

    def test_get_page(self):
        self.assertRegex(get_page("https://www.baidu.com", "").decode(), "baidu")


if __name__ == "__main__":
    unittest.main()
