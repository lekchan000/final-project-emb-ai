"""
This module uses the Watson Tone Analyzer API to detect the emotions in a given text.

"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Analyzes the emotions in a given text using the Watson Tone Analyzer API.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: A dictionary containing the emotion scores and dominant emotion.
    """
    # Define the URL for the sentiment analysis API
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Set the headers with the required model ID for the API
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    Input_json = {"raw_document": {"text": text_to_analyze}}

    # Make a POST request to the API with the payload and headers
    response = requests.post(URL, headers=Headers, json=Input_json, timeout=10)

    # If the response status code is 200, extract the emotions from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion,
        }

    elif response.status_code == 500:
        # If the response status code is 500, return None for all emotions
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    # if the response status code is any other unexpected status codes
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
