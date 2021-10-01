from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from timediff_operator import TimeDiffOperator



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
	
	task_n[1::2]>> task_n[0]
	start>>end
	
	
with dag:	
	diffTimeTask = TimeDiffOperator(task_id='diffTimeTask',input_date=datetime(2012, 3, 5, 23, 8, 15))
	diffTimeTask