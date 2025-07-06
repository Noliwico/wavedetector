import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

        # Integetéshez szükséges változók
        self.prev_x = None
        self.motion_direction = None
        self.wave_counter = 0
        self.last_wave_time = 0

    def find_hands(self, frame, draw=True):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)
        hands_detected = False
        wave_detected = False

        if results.multi_hand_landmarks:
            hands_detected = True
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )

                # Kiválasztjuk pl. az indexujj (8. landmark) X pozícióját
                index_finger_tip = hand_landmarks.landmark[8].x

                # Mozgás irányának követése
                if self.prev_x is not None:
                    dx = index_finger_tip - self.prev_x
                    if abs(dx) > 0.02:  # mozgásküszöb (kis elmozdulásokat ne vegyen figyelembe)
                        direction = 'right' if dx > 0 else 'left'
                        if self.motion_direction and self.motion_direction != direction:
                            self.wave_counter += 1
                            # Ha elég gyorsan vált irányt, és már 2-szer
                            if self.wave_counter >= 2 and time.time() - self.last_wave_time > 1.0:
                                wave_detected = True
                                self.wave_counter = 0
                                self.last_wave_time = time.time()
                        self.motion_direction = direction

                self.prev_x = index_finger_tip
        else:
            # reseteljük, ha nincs kéz
            self.prev_x = None
            self.motion_direction = None
            self.wave_counter = 0

        return frame, hands_detected, wave_detected
