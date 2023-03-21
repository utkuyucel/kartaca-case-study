from airflow.decorators import dag, task
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime
import requests

## DAG 2 - "currency"
@dag(default_args={"owner": "kartaca"}, start_date=datetime(2023, 3, 21), schedule_interval="0 15 * * *")
def currency():
    # Task 1
    @task
    def start_task():
        print("DAG started!") 

    # Task 2
    @task
    def fetch_json():
        url = "http://country.io/currency.json" 
        response = requests.get(url) 
        data = response.json() 
        return data

    # Task 3
    @task 
    def insert_json(data): # Input data is coming from "fetch_json()" task's output 
        mysql_hook = MySqlHook(mysql_conn_id="mysql_default") 
        
        for id, name in data.items(): 
            sql = f"INSERT INTO country_currency.currency (code, currency) VALUES ('{id}', '{name}')" 
            mysql_hook.run(sql) 

    #Task 4
    @task 
    def end_task():
        print("DAG finished") 

    start_task = start_task() 
    fetch_task = fetch_json()
    insert_task = insert_json(fetch_task)
    end_task = end_task()


currency_dag = currency()


