import cv2
import mediapipe as mp
import time

class HandDetector:
    # Constants
    MOTION_THRESHOLD = 0.02  # Minimal X movement to consider a direction change
    WAVE_DIRECTION_CHANGES_REQUIRED = 2
    WAVE_TIMEOUT_SECONDS = 1.0  # Min time between two wave detections

    def __init__(self, max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

        # State variables
        self.prev_x = None
        self.motion_direction = None
        self.wave_counter = 0
        self.last_wave_time = 0

    def find_hands(self, frame, draw=True):
        """Detect hands and determine if a wave gesture occurred."""
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)
        hands_detected = False
        wave_detected = False

        if results.multi_hand_landmarks:
            hands_detected = True
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self._draw_landmarks(frame, hand_landmarks)

                wave_detected |= self._process_landmarks(hand_landmarks)

        else:
            self._reset_state()

        return frame, hands_detected, wave_detected

    def _draw_landmarks(self, frame, hand_landmarks):
        """Draw hand landmarks on the frame."""
        self.mp_draw.draw_landmarks(
            frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
        )

    def _process_landmarks(self, hand_landmarks):
        """Analyze hand movement and detect wave gesture."""
        index_finger_x = hand_landmarks.landmark[8].x
        wave_detected = False

        if self.prev_x is not None:
            dx = index_finger_x - self.prev_x

            if abs(dx) > self.MOTION_THRESHOLD:
                current_direction = 'right' if dx > 0 else 'left'

                if self.motion_direction and self.motion_direction != current_direction:
                    self.wave_counter += 1

                    if (
                        self.wave_counter >= self.WAVE_DIRECTION_CHANGES_REQUIRED
                        and time.time() - self.last_wave_time > self.WAVE_TIMEOUT_SECONDS
                    ):
                        wave_detected = True
                        self.wave_counter = 0
                        self.last_wave_time = time.time()

                self.motion_direction = current_direction

        self.prev_x = index_finger_x
        return wave_detected

    def _reset_state(self):
        """Reset internal state if no hands are detected."""
        self.prev_x = None
        self.motion_direction = None
        self.wave_counter = 0
