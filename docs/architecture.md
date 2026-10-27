SentraPulse Architecture

1. Input

The user uploads a crowd image.

2. Image Processing

Pillow prepares the image for analysis.

3. Person Detection

The YOLO model detects people in the uploaded image.

4. Crowd Analysis

The application counts the detected people.

5. Risk Alert

Demo thresholds classify the result as LOW, MODERATE, or HIGH.

6. Output Dashboard

Streamlit displays the detected person count, risk alert, and annotated image.

Current Prototype Limitations

This prototype analyzes a single uploaded image. It does not currently provide live CCTV monitoring, area-based crowd density measurement, or validated future-risk prediction.
