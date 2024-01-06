import sys
import time
import requests
import datetime
from airflow.custom_utils.spotify_api.scripts.spotify_auth import SpotifyAPI


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

    # Spotify requires the timestamp in milliseconds
    query += f"&after={start_ts}"
    query_url = url + query
    result = requests.get(query_url, headers=headers)

    return result

def main():
    sp = SpotifyAPI()
    print(get_recent())
    result = get_recently_played(sp.get_auth_token(),get_recent())
    print(result.json())
if __name__ == "__main__":
    main()
