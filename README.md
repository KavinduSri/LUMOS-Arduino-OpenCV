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
```bash
pip install -r requirements.txt
python lumos.py
