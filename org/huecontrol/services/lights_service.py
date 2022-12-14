from org.huecontrol.requests.hue_requests import get_request, Request_Paths
from org.huecontrol.models.Light import Light


def get_all_lights(bridge_address, username):
    response = get_request(
        "{}{}/{}/lights".format(bridge_address, str(Request_Paths.API.value), username))

    if response.status_code == 200:
        response_body = response.json()

        if "error" not in response_body:
            return response_body

        else:
            print("something went wrong while fetching lights")
            print(response_body["error"]["description"])
    else:
        print("something went wrong while fetching lights")


def get_light(bridge_address: str, username: str, light: int):
    response = get_request(
        "{}{}/{}/lights/{}".format(bridge_address, str(Request_Paths.API.value), username, light))

    if response.status_code == 200:
        response_body = response.json()

        if "error" not in response_body:
            return response_body
        else:
            print("something went wrong while fetching lights")
            print(response_body["error"]["description"])
    else:
        print("something went wrong while fetching lights")
