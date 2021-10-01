
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
	
	
	N=5
	task_n =[]

	for i in range(N):
		t = DummyOperator(task_id=f"task_{str(i)}", dag=dag)
		task_n.append(t) 
		if i>0 and i % 2 == 0:
			task_n[1::2]>>t
	
	start>>end
		 

	
	