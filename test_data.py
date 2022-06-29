#from src.data.create_data_lake import create_data_lake
from src.models.train_daily_model import train_daily_model

def test_create_data_lake():
    d = train_daily_model()
    assert  d == True 