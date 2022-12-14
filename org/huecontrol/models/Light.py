from org.huecontrol.models.Bridge import Bridge


class Light:

    bridge: Bridge
    id: int
    power: bool
    hue: int
    name: str

    def __init__(self, bridge: Bridge, id: int, power: bool, hue: int, name: str):
        self.bridge = bridge
        self.id = id
        self.power = power
        self.hue = hue
        self.name = name


