import json
import os
import requests
from cachetools.func import ttl_cache
from urllib.error import HTTPError

# Global variables
username = (
    os.getenv("HCOMET_API").split(";")[0].split("=")[1]
)  # username is “AccName___UserID” with 3 underscores
password = (
    os.getenv("HCOMET_API").split(";")[1].split("=")[1]
)  # enter the user's password here
bearerToken = ""  # tokens are set programmatically after login
refreshToken = ""

headers = {"Content-Type": "application/json"}

# Sends login request
@ttl_cache(ttl=4 * 60)
def Login(user, passwrd):
    url = "https://hcomet.haverly.com/api/login"

    payload = ""
    proxies = {"http": os.getenv("HTTP_PROXY"), "https": os.getenv("HTTPS_PROXY")}
    response = requests.request(
        "GET", url, headers=headers, proxies=proxies, data=payload, auth=(user, passwrd)
    )

    if response.status_code == 200:  # success response, set global tokens
        jsonResponse = json.loads(response.text)
        global bearerToken
        global refreshToken
        bearerToken = jsonResponse["token"]
        refreshToken = jsonResponse["refreshToken"]
        return "Login Successful\n"
    elif response.status_code == 500:  # possible user conflict, try override
        print("H/COMET API user conflict... trying override\n")
        return Override(user, passwrd)
    else:  # other errors
        return "Login error: " + response.reason + "\n"


# Sends Override request (if login request has user conflict)
def Override(user, passwrd):
    url = "https://hcomet.haverly.com/api/override"

    payload = ""

    response = requests.request(
        "GET", url, headers=headers, data=payload, auth=(user, passwrd)
    )

    if response.status_code == 200:  # success response, set global tokens
        jsonResponse = json.loads(response.text)
        global bearerToken
        global refreshToken
        bearerToken = jsonResponse["token"]
        refreshToken = jsonResponse["refreshToken"]
        return "Login Successful\n"
    else:  # other errors
        return "Override error: " + response.reason + "\n"


# Sends Refresh Request (when Tokens timeout they must be refreshed with this)
def Refresh():
    global bearerToken
    global refreshToken
    url = "https://hcomet.haverly.com/api/refresh"

    payload = json.dumps(refreshToken)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + bearerToken,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:  # success response, set global tokens
        jsonResponse = json.loads(response.text)
        bearerToken = jsonResponse["token"]
        refreshToken = jsonResponse["refreshToken"]
        return "Refresh Successful\n"
    else:  # other errors
        return "Refresh error: " + response.reason + "\n"


# Sends Logout Request
def Logout():
    url = "https://hcomet.haverly.com/api/logout"

    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 204:  # Success response
        return "Successfully logged out\n"
    else:  # errors
        return "Logout error: " + response.reason + "\n"


def get_token():
    if bearerToken is None or bearerToken == "":
        Login(user=username, passwrd=password)

    return bearerToken


def get_header():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_token(),
    }
    return headers


def generic_api_call(
    set_url: str,
    requestType="GET",
    payload={},
    expected_response_code=200,
    convert="ignore",
):
    # todo rename param to expected_response_code

    response = requests.request(
        requestType, set_url, headers=get_header(), data=payload
    )
    if response.status_code == expected_response_code:
        if convert == "ignore":
            d = response.json()
            return d
        d = response
        return d
    elif response.status_code == 401:
        Refresh()
    else:
        try:
            msg = response.json()["Message"]
        except json.JSONDecodeError:
            msg = response.text
        raise HTTPError(
            url=set_url,
            code=response.status_code,
            msg=msg,
            hdrs=None,
            fp=None,
        )
