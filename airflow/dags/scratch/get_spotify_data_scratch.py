from airflow.custom_utils.spotify_api.scripts import spotify_auth
from pg_local import PGConn
from airflow import DAG
import requests
import datetime
import json

spotify_api = spotify_auth.SpotifyAPI()


def get_token() -> str:
    token = spotify_api.get_client_token()
    return token


def get_spotify_data(days_ago: int, endpoint):

    """

    :param days_ago: in seconds
    :param endpoint:
    :return:
    """

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    headers = {
        "Authorization": "Bearer {TOKEN}".format(TOKEN=get_token())
    }

    url = "https://api.spotify.com/v1/me/player/recently-played"
    url = "https://api.spotify.com/v1/tracks/4cOdK2wGLETKBW3PvgPWqT"

    # Set the Authorization header with the access token
    # access_token = get_token()

    # Make the API request
    response = requests.get(url, headers=headers)

    data = requests.post("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = requests.get(f"https://api.spotify.com/v1/me/player/recently-played?after={yesterday_unix_timestamp}", headers=headers)

    dd = data.json()








    return None


def main():
    print("")


if __name__ == "__main__":
    main()




