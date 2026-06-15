import json, requests


def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Set the headers with the required model ID for the API
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    Input_json = {"raw_document": {"text": text_to_analyze}}

    # Make a POST request to the API with the payload and headers
    response = requests.post(URL, headers=Headers, json=Input_json)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]

    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

    # For any other unexpected status codes, set label and score to None
    else:
        label = None
        score = None

    # Return the label and score in a dictionary
    return {"label": label, "score": score}
