from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator


default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'start_date': datetime(1900, 1, 1),
	'retries': 1,
	'retry_delay': timedelta(seconds=5)
}

with DAG(dag_id='test',default_args=default_args, schedule_interval="0 3 * * *") as dag:

	# Task Start
	start = DummyOperator(task_id='start')
	# Task End
	end = DummyOperator(task_id='end')
	
	start >> end	
	
	