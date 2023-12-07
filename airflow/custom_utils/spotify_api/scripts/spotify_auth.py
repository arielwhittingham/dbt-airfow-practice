import requests
import configparser
import base64
import json
import datetime


class SpotifyAPI:
    """
    Spotify API connected through Ariel's Client
    https://stackoverflow.com/questions/48572494/structuring-api-calls-in-python
    """

    def __init__(self):
        self.method_type = "ini"  # Setting the method_type attribute to "ini" within the __init__ method
        self.refresh_time = None
        self.token = self._get_and_update_new_token()

    def _get_and_update_new_token(self):
        if self.method_type == "ini":
            parser = configparser.ConfigParser()
            auth_url = "https://accounts.spotify.com/api/token"
            try:
                parser.read("pipeline.ini")
                body_params = {"grant_type": "client_credentials"}
                response = requests.post(auth_url, data=body_params, auth=(parser.get("SPOTIFY_AUTH", "CLIENT_ID"), parser.get("SPOTIFY_AUTH", "CLIENT_SECRET")))
                if response.status_code != 200:
                    raise requests.exceptions.RequestException("Non-200 Response Code.")
                else:
                    self.refresh_time = datetime.timedelta(seconds=json.loads(response.text)["expires_in"]) + datetime.datetime.now()
                    self.token = json.loads(response.text)["access_token"]
                    return self.token
            except FileNotFoundError as exc:
                print(exc.args)
            except requests.exceptions.RequestException as exc:
                print("Invalid Request: " + str(exc.args))
            except Exception as exc:
                print(exc.args)

    def check_to_get_new_token(self):
        if datetime.datetime.now() > self.refresh_time:
            return True

    def get_token(self):
        if self.check_to_get_new_token():
            return self._get_and_update_new_token()
        else:
            return self.token


class SpotifyAPIData(SpotifyAPI):

    def __init__(self):
        super().__init__()
        self.token = super()._get_and_update_new_token()

    def create_get_request(self, url, headers=None):
        token = super().get_token()

        headers = {"Authorization": "Bearer " + token}

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def make_post_request(self, url, data, headers=None):
        access_token = self.get_access_token()
        if headers is None:
            headers = {"Authorization": "Bearer " + access_token}






