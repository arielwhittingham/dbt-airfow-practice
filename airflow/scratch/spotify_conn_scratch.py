import sys
import time
import requests
import json
import datetime
import os
from airflow.custom_utils.spotify_api.scripts import spotify_auth


def get_header(auth_token):
    return {"Authorization": "Bearer " + auth_token}

def get_recent(after_date=None):
    if after_date is None:
        after_ts = int((datetime.datetime.now() - datetime.timedelta(days = 7)).timestamp() * 1000).__round__(0)
    else:
        after_ts = int(datetime.datetime.strptime(after_date,'%Y-%m-%d').timestamp() * 1000).__round__(0)
    return after_ts

def get_recently_played(token, start_ts):
    url = "https://api.spotify.com/v1/me/player/recently-played"
    headers = get_header(token)
    limit = 50
    query = f"?limit={limit}"

    query += f"&after={start_ts}"
    query_url = url + query
    result = requests.get(query_url, headers=headers)
    return result

def main(run_type = "local"):
    sp = spotify_auth.SpotifyAPI()
    result = get_recently_played(sp.get_auth_token(),get_recent())
    try:
        f = os.makedirs("../data")
    except:
        print("Directory already exists")
    with open(os.path.join("../data",f"spotify_sample_data_from_{run_type}"+datetime.datetime.strftime(datetime.datetime.now(),"_%Y-%m-%d %H:%M:%S.json")),"w") as jsonf:
        json.dump(result.json(),jsonf)
        jsonf.close()



if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            main()
        elif len(sys.argv) == 2:
            main(sys.argv[1])
        else:
            raise Exception("Usage: python3 spotify_conn_scratch.py [run_type]. use either 0 or 1 command line argument")
    except Exception as e:
        print(e)
        exit(1)
