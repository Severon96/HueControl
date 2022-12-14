from org.huecontrol.models.Bridge import Bridge
from org.huecontrol.services.lights_service import set_light_power


class Light:

    bridge: Bridge
    id: int
    power: bool
    hue: int
    bri: int
    sat: int
    name: str

    def __init__(self, bridge: Bridge, id: int, response_body: [str, str]):
        self.bridge = bridge
        self.id = id
        self.power = response_body["state"]["on"]
        self.hue = response_body["state"]["hue"]
        self.bri = response_body["state"]["bri"]
        self.sat = response_body["state"]["sat"]
        self.name = response_body["name"]

    def toggle_power(self):
        set_light_power(self.bridge, self.id, not self.power)


