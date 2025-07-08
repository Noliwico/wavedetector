# WaveDetector

WaveDetector is a Python application that uses your webcam to detect wave gestures in real time. It leverages [MediaPipe](https://github.com/google/mediapipe) for hand tracking and [OpenCV](https://opencv.org/) for video processing.

## Features
- Real-time hand detection via webcam
- Wave gesture recognition based on motion direction changes
- Visual feedback with live message overlay

## Project Structure
```
WaveDetector/
├── main.py                       # Main entry point
└── detector/
    └── hand_detector.py         # Hand detection and gesture logic
```

## Installation

### Prerequisites
- Python 3.7 or later

### Install dependencies
```bash
pip install opencv-python mediapipe
```

## Usage
Run the main script to start detection:
```bash
python main.py
```

- The program opens your webcam.
- If a wave gesture is detected, the text "You waved at me!" will appear on the screen for 2 seconds.
- Press `q` to quit.

## How Wave Detection Works
- The `HandDetector` tracks the X-coordinate of the index finger.
- If the direction of horizontal motion switches at least twice (left-right-left or right-left-right), and within a set time window, it counts as a wave.
- If no hand is detected, internal counters reset.

## Use Cases
- Fun gesture-based interaction
- Educational projects using computer vision
- Touchless interfaces or public kiosks

## License
MIT License

## Credits
- [MediaPipe](https://mediapipe.dev/) by Google for hand landmark tracking
- [OpenCV](https://opencv.org/) for camera and image handling
