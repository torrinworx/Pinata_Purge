# FOR TESTING AND DEVELOPMENT ONLY, NEVER USE ONCE DEPLOYED.
import copy
import requests

pinata_api_key = ""
pinata_secret_api_key = ""
JWT = ""

API_ENDPOINT = 'https://api.pinata.cloud/'

Headers = {
    "pinata_api_key": pinata_api_key,
    "pinata_secret_api_key": pinata_secret_api_key,
}

# Remove function:
def remove_pin_from_ipfs(hash_to_remove):
    """Removes specified hash pin"""
    url: str = API_ENDPOINT + "pinning/removePinFromIPFS/"
    headers: Headers = copy.deepcopy(Headers)
    headers["Content-Type"] = "application/json"
    body = {"ipfs_pin_hash": hash_to_remove}
    response: requests.Response = requests.post(url=url, json=body, headers=headers)
    return print({"status": response.status_code, "reason": response.reason, "text": response.text}) if not response.ok else print({"message": "Removed"})

# Get pinned hashes:
def pin_jobs():
    """
    Retrieves a list of all the pins that are currently in the pin queue for your user.

    More: https://docs.pinata.cloud/api-pinning/pin-jobs
    """
    url: str = API_ENDPOINT + "data/pinList/"
    response: requests.Response = requests.get(url=url, headers=Headers)
    return response.json() if response.ok else {"status": response.status_code, "reason": response.reason, "text": response.text}


for i in pin_jobs()['rows']:
    remove_pin_from_ipfs(i['ipfs_pin_hash'])
