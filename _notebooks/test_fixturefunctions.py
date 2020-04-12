import numpy as np
import pandas as pd
import pytest

def data_handling(df: pd.DataFrame):
    new_col_name = "".join([c for c in df.columns])
    print(new_col_name)
    

@pytest.fixture()
def data():
    return pd.DataFrame(columns=["a", "b", "c"], data=[3, 2, 1]*np.ones([5,3]))


def test_data_handling(data):
    data_handling(data)
