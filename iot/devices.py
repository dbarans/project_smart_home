from iot.device import Device
from iot.message import MessageType


class HueLight(Device):
    def __init__(self, device_id):
        self.device_id = device_id

    def connect(self) -> None:
        print("Connecting Hue Light")

    def disconnect(self) -> None:
        print("Disconnecting Hue Light")

    def send_message(self, message_type: MessageType, data: str):
        print(f"Hue Light handling message of type {message_type.name} with data [{data}].")

    def status_update(self) -> str:
        return "hue_light_status_ok"


class SmartSpeaker(Device):
    def __init__(self, device_id):
        self.device_id = device_id

    def connect(self) -> None:
        print("Connecting Smart Speaker")

    def disconnect(self) -> None:
        print("Disconnecting Smart Speaker")

    def send_message(self, message_type: MessageType, data: str):
        print(f"Smart Speaker handling message of type {message_type.name} with data [{data}].")

    def status_update(self) -> str:
        return "Smart_Speaker_status_ok"


class Curtains(Device):
    def __init__(self, device_id):
        self.device_id = device_id

    def connect(self) -> None:
        print("Connecting Curtains")

    def disconnect(self) -> None:
        print("Disconnecting Curtains")

    def send_message(self, message_type: MessageType, data: str):
        print(f"Curtains handling message of type {message_type.name} with data [{data}].")

    def status_update(self) -> str:
        return "Curtains_status_ok"
