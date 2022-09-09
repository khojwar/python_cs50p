'''
from hello import hello

def test_hello():
    assert hello("tika") == "hello, tika"
    assert hello() == "hello, world"
'''


'''
# making more clear 
from hello import hello

def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("tika") == "hello, tika"
'''



# using loop
from hello import hello

def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["hermione", "harry", "ron"]:
        assert hello(name) == f"hello, {name}"

