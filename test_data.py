#from src.data.create_data_lake import create_data_lake
from src.features.make_features import make_features

def test_create_data_lake():
    d = make_features()
    assert  d == True 