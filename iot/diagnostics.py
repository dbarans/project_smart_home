from iot.devices import SmartSpeaker, HueLight, Curtains


def collect_diagnostics(device) -> None:
    print("Connecting to diagnostics server.")
    print(f"Sending status update {device.status_update()} to server.")
