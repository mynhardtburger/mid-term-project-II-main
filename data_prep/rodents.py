import pandas as pd


def convert_to_parquet(load_path: str, save_path: str) -> None:
    """Read rodent activity data and save it to parquet format for faster future processing

    Parameters:
        path (str): Path to NYC rodent inspection csv dataset
    """

    data = pd.read_csv(load_path, parse_dates=["INSPECTION_DATE"])
    data.to_parquet(save_path)


def query_data(
    load_path: str,
    start_date: str,
    end_date: str,
    inspection_type: list[str],
    result: list[str],
) -> pd.DataFrame:
    """Read parquet rodent activity data, apply date, inspection type and result filters and return a resulting dataframe.

    Parameters:
        load_path (str): Path to parquet rodent inspection dataset
        start_date (str): Start date
        end_date (str): End date
        inspection_type (list[str]):    ['Initial', 'BAIT', 'Compliance', 'STOPPAGE', 'CLEAN_UPS']
        result (list[str]): ['Passed', 'Bait applied', 'Failed for Other R', 'Rat Activity', 'Monitoring visit', 'Stoppage done', 'Cleanup done', nan]

    Return:
        DataFrame
    """
    data = (
        pd.read_parquet(load_path)
        .query(
            "`INSPECTION_DATE` >= @start_date and `INSPECTION_DATE` <= @end_date and `INSPECTION_TYPE` in @inspection_type and `RESULT` in @result"
        )
        .copy()
    )

    return data
