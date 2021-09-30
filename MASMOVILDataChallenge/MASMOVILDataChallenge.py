from airflow import DAG
from datetime import datetime, timedelta

default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'start_date': datetime(1900, 1, 1),
	'retries': 1,
	'retry_delay': timedelta(seconds=5)
}

dag=DAG(dag_id='test',default_args=default_args, schedule_interval="0 3 * * *")
	
	