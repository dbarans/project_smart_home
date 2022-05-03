from device import Device
from message import MessageType


class HueLight(Device):
    def connect(self) -> None:
        print("Connecting Hue Light")

    def disconnect(self) -> None:
        print("Disconnecting Hue Light")

    def send_message(self, message_type: MessageType, data: str):
        print(f"Hue Light handling message of type {message_type.name} with data [{data}].")

    def status_update(self) -> str:
        print("hue_light_status_ok")


