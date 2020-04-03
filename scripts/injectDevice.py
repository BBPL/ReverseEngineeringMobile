import frida
import time
import sys
import os

SCRIPT_PATH = r""
APPLICATION_NAMESPACE = ""
DEVICE_NAME = "emulator-5554"


device = frida.get_device_manager().get_device(DEVICE_NAME)

# f = open('pass.txt', 'a')


def on_message(message, data):
    print(message['payload'])


pid = device.spawn([APPLICATION_NAMESPACE])
device.resume(pid)
time.sleep(0)
session = device.attach(pid)
script = session.create_script(open(SCRIPT_PATH).read())
# script.on('message', on_message)
script.load()
sys.stdin.read()
