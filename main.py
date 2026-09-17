import cv2
import mediapipe as mp
from vehicle import vehicle_command


# MediaPipe Hand Setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


# Camera Setup
camera = cv2.VideoCapture(0)


# Gesture Stability
last_command = "STOP"
stable_count = 0


while True:

    success, frame = camera.read()

    if not success:
        print("Camera not found")
        break


    # Mirror camera
    frame = cv2.flip(frame, 1)


    # Convert image for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)


    # Default values
    finger_count = 0
    command = "STOP"


    # Hand Detection
    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )


            landmarks = hand_landmarks.landmark


            # Count fingers
            if landmarks[8].y < landmarks[6].y:
                finger_count += 1

            if landmarks[12].y < landmarks[10].y:
                finger_count += 1

            if landmarks[16].y < landmarks[14].y:
                finger_count += 1

            if landmarks[20].y < landmarks[18].y:
                finger_count += 1


            # Gesture Commands
            if finger_count == 0:
                command = "STOP"

            elif finger_count == 1:
                command = "FORWARD"

            elif finger_count == 2:
                command = "LEFT"

            elif finger_count == 3:
                command = "RIGHT"

            elif finger_count == 4:
                command = "STOP"


    else:

        # No hand = STOP
        command = "STOP"


    # Gesture Stability
    if command == last_command:

        stable_count += 1

    else:

        stable_count = 0
        last_command = command


        # Send command only after stable gesture
    if stable_count >= 5:
        vehicle_command(command)
        stable_count = 0

    # Dashboard background
    cv2.rectangle(
        frame,
        (10, 10),
        (460, 180),
        (0, 0, 0),
        -1
    )


    # Title
    cv2.putText(
        frame,
        "SIXTH SENSE",
        (25, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )


    # Finger Count
    cv2.putText(
        frame,
        "Fingers: " + str(finger_count),
        (25, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (0, 255, 0),
        2
    )


    # Command
    cv2.putText(
        frame,
        "Command: " + command,
        (25, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (0, 255, 255),
        2
    )


    # Stability
    cv2.putText(
        frame,
        "Stable: " + str(stable_count),
        (25, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )


    # Show Camera
    cv2.imshow(
        "Sixth Sense - Gesture Vehicle Control",
        frame
    )


    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Cleanup
# Send STOP before closing
vehicle_command("STOP")
camera.release()
hands.close()
cv2.destroyAllWindows()