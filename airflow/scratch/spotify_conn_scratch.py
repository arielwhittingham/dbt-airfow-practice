import time
import requests
import datetime
import configparser
from airflow.custom_utils.spotify_api.scripts.spotify_auth import SpotifyAPI


def get_header(auth_token):
    return {"Authorization": "Bearer " + auth_token}


def get_recent(after_date):
    if after_date == None:
        after_ts = (datetime.datetime.now() - datetime.timedelta(days = 7)).timestamp() * 1000
    else:
        after_ts = datetime.datetime.strptime(after_date,'%Y-%m-%d').timestamp() * 1000


def main():
    print("Spotify Connection Started")
    sp = SpotifyAPI()
    sp.get_auth_token()




def get_recently_played(token, start_date):
    url = "https://api.spotify.com/v1/me/player/recently-played"
    headers = get_auth_header(token)
    limit = 50
    query = f"?limit={limit}"

    # Spotify requires the timestamp in milliseconds
    timestamp_ms = int(start_date.timestamp()) * 1000
    query += f"&after={timestamp_ms}"

    query_url = url + query
    result = get(query_url, headers=headers)

    return json_result




