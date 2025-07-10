# 👋 WaveDetector

A simple real-time hand gesture detector written in Python using OpenCV and MediaPipe.  
It recognizes when a person **waves** at the camera, and displays an on-screen message accordingly.

---

## 🎯 Features

- ✅ Real-time webcam hand detection
- ✅ Wave gesture recognition based on horizontal hand motion
- ✅ On-screen message display upon wave detection
- ✅ Clean, modular code following Clean Code principles
- ✅ Fully cross-platform (Windows, Linux, Raspberry Pi*)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Noliwico/wavedetector.git
cd wavedetector
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the program

```bash
python main.py
```

Press `Q` anytime to quit.

---

## 📦 Dependencies

- Python 3.10+
- OpenCV
- MediaPipe

You can install all required packages using:

```bash
pip install opencv-python mediapipe
```

---

## 🤖 Raspberry Pi Support

This program can run on a Raspberry Pi 4 or 5 (with reduced performance).  
Make sure to use a USB webcam and install compatible versions of OpenCV and MediaPipe.

---


## 📚 Future ideas

- Add GUI (Tkinter or PyQt) with Start/Stop buttons
- Save wave events to log file
- Add sound effect or LED feedback (IoT)

---

## 👨‍💻 Author

Developed by [Noliwico]  
Feel free to contribute or fork the project!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
