from um import count

def test_um():
    assert count("um, hello, world") == 1
    assert count("um, hello, world, um") == 2
    assert count("hello, world") == 0
    assert count("yummy") == 0
    assert count("Um, hello") == 1
    