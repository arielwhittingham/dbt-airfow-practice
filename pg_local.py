import psycopg2
import json
import os
import configparser


class PGConn:
    """
    MODULE for CONNECTING TO Postgresql localhost server

    method types:
    "ini": use credentials from .ini
    "env"

    set PGPORT=5433; export PGPORT

    """
    def __init__(self):
        self.method_type = "ini"  # Setting the method_type attribute to "ini" within the __init__ method

    def get_pg_connection(self):
        if self.method_type == "ini":
            parser = configparser.ConfigParser()
            try:
                parser.read("pipeline.ini")
                conn = psycopg2.connect(
                    "dbname=" + parser.get("PG_LOCAL_AIRFLOW", "database")
                    + " user=" + parser.get("PG_LOCAL_AIRFLOW", "username")
                    + " password=" + parser.get("PG_LOCAL_AIRFLOW", "password")
                    + " host=" + parser.get("PG_LOCAL_AIRFLOW", "hostname"),
                    port=parser.get("PG_LOCAL_AIRFLOW", "port")
                )
                print("Connected to Postgres server: " + parser.get("PG_LOCAL_AIRFLOW", "hostname") + " p: " + parser.get("PG_LOCAL_AIRFLOW", "port"))
                return conn
            except FileNotFoundError as exc:
                print(exc.args)

        # elif self.method_type == "env":
        #     return 2

        else:
            return None

