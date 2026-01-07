# LUMOS – Arduino + OpenCV

## Tech Stack
- Python
- OpenCV
- MediaPipe
- Arduino UNO
- PySerial

## How it works
- Camera detects hand landmarks
- Distance between **thumb & index finger** is calculated
- That distance controls LEDs via Arduino
- Inspired by the **LUMOS spell**

## Run the project
```bash```
pip install -r requirements.txt
python lumos.py
-------------------------------------------------------------------------------------

## Arduino Setup
=> Components Required
> Arduino UNO
> LEDs
> 220Ω resistors (one per LED)
> Breadboard
> Jumper wires
> USB cable

## Circuit Connection
Connect LED positive (long leg) to Arduino digital pins ( D2–D13)
Connect LED negative (short leg) → 220Ω resistor
Connect resistor → GND on Arduino
Repeat the same for each LED.

## Arduino Code Upload
> Open Arduino IDE
> Connect Arduino UNO via USB
> Select:Board: Arduino UNO
> Port: COM (your Arduino port)
> Open lumos.ino
> Click Upload


