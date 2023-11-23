import psycopg2
import json
import os
import pg_local
import configparser


# Create an instance of the PGConn class and call the get_pg_connection method
if __name__ == "__main__":
    conn = pg_local.PGConn()
    conn.get_pg_connection()
