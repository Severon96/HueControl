from org.huecontrol.requests.hue_requests import get_request, put_request, Request_Paths
from org.huecontrol.models.Bridge import Bridge


def get_all_lights(bridge: Bridge):
    response = get_request(
        "{}{}/{}/lights".format(bridge.bridge_address, str(Request_Paths.API.value), bridge.username))

    if response.status_code == 200:
        response_body = response.json()

        if "error" not in response_body:
            return response_body

        else:
            print("something went wrong while fetching lights")
            print(response_body["error"]["description"])
    else:
        print("something went wrong while fetching lights")


def get_light(bridge: Bridge, light: int):
    response = get_request(
        "{}{}/{}/lights/{}".format(bridge.bridge_address, str(Request_Paths.API.value), bridge.username, light))

    if response.status_code == 200:
        response_body = response.json()

        if "error" not in response_body:
            return response_body
        else:
            print("something went wrong while fetching lights")
            print(response_body["error"]["description"])
    else:
        print("something went wrong while fetching lights")


def set_light_power(bridge: Bridge, light: int, power: bool):
    response = put_request(
        "{}{}/{}/lights/{}/state".format(bridge.bridge_address, str(Request_Paths.API.value), bridge.username, light), { "on": power})
    print(response.json())
