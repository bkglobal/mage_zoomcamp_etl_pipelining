import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def load_single_chunk(url: str, taxi_data_types, parse_dates):
    return pd.read_csv(url, sep=',', compression="gzip", dtype=taxi_data_types, parse_dates=parse_dates)

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url_quarter_10 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url_quarter_11 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url_quarter_12 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'

    taxi_data_types = {

        "VendorID": pd.Int64Dtype(),
        "passenger_count":  pd.Int64Dtype(),
        "trip_distance": float,
        "RatecodeID": pd.Int64Dtype(),
        "store_and_fwd_flag": str,
        "PULocationID": pd.Int64Dtype(),
        "DOLocationID": pd.Int64Dtype(),
        "payment_type": pd.Int64Dtype(),
        "fare_amount": float,
        "extra": float,
        "mta_tax": float,
        "tip_amount": float,
        "tolls_amount": float,
        "improvement_surcharge": float,
        "total_amount": float,
        "congestion_surcharge": float
    }

    parse_dates = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]


    all_data_frames = [load_single_chunk(frame, taxi_data_types, parse_dates) for frame in [url_quarter_10, url_quarter_11, url_quarter_12]]
    final_data_frame = pd.concat(all_data_frames)
    # for url in [url_quarter_10, url_quarter_11, url_quarter_12]:
    #     green_taxi_data = pd.read_csv(url, sep=',', compression="gzip", dtype=taxi_data_types, parse_dates=parse_dates)
    #     all_data.merge(green_taxi_data)

    return final_data_frame


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
