from typing import Optional

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
from pathlib import Path
import pytest


def save(df: pd.DataFrame, save_path: Path, num_rows: Optional[int] = None):
    if not df.empty: 
        if num_rows: 
            num_rows = validate_num_rows(num_rows)
            df = df[0: num_rows]
        df.to_csv(save_path, index=False)
    else:
        print("Nothing to save. ")

def validate_num_rows(num_rows)-> int:
    if not int(num_rows) == num_rows:
        raise ValueError(f"num_rows must be int, got {num_rows}")
    if num_rows < 1:
        raise ValueError(f"num_rows must be >= 1, got {num_rows}")
    return int(num_rows)
        
        
@pytest.fixture()
def test_dataframe():
    df = pd.DataFrame(columns=["a", "b", "c"], data=[3, 2, 1]*np.ones([5,3]))
    return df


@pytest.mark.parametrize("number_of_rows", [None, 3])
def test_save_fixturized(tmp_path, test_dataframe, number_of_rows):
    save_path = tmp_path / "df.csv"
    save(test_dataframe, save_path, num_rows=number_of_rows)

    df_actual = pd.read_csv(save_path)
    if number_of_rows:
        expected_df = test_dataframe[0:number_of_rows]
    else: 
        expected_df = test_dataframe
        
    assert_frame_equal(expected_df, df_actual)


    
@pytest.mark.parametrize(
    "input_num_rows, expected_output, expected_error", 
    [
        (3, 3, None),
        (2.0, 2, None),
        ("text", None, ValueError),
        ("3.4", None, ValueError),
        (-1, None, ValueError),
    ], 
    ids=[
        "integer",
        "float_that_can_be_converted_to_integer",
        "string_fails",
        "float_fails",
        "negative_number_fails"
    ]
)
def test_validate_num_rows(input_num_rows, expected_output, expected_error):
    if expected_error:
        with pytest.raises(expected_error):
            validate_num_rows(input_num_rows)
    else:
        actual_output = validate_num_rows(input_num_rows)
        assert expected_output == actual_output