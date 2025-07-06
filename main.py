import cv2
from detector.hand_detector import HandDetector

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    wave_detected = False  # egyszerű állapotfigyelés

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame, hands_detected = detector.find_hands(frame)

        if hands_detected:
            if not wave_detected:
                print("👋 Hand detected!")
                wave_detected = True
        else:
            wave_detected = False

        cv2.imshow("WaveDetector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
