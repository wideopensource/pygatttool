from pygatttool import PyGatttool

OH1_ADDR = "A0:9E:1A:7D:3C:5D"
OH1_CONTROL_ATTRIBUTE_HANDLE = 0x003f
OH1_DATA_ATTRIBUTE_HANDLE = 0x0042
OH1_START_PPG_COMMAND = b'\x02\x01\x00\x01\x82\x00\x01\x01\x16\x00'

if '__main__' == __name__:
    ble = PyGatttool(address=OH1_ADDR)

    ble.connect()
    ble.mtu(232)
    ble.char_write_req(handle=OH1_CONTROL_ATTRIBUTE_HANDLE + 1, value=0x200)
    ble.char_write_req(handle=OH1_DATA_ATTRIBUTE_HANDLE + 1, value=0x100)
    ble.char_write_cmd(handle=OH1_CONTROL_ATTRIBUTE_HANDLE, command=OH1_START_PPG_COMMAND)

    while True:
        print(ble.wait_for_notification(handle=OH1_DATA_ATTRIBUTE_HANDLE))
