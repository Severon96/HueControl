from org.huecontrol.services.bridge_service import username_exists, setup_bridge, read_username


class Bridge:
    bridge_address: str
    username: str

    def __init__(self, bridge_address: str):
        self.bridge_address = bridge_address

        if not username_exists():
            self.username = setup_bridge(self.bridge_address)
        else:
            self.username = read_username()
