# Final Project: Emotion Detection Application

## Project Overview
This project implements an Emotion Detection application using the IBM Watson Natural Language Processing (NLP) service. It analyzes text and identifies five emotions: anger, disgust, fear, joy, and sadness.

## Features
- Detects five emotions from user-provided text.
- Identifies the dominant emotion.
- Provides a web interface using Flask.
- Handles empty input and service errors.
- Includes unit tests for emotion detection.

## Technologies Used
- Python
- Flask
- Requests
- IBM Watson NLP Emotion Detection API
- HTML, CSS, and JavaScript
- Unittest

## Project Structure
- `EmotionDetection/emotion_detection.py` — Emotion detection function.
- `EmotionDetection/__init__.py` — Python package initialization.
- `server.py` — Flask web application.
- `test_emotion_detection.py` — Unit tests.
- `templates/index.html` — Web interface.
- `static/mywebscript.js` — Frontend interaction.

## How to Run
1. Install the required dependencies using `pip install flask requests`.
2. Run the application using `python server.py`.
3. Open `http://127.0.0.1:5000` in a browser.
4. Enter text and click **Run Sentiment Analysis** to view the result.

## Repository
https://github.com/harshadat167-cmd/final-project-emb-ai
