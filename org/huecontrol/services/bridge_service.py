from org.huecontrol.requests.hue_requests import post_request, Request_Paths
import pickle
import os


def setup_bridge(bridge_address: str) -> str:
    bridge_response = post_request(bridge_address + str(Request_Paths.API.value),
                                   {'devicetype': 'huecontrol#pythonpackage'})
    if bridge_response.status_code == 200:
        return handle_response(bridge_response.json()[0])
    else:
        handle_error(bridge_response.text)


def handle_response(response) -> str:
    if "error" in response:
        handle_error(response["error"]["description"])
    else:
        persist_username(response)
        return response["success"]["username"]


def username_exists() -> bool:
    return os.path.exists("bridge_user.p")


def persist_username(json_object):
    pickle.dump(json_object["success"], open("bridge_user.p", "wb"))


def delete_username():
    if username_exists():
        os.remove("bridge_user.p")


def read_username() -> str:
    user = pickle.load(open("bridge_user.p", "rb"))
    return user["username"]


def handle_error(message: str):
    print("something went wrong")
    print(message)
    exit(1)
