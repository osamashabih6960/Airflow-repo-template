from datetime import timedelta

from airflow import DAG 
from airflow.utils.dates import days_ago 
from modules.custom_operator_example import ExamplePluginOperator


with DAG(
    "custom_operator_dag",
    schedule_interval=None,
    start_date=days_ago(0),
    dagrun_timeout=timedelta(minutes=60),
    
    
) as dsg:
    plugin_task = ExamplePluginOperator(
        task_id="plugin_task",message="here is the message!"
    )