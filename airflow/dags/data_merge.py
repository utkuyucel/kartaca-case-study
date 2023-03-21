from airflow.decorators import dag, task
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime
import requests

## DAG 3 - "data_merge"
@dag(default_args={"owner": "kartaca"}, start_date=datetime(2023, 3, 21), schedule_interval="0 20 * * *")
def data_merge():
    # Task 1
    @task
    def start_task():
        print("DAG started!") 


    # Task 2
    @task 
    def merge_data(): 
        mysql_hook = MySqlHook(mysql_conn_id="mysql_default") 
        
        sql_query = """
        TRUNCATE TABLE country_currency.data_merge;
        INSERT INTO country_currency.data_merge (code, name, currency)
        SELECT c.code, c.name, cu.currency FROM country_currency.country c JOIN country_currency.currency cu ON c.code = cu.code;
        """
        
        mysql_hook.run(sql_query)


    #Task 3
    @task 
    def end_task():
        print("DAG finished") 

    start_task = start_task() 
    merge_data = merge_data()
    end_task = end_task()


data_merge_dag = data_merge()

