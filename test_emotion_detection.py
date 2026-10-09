"""Unit tests for the emotion detection module."""

import unittest
from unittest.mock import patch, Mock

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test emotion detection responses."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy_is_dominant(self, mock_post):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.02,
                        "joy": 0.90,
                        "sadness": 0.06,
                    }
                }
            ]
        }
        mock_post.return_value = response

        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request(self, mock_post):
        response = Mock()
        response.status_code = 400
        mock_post.return_value = response

        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])

    def test_empty_text(self):
        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()