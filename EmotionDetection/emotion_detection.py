"""Detect emotions using the IBM Watson NLP service."""
import requests


def emotion_detector(text_to_analyze):
    """Detect emotions in text using the IBM Watson NLP service."""
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return empty_result

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            url, json=data, headers=headers, timeout=5
        )

        if response.status_code == 400:
            return empty_result

        response.raise_for_status()
        emotions = response.json()["emotionPredictions"][0]["emotion"]

        result = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
        }
        result["dominant_emotion"] = max(
            result, key=result.get
        )
        return result

    except (requests.exceptions.RequestException, KeyError, IndexError, ValueError):
        return empty_result
