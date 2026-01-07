import cv2
import mediapipe as mp
import math
import serial
import time


ser = serial.Serial("COM5", 9600)   
time.sleep(2)

# ---------- MEDIAPIPE ----------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(
                result.multi_hand_landmarks,
                result.multi_handedness):

            hand_label = hand_info.classification[0].label  # Left / Right

            # Thumb tip & Index tip
            thumb = hand_landmarks.landmark[4]
            index = hand_landmarks.landmark[8]

            x1, y1 = int(thumb.x * w), int(thumb.y * h)
            x2, y2 = int(index.x * w), int(index.y * h)

            distance = int(math.hypot(x2 - x1, y2 - y1))

            # Draw hand
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.circle(frame, (x1, y1), 6, (0, 255, 0), -1)
            cv2.circle(frame, (x2, y2), 6, (0, 255, 0), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # Display text
            text_y = 50 if hand_label == "Left" else 100
            label_text = f"{hand_label} HD: {distance}"

            cv2.putText(
                frame, label_text, (30, text_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

            #Send ONLY Left Hand Distance to Arduino
            if hand_label == "Left":
                ser.write(f"{distance}\n".encode())

    cv2.imshow("Hand Distance Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
ser.close()
cv2.destroyAllWindows()

