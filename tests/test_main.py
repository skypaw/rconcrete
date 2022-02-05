from src.main import sample_function

def test_addition():
    test = sample_function(4)
    print('test')
    assert 8 == test