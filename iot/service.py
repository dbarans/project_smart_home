import random
import string
from iot.diagnostics import collect_diagnostics

# from devices import *


def generate_id(length):
    alphabet = list(string.ascii_uppercase)
    device_id = ""
    for index in range(length):
        letter = random.choice(alphabet)
        device_id += letter
    return device_id


class IOTService:

    def __init__(self):
        self.devices = []

    def register_device(self, device):
        device_id = generate_id(30)
        device_object = device(device_id)
        self.devices.append(device_object)
        device_object.connect()

    def unregister_device(self, device_id):
        for object in self.devices:
            if object.device_id == device_id:
                object.disconnect()
                self.devices.remove(object)
                break

    def get_device(self, device_id):
        for object in self.devices:
            if object.device_id == device_id:
                return object

    def run_program(self, message: list):
        print("=====RUNNING PROGRAM======")

    def test_devices(self):
        print("Start test devices")
        for device in self.devices:
            collect_diagnostics(device)
