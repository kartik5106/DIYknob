
This project turns your **Arduino Nano + Rotary Encoder** into a **PC media control knob** or **timeline scrubber** for video editors like DaVinci Resolve.  
Since the Nano doesn't support USB HID, we use **serial communication** + a **Python script** to interpret encoder signals and send keyboard/media commands.

---

## 📦 Components Required

| Item                      | Quantity | Notes |
|---------------------------|----------|-------|
| ✅ Arduino Nano            | 1        | Or any non-HID microcontroller |
| 🔁 Rotary Encoder with Button | 1     |  
| 🔌 Jumper wires            | 5+       | Female-to-Female |
| 🪛 USB Cable (Mini USB)     | 1        | For connecting Nano to PC |

---

## 🔧 Wiring Diagram [reference](https://newbiely.com/tutorials/arduino-nano/arduino-nano-rotary-encoder)

<img width="1717" height="765" alt="image" src="https://github.com/user-attachments/assets/02cf1afd-5a29-4840-bd51-7bef52e60895" /># 🎛️ Rotary Encoder + Arduino Nano + Python = USB Volume/Timeline Controller

| Rotary Encoder Pin | Connect To |
|--------------------|------------|
| **CLK**            | Nano Pin D2 |
| **DT**             | Nano Pin D3 |
| **SW (Button)**    | Nano Pin D4 |
| **VCC**            | 5V          |
| **GND**            | GND         |

---

-Upload the arduino_code_knob.ino to Nano via Arduino IDE
-connect the nano (test and see if you are the sensor is working properly)
-run the python code (after installing the requirements)
-Modify Python code to your liking 

## 🧠 How It Works

- Arduino Nano detects rotary encoder movement and button press.
- It sends `"0"`, `"1"`, or `"3"` via serial:
  - `"0"` = Clockwise
  - `"1"` = Counter-clockwise
  - `"3"` = Button press
- Python script reads serial data:
  - You can choose to:
    - 🔊 Adjust volume using `pycaw`
    - 🎞️ Control DaVinci Resolve timeline using `keyboard`

---
