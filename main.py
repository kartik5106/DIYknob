import serial
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import keyboard  # pip install keyboard

def control_davinci(action):
    if action == "0":
        # add or remove the lines to control the volume of the clicks
        keyboard.send("right")
        keyboard.send("right")
        keyboard.send("right")  # move forward in timeline
    elif action == "1":
        keyboard.send("left")
        keyboard.send("left")
        keyboard.send("left")   # move backward
    elif action == "3":
        keyboard.send("space")  

def adjust_volume(level_change):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    current = volume.GetMasterVolumeLevelScalar()  # between 0.0 and 1.0
    if level_change == "0":
        volume.SetMasterVolumeLevelScalar(min(1.0, current + 0.07), None)
    elif level_change == "1":
        volume.SetMasterVolumeLevelScalar(max(0.0, current - 0.07), None)
    elif level_change == "3":
        mute = volume.GetMute()
        volume.SetMute(not mute, None)

def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.001)         # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().strip()
        if data:
            print(data)
            # Control the volume or the timeline based on the data received
            # adjust_volume(data)
            control_davinci(data)


if __name__ == '__main__':
    # Change 'COM9' to your Arduino's serial port
    readserial('COM9', 9600) 