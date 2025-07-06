import cv2
import time
from detector.hand_detector import HandDetector

def main():
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
            print("👋 Wave detected!")
            show_wave_text = True
            last_wave_time = time.time()

        # Ha 2 másodpercen belül vagyunk az utolsó integetéstől, mutatjuk a feliratot
        if show_wave_text:
            if time.time() - last_wave_time < 2.0:
                cv2.putText(frame, "👋 Wave detected!", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            else:
                show_wave_text = False

        cv2.imshow("WaveDetector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
