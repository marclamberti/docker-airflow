from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello Wolrd'

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 14, 16, 12),
    'schedule_interval': '0 * * * *',
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

with DAG(dag_id='hello_world_dag2', 
         default_args=args) as dag:

    start_dag = DummyOperator(task_id='START_dag')

    #hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

    end_dag1 = DummyOperator(task_id='END1_dag')

    end_dag2 = DummyOperator(task_id='END2_dag')

    hello_pattern = dict()

    for i in range(5):

        hello_pattern[i] = PythonOperator(task_id='hello_task_{}'.format(i), python_callable=print_hello, dag=dag)
        
        start_dag >> hello_pattern[i] >> end_dag1

    end_dag1 >> end_dag2