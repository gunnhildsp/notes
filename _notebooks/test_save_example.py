import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
from pathlib import Path
import pytest


def save(df: pd.DataFrame, save_path: Path):
    if not df.empty:
        df.to_csv(save_path, index=False)
    else:
        print("Nothing to save. ")


def test_save(tmp_path):
    # Given
    save_path = tmp_path / "df.csv"
    df_expected = pd.DataFrame(columns=["a", "b", "c"], data=[3, 2, 1]*np.ones([5,3]))
    save(df_expected, save_path)

    # When 
    df_actual = pd.read_csv(save_path, index_col=False)

    # Then 
    assert_frame_equal(df_expected, df_actual)


@pytest.fixture()
def test_dataframe():
    df = pd.DataFrame(columns=["a", "b", "c"], data=[3, 2, 1]*np.ones([5,3]))
    return df


@pytest.fixture(params=[True, False], ids=["non-empty", "empty"])
def dataframes(request):
    if request.param:
        return pd.DataFrame(columns=["a", "b", "c"], data=[3, 2, 1]*np.ones([5,3]))
    else:
        return pd.DataFrame()
    
def test_save_fixturized(tmp_path, test_dataframe):
    # Given
    save_path = tmp_path / "df.csv"
    save(test_dataframe, save_path)

    # When 
    df_actual = pd.read_csv(save_path, index_col=False)

    # Then 
    assert_frame_equal(test_dataframe, df_actual)


@pytest.fixture(params=[{"non_empty": True, "length": 5}, {"non_empty": False, "length": None}], ids=["non-empty", "empty"])
def df_tuplefixture(request):
    if request.param["non_empty"]:
        n = request.param["length"]
        return pd.DataFrame(columns=["a", "b", "c"], data=[3, 2, 1]*np.ones([n,3]))
    else:
        return pd.DataFrame()
    
def test_save_parametrized_fixture(tmp_path, dataframes):
    # Given
    save_path = tmp_path / "df.csv"
    save(dataframes, save_path)

    # When 
    if dataframes.empty:
        # Then 
        files_in_dir = [x for x in tmp_path.iterdir() if x.is_file()]
        assert not files_in_dir
        
    # Other when
    else:
        df_actual = pd.read_csv(save_path, index_col=False)

        # Then 
        assert_frame_equal(dataframes, df_actual)

def test_save_parametrized_fixture2(tmp_path, df_tuplefixture):
    # Given
    save_path = tmp_path / "df.csv"
    save(df_tuplefixture, save_path)

    # When 
    if df_tuplefixture.empty:
        # Then 
        files_in_dir = [x for x in tmp_path.iterdir() if x.is_file()]
        assert not files_in_dir
        
    # Other when
    else:
        df_actual = pd.read_csv(save_path, index_col=False)

        # Then 
        assert_frame_equal(df_tuplefixture, df_actual)
        
        
def test_demo_fail_output(dataframes):
    if dataframes.empty:
        assert False
    else: 
        assert True