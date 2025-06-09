Emotion Detection with DeepFace
This project uses the DeepFace library to analyze facial emotions in images. It downloads images representing different emotions from provided URLs, processes them to detect the dominant emotion, and displays the results with the expected and detected emotions.
Features

Downloads images for seven emotions: disgust, happy, sad, angry, surprise, neutral, and fear.
Uses DeepFace to perform facial emotion analysis.
Displays each image with its expected and detected emotion using Matplotlib.
Saves downloaded images in an emotion_images directory.

Requirements

Python 3.x
Libraries: os, cv2 (OpenCV), requests, deepface, matplotlib
Install dependencies using:pip install opencv-python requests deepface matplotlib



Usage

Clone the repository:git clone <repository-url>
cd <repository-directory>


Run the script:python emotion_detection.py


The script will:
Create an emotion_images directory if it doesn't exist.
Download images for each emotion.
Analyze each image using DeepFace to detect the dominant emotion.
Display the images with titles showing the expected and detected emotions.



File Structure

emotion_detection.py: Main script for downloading images, analyzing emotions, and displaying results.
emotion_images/: Directory where downloaded images are saved.
README.md: Project documentation.

Notes

Ensure a stable internet connection for downloading images.
The DeepFace library requires a face to be detected in the image. If face detection fails, an error will be printed for that image.
The script uses enforce_detection=True to ensure face detection is performed, which may raise exceptions for images without detectable faces.

License
This project is licensed under the MIT License. See the LICENSE file for details.
