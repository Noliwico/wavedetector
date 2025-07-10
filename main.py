import cv2
import time
from detector.hand_detector import HandDetector

# Constants
WINDOW_NAME = "WaveDetector"
WAVE_DISPLAY_DURATION = 2.0  # seconds
WAVE_TEXT = "You waved at me!"
TEXT_POSITION = (50, 50)
TEXT_FONT = cv2.FONT_HERSHEY_SIMPLEX
TEXT_SCALE = 1.2
TEXT_COLOR = (0, 255, 0)
TEXT_THICKNESS = 3


def display_wave_message(frame):
    """Draws the wave text on the frame."""
    cv2.putText(frame, WAVE_TEXT, TEXT_POSITION, TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)


def run_wave_detector():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    last_wave_time = 0
    show_wave_text = False

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame, hands_detected, wave_detected = detector.find_hands(frame)

        if wave_detected:
            show_wave_text = True
            last_wave_time = time.time()

        if show_wave_text:
            if time.time() - last_wave_time < WAVE_DISPLAY_DURATION:
                display_wave_message(frame)
            else:
                show_wave_text = False

        cv2.imshow(WINDOW_NAME, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_wave_detector()
