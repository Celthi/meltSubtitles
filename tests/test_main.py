from meltsubtitles.main import (
    get_page,
    translate2chinese,
    translate2english,

)
def test_translate2chinese():
    assert "测试" in translate2chinese("test")

# this seems has problem
def test_translate2english():
    assert translate2english("测试") == ""

def test_get_page():
    assert  "baidu" in get_page("https://www.baidu.com", "").decode()
