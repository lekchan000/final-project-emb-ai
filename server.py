"""Server module for the Emotion Detector application"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


# Initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """
    This function analyzes the text provided in the request arguments and returns the emotion scores and dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    else:
        # Return a formatted string with the emotion scores and dominant emotion
        return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."


@app.route("/")
def render_index_page():
    """This functions executes the flask app and deploys it on localhost:5000"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
