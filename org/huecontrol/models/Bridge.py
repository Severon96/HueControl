from org.huecontrol.services.bridge_service import username_exists, setup_bridge, read_username
from org.huecontrol.services.lights_service import get_all_lights, get_light
from org.huecontrol.models.Light import Light


class Bridge:
    bridge_address: str
    username: str

    def __init__(self, bridge_address: str):
        self.bridge_address = bridge_address

        if not username_exists():
            self.username = setup_bridge(self.bridge_address)
        else:
            self.username = read_username()

    def get_all_lights(self) -> [Light]:
        lights: [Light] = []
        response_body = get_all_lights(self.bridge_address, self.username)

        for key in response_body:
            light_response = response_body[key]

            lights.append(
                Light(self, key, light_response["state"]["on"], light_response["state"]["hue"],
                      light_response["name"]))

    def get_light(self, light: int) -> Light:
        response_body = get_light(self.bridge_address, self.username, light)

        return Light(self, light, response_body["state"]["on"], response_body["state"]["hue"], response_body["name"])
