from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


"""
    https://data.laadsdaac.earthdatacloud.nasa.gov/s3credentialsREADME
    https://ladsweb.modaps.eosdis.nasa.gov/learn/how-to-access-laads-daac-data-files-using-s3-direct-access/
    https://www.youtube.com/watch?v=8gmNySwnh2k
    https://ladsweb.modaps.eosdis.nasa.gov/learn/download-files-using-laads-daac-tokens/
    OPENDAP: https://ladsweb.modaps.eosdis.nasa.gov/learn/using-laads-apis/
    Instructons: https://www.opendap.org/documentation/QuickStart.html     
"""

dag = DAG(
    'get_aws_earth_data',
    description='Testing AWS Bucket for Earth Data data dump',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
)

_get_from_bucket_task = BashOperator(
    task_id='get_from_bucket_task',
    bash_command=' curl ',
    dag=dag,
)
