#!/bin/python3
import signal
import os
import time
from evdev import InputDevice, categorize, ecodes
import json
import subprocess
def keyboardInterruptHandler(name):
    print("\nKeyboardInterrupt Detected")
    output = os.popen("xinput list --id-only "+name)
    boardid = output.read()
    os.popen("xinput enable "+boardid)
    print("Enabled "+name)
    exit(0)

class KeyPressed(object):
    def __init__(self, name, idN):
        self.ID_Name = idN
        self.name = name
        EN = self.getEventNo()
        self.dev = InputDevice('/dev/input/event'+str(EN))

    def getEventNo(self):
        while True:
            for i in range(1, 15):
                try:
                    output = os.popen("udevadm info --query=property --name=/dev/input/event"+str(i)+" | grep ID_SERIAL=CHICONY_HP_Basic_USB_Keyboard")
                    ID_SERIAL = output.read()
                    if(ID_SERIAL == "ID_SERIAL="+self.ID_Name+"\n"):
                        return i
                except:
                    print("Could not find keyboard trying again in few secs....")
                    time.sleep(5)

    def DisableKeyboard(self):
        output = os.popen("xinput list --id-only "+self.name)
        boardid = output.read()
        os.popen("xinput disable "+boardid)
        print("Disabled "+self.name)

    def whkey(self, event):
        if event.type == ecodes.EV_KEY:
            key = categorize(event)
            if key.keystate == key.key_down:
                return key.keycode
    def Key(self):
        self.dev.grab()
        for event in self.dev.read_loop():
            if self.whkey(event) != None:
                return self.whkey(event)
                
f = open("Keys.json","r")
Keys = json.loads(f.read())
f.close
f = open("Info.json","r")
Info = json.loads(f.read())
f.close
KeyPressed(Info["KeyboardName"], Info["ID_Name"]).DisableKeyboard()

while True:
    try:
        Key = str(KeyPressed(Info["KeyboardName"], Info["ID_Name"]).Key())[4:]
        cmd = 'echo "'+Keys[Key]+'"'+" | ssh "+Info["username"]+"@"+Info["host"]+""
        print(cmd)
        os.popen(cmd)
    except KeyboardInterrupt:
        keyboardInterruptHandler(Info["KeyboardName"])