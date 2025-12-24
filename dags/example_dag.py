from datetime import timedelta 

from airflow import DAG 
from airflow.opeartors.dummy_opeartor import DummyOperator
from airflow.utils.dates import days_ago 

with DAG(
    "example_dag",
    schedule_interval=None,
    start_date=days_ago(0),
    dargun_timeout=timedelta(minutes=60),
) as dag:
    
    dummy_task = DummyOperator(task_id="dummy_task")
    
    