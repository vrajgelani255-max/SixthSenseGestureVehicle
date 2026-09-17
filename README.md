# Sixth Sense Gesture Controlled Vehicle

## Project Overview

This project uses computer vision and hand gestures to control a vehicle.

## Technologies Used

- Python
- OpenCV
- MediaPipe
- Computer Vision

## Gesture Commands

| Finger Count | Command |
|---|---|
| 0 | STOP |
| 1 | FORWARD |
| 2 | LEFT |
| 3 | RIGHT |
| 4 | STOP |

## Features

- Live camera input
- Hand landmark detection
- Finger counting
- Gesture recognition
- Gesture stability
- Automatic STOP when no hand is detected
- Vehicle command system
- Command logging

## Project Files

- `main.py` — Camera and gesture detection
- `vehicle.py` — Vehicle command system
- `requirements.txt` — Required Python packages
- `vehicle_log.txt` — Command log generated during testing

## Future Hardware Integration

The software is designed to be connected to a physical vehicle controller and motor driver.