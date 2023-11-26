import requests
import configparser
import base64
import json


class SpotifyConn:
    """
    Spotify API connected through Ariel's Client
    """

    def __init__(self):
        self.method_type = "ini"  # Setting the method_type attribute to "ini" within the __init__ method

    def get_spotify_token(self) -> str:
        if self.method_type == "ini":
            parser = configparser.ConfigParser()
            auth_url = "https://accounts.spotify.com/api/token"
            try:
                parser.read("pipeline.ini")
                body_params = {"grant_type": "client_credentials"}
                response = requests.post(auth_url, data=body_params, auth=(parser.get("SPOTIFY_AUTH", "CLIENT_ID"), parser.get("SPOTIFY_AUTH", "CLIENT_SECRET")))
                if response.status_code == 200:
                    return json.loads(response.text)["access_token"]
                else:
                    raise requests.exceptions.RequestException("Non-200 Code")
            except FileNotFoundError as exc:
                print(exc.args)
            except requests.exceptions.RequestException as exc:
                print("Invalid Request: " + str(exc.args))
            except Exception as exc:
                print(exc.args)


headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {token}".format(token=TOKEN)
}


