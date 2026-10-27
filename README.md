# SentraPulse
## Smart Crowd Density Risk Prediction and Safety Alert System

An AI-based prototype that analyzes crowd images, detects people using YOLO, and displays illustrative crowd-risk alerts.

## Technologies
- Python
- Streamlit
- Ultralytics YOLO
- Pillow

## Setup
1. Install Python 3.10 or a compatible version supported by the selected dependencies.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

## Usage
Upload a JPG or PNG crowd image and click Analyze Crowd.

## Limitations
Risk categories use demonstration thresholds based on detected people in one image. They do not represent actual area-based density or validated risk predictions.

## Project Website
https://sec25ci123.github.io/Sentra-Pulse-/
