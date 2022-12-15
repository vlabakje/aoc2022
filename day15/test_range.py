import two

def test_range():
    r = two.Range(0, 20)
    r.occupy(-10, 10)
    assert not r.covered()
    r.occupy(10, 25)
    assert r.covered()
    r = two.Range(0, 20)
    r.occupy(0, 8)
    r.occupy(12, 16)
    r.occupy(9, 13)
    r.occupy(15, 20)
    assert r.covered()
