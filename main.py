from iot.service import IOTService
from iot.devices import *
from iot.message import *


def main():
    iot_service = IOTService()
    iot_service.register_device(HueLight)
    iot_service.register_device(SmartSpeaker)
    iot_service.register_device(Curtains)
    id_hue_light = iot_service.devices[0].device_id
    id_smart_speaker = iot_service.devices[1].device_id
    id_curtains = iot_service.devices[2].device_id
    while True:
        menu = input("-----MENU-----\nWAKE UP (W) --- SLEEP (S) --- TEST (T) --- QUIT (Q)\n").upper()
        if menu == "T":
            iot_service.test_devices()
        elif menu == "S":
            message_list = [Message(device_id=id_hue_light, msg_type=MessageType(2), data="turn_off_light"),
                            Message(device_id=id_curtains, msg_type=MessageType(6), data="close_curtain"),
                            Message(device_id=id_smart_speaker, msg_type=MessageType(2), data="turn_off_speaker")]
            iot_service.run_program(message_list)

        elif menu == "W":
            message_list = [Message(device_id=id_hue_light, msg_type=MessageType(1), data="turn_on_light"),
                            Message(device_id=id_curtains, msg_type=MessageType(5), data="open_curtain"),
                            Message(device_id=id_smart_speaker, msg_type=MessageType(1), data="turn_on_speaker"),
                            Message(device_id=id_smart_speaker, msg_type=MessageType(4), data="play_song")]
            iot_service.run_program(message_list)


        elif menu == "Q":
            break


main()
