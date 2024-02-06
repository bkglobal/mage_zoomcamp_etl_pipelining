from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path
import pyarrow as pa
import pyarrow.parquet as pq



if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ[ 'GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/verdant-current-393218-c0e87b0ec239.json"
bucket_name = 'mage-zoomcamp-bucket'
project_id = 'verdant-current-393218'
table_name = "green_taxi"
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    
    table = pa.Table.from_pandas(df)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_datast(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )
