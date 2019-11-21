import requests
import urllib3
from requests_ntlm import HttpNtlmAuth

urllib3.disable_warnings()

endpoint = 'https://192.168.10.12/piwebapi'
user = 'piuser'
password = 'piuser'
server = 'PI-IDES'


def eazy_requests(url, params=None):
    resp = requests.get(url, auth=HttpNtlmAuth(user, password), params=params, verify=False)
    return resp
