## Deployment and testing notes

### Manual/local Airflow run/setup
helpful commands


### Cheat sheet for commands:
```
airflow cheat-sheet
```

```
https://airflow.apache.org/docs/apache-airflow/stable/start.html

check:
# from ~wokspace/airflow directory:

export AIRFLOW_HOME=~/workspace/airflow
echo $AIRFLOW_HOME

#if not recognizing new dags
airflow db migrate

# pid issues when trying to restart webserver try deleting .pid file:

~/workspace/airflow$ rm -rf airflow-webserver.pid

# find and kill process
ps | grep airflow 

run:
airflow db init && airflow webserver -p 8080 && airflow scheduler




```


### Docker Airflow run/setup