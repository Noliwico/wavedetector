# WaveDetector

WaveDetector is a Python application that detects hand wave gestures in real time using a webcam. It utilizes [MediaPipe](https://github.com/google/mediapipe) for hand landmark detection and [OpenCV](https://opencv.org/) for video capture and display.

## Features
- Real-time webcam hand tracking
- Wave gesture recognition using hand landmark movement
- Visual feedback with bounding boxes and keypoints
- Lightweight and easy to use

## Installation

### Requirements
- Python 3.7+
- OpenCV
- MediaPipe

### Install dependencies
```bash
pip install -r requirements.txt
```
If you don’t have a `requirements.txt` file, manually install:
```bash
pip install opencv-python mediapipe
```

## Usage
Run the application with:
```bash
python main.py
```

This will start capturing video from your default webcam. When a wave gesture is detected, the message `Wave Detected!` will be printed to the console.

## How It Works
- The `WaveDetector` class (in `detector.py`) processes each video frame and extracts hand landmarks.
- It tracks the horizontal movement of the hand across frames.
- If it detects repeated left-right-left motion (or vice versa), it registers a wave.

## Files
- `main.py`: Captures video, runs detection, and displays results.
- `detector.py`: Contains the wave detection logic.

## Example
You’ll see output like this when running:
```
Wave Detected!
Wave Detected!
```
And your webcam feed will be displayed with hand landmarks visualized.

## Use Cases
- Touchless UI for kiosks or public installations
- Gesture control for simple applications
- Fun project for learning computer vision and ML

## License
This project is licensed under the MIT License.

## Credits
- [MediaPipe](https://mediapipe.dev/) for real-time hand tracking
- [OpenCV](https://opencv.org/) for video processing
