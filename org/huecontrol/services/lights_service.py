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
            print("something went wrong while fetching light")
            print(response_body["error"]["description"])
    else:
        print("something went wrong while fetching light")


def set_light_power(bridge: Bridge, light: int, power: bool):
    response = put_request(
        "{}{}/{}/lights/{}/state".format(bridge.bridge_address, str(Request_Paths.API.value), bridge.username, light),
        {"on": power})

    if response.status_code == 200:
        response_body = response.json()

        if "error" in response_body:
            print("something went wrong while toggling light power")
            print(response_body["error"]["description"])

    else:
        print("something went wrong while toggling light power")


def set_light_color(bridge: Bridge, light: int, hue: int):
    response = put_request(
        "{}{}/{}/lights/{}/state".format(bridge.bridge_address, str(Request_Paths.API.value), bridge.username, light),
        {"on": True, "sat": 254, "bri": 254, "hue": hue})

    if response.status_code == 200:
        response_body = response.json()

        if "error" in response_body:
            print("something went wrong while setting light color")
            print(response_body["error"]["description"])

    else:
        print("something went wrong while setting light color")
