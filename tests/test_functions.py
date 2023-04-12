import utils_test
utils_test.load_path()
from src.biomodels_restful_ws_tnguyenv import main

def test_add_one():
    assert 4 == main.add_one(3)

